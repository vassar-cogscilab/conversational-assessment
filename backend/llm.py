"""
Examiner LLM backend — Anthropic's API or a self-hosted Ollama server.

Which one runs is selected by the LLM_BACKEND env var:

    anthropic  (default)  Claude via the Anthropic API.
    ollama                Ollama on the lab's GPU box (lambda-server), reached
                          over Tailscale at OLLAMA_HOST.

Both backends return the same ``(text, thinking)`` pair, so callers never branch
on which one is active. Anthropic stays the default deliberately: the Ollama
path adds a dependency on the tailnet and on a single GPU box being up, and
keeping the fallback one env var away makes an outage a config change rather
than a code rollback.

Shared by backend/app.py (the live examiner) and testing/run_trials.py (the
offline trial harness) so the two can't drift — the harness only produces
meaningful numbers if it calls the model exactly the way the app does.
"""
# The deploy box (Amazon Linux 2023) runs Python 3.9, where PEP 604 unions like
# `str | None` are a TypeError at def time rather than a syntax feature. This
# defers annotation evaluation so they're never executed; without it the module
# fails to import on the server even though it's fine locally.
from __future__ import annotations

import os

import anthropic

DEFAULT_MAX_TOKENS = 4096

ANTHROPIC_DEFAULT_MODEL = "claude-sonnet-5"
OLLAMA_DEFAULT_MODEL = "gemma4:26b"
OLLAMA_DEFAULT_HOST = "http://lambda-server:11434"

# Ollama can be slow on the first call after an idle stretch: it unloads models
# once OLLAMA_KEEP_ALIVE expires, and gemma4:26b is ~17 GB to page back onto the
# GPUs. Too short a timeout turns that cold start into a spurious failure for
# whichever student happens to go first.
OLLAMA_TIMEOUT_SECONDS = float(os.environ.get("OLLAMA_TIMEOUT", "300"))

# Appended to the system prompt on the Ollama path only. The frontend renders
# examiner questions with textContent (frontend/public/app.js), so Markdown
# reaches the student as literal asterisks. Claude already answers in plain
# prose here; the open models do not reliably. Scoping the correction to the
# backend that needs it avoids perturbing a prompt that's already been tuned
# and measured against Claude.
OLLAMA_PLAIN_TEXT_RULE = (
    "\n\nFormatting: write in plain text only. Do not use Markdown of any kind "
    "— no **bold**, no *italics*, no bullet or heading syntax. The interface "
    "shows your text verbatim, so any markup appears literally to the student."
)


class LLMError(RuntimeError):
    """A backend was unreachable, errored, or returned an unusable response."""


def active_backend(backend: str | None = None) -> str:
    return (backend or os.environ.get("LLM_BACKEND") or "anthropic").strip().lower()


def active_model(backend: str | None = None) -> str:
    if active_backend(backend) == "ollama":
        return os.environ.get("OLLAMA_MODEL", OLLAMA_DEFAULT_MODEL)
    return os.environ.get("ANTHROPIC_MODEL", ANTHROPIC_DEFAULT_MODEL)


def _inject_rag_context(msgs: list[dict], rag_context: str | None) -> list[dict]:
    # Retrieved context rides on the newest message rather than the system
    # prompt, so it changes every turn without invalidating any prefix cached
    # ahead of it. Shared by both backends so the text the model sees is
    # identical apart from backend-specific plumbing.
    if not rag_context:
        return msgs
    latest = msgs[-1]
    msgs[-1] = {
        **latest,
        "content": f"<verified_context>\n{rag_context}\n</verified_context>\n\n{latest['content']}",
    }
    return msgs


# Constructed on first use rather than at import. anthropic.Anthropic() raises
# without an API key, which would otherwise make importing this module fail on
# an Ollama-only deployment that legitimately has no Anthropic key.
_anthropic_client: anthropic.Anthropic | None = None


def _call_anthropic(messages, prompt, rag_context, output_schema, max_tokens):
    global _anthropic_client
    if _anthropic_client is None:
        _anthropic_client = anthropic.Anthropic()

    msgs = [dict(m) for m in messages]

    system = [{"type": "text", "text": prompt, "cache_control": {"type": "ephemeral"}}]

    # Cache everything through the prior turn so each call only pays to process
    # the newest message, instead of re-processing the whole growing transcript
    # uncached every time. The breakpoint has to sit before wherever rag_context
    # gets injected below — a block that changes every turn would otherwise
    # invalidate any cache breakpoint that comes after it.
    if len(msgs) >= 2:
        prior = msgs[-2]
        msgs[-2] = {
            **prior,
            "content": [{"type": "text", "text": prior["content"], "cache_control": {"type": "ephemeral"}}],
        }

    msgs = _inject_rag_context(msgs, rag_context)

    kwargs = {}
    if output_schema:
        kwargs["output_config"] = {"format": {"type": "json_schema", "schema": output_schema}}

    # display: "summarized" is required to get readable text back on Sonnet 5 —
    # thinking runs adaptively either way, but the .thinking field is empty
    # under the default "omitted" display. This is the source of truth for
    # the examiner's admin-visible reasoning trail (see turn_log in /string),
    # rather than asking the model to restate its reasoning in a schema field.
    response = _anthropic_client.messages.create(
        model=os.environ.get("ANTHROPIC_MODEL", ANTHROPIC_DEFAULT_MODEL),
        max_tokens=max_tokens,
        thinking={"type": "adaptive", "display": "summarized"},
        system=system,
        messages=msgs,
        **kwargs,
    )
    if response.stop_reason == "max_tokens":
        raise LLMError(
            "Claude response was truncated (hit max_tokens) before finishing — "
            "increase max_tokens in call_llm."
        )
    text = next(block.text for block in response.content if block.type == "text")
    thinking = next((block.thinking for block in response.content if block.type == "thinking"), "")
    return text, thinking


def _ollama_keep_alive():
    # Ollama accepts either a number of seconds or a duration string ("30m");
    # a negative number means "never unload". It parses a bare "-1" only as a
    # number, so send numeric values as ints and pass anything else through as
    # the duration string it looks like.
    raw = os.environ.get("OLLAMA_KEEP_ALIVE", "-1")
    try:
        return int(raw)
    except ValueError:
        return raw


def _call_ollama(messages, prompt, rag_context, output_schema, max_tokens):
    # Imported lazily: httpx arrives as an anthropic dependency, and keeping the
    # import next to its only use makes the coupling obvious.
    import httpx

    host = os.environ.get("OLLAMA_HOST", OLLAMA_DEFAULT_HOST).rstrip("/")
    model = os.environ.get("OLLAMA_MODEL", OLLAMA_DEFAULT_MODEL)

    msgs = _inject_rag_context([dict(m) for m in messages], rag_context)

    # No cache_control equivalent here, and none needed: Ollama reuses the KV
    # cache for a stable prompt prefix automatically. Because RAG context is
    # injected into the last message only (see _inject_rag_context), the ~16 KB
    # system prompt and the settled transcript stay byte-identical turn to turn
    # and land in that reuse window.
    options = {"num_predict": max_tokens}

    # llama3.3:70b overflows VRAM at the server's default 128K context and falls
    # back to CPU (~2.4 tok/s vs ~12); it needs OLLAMA_NUM_CTX=32768. The gemma4
    # models use sliding-window attention and are fine at the default, so this
    # stays unset unless someone asks for it.
    num_ctx = os.environ.get("OLLAMA_NUM_CTX")
    if num_ctx:
        options["num_ctx"] = int(num_ctx)

    payload = {
        "model": model,
        "stream": False,
        # Ollama's native /api/chat, not its OpenAI-compatible /v1 endpoint:
        # only the native one exposes think and format together, and dropping
        # either would cost the reasoning trail or the schema guarantee.
        "think": True,
        "keep_alive": _ollama_keep_alive(),
        "options": options,
        "messages": [
            {"role": "system", "content": prompt + OLLAMA_PLAIN_TEXT_RULE},
            *msgs,
        ],
    }
    if output_schema:
        # Constrained decoding against the JSON schema, so the reply parses as
        # the caller's shape rather than merely being asked to.
        payload["format"] = output_schema

    try:
        response = httpx.post(f"{host}/api/chat", json=payload, timeout=OLLAMA_TIMEOUT_SECONDS)
        response.raise_for_status()
        data = response.json()
    except httpx.HTTPError as exc:
        raise LLMError(
            f"Ollama request to {host} failed: {exc}. Check that the tailnet is "
            f"up (tailscale status) and that lambda-server is serving 11434."
        ) from exc

    if data.get("error"):
        raise LLMError(f"Ollama returned an error: {data['error']}")

    message = data.get("message") or {}
    text = message.get("content") or ""
    thinking = message.get("thinking") or ""

    if data.get("done_reason") == "length":
        raise LLMError(
            "Ollama response was truncated (hit num_predict) before finishing — "
            "increase max_tokens in call_llm."
        )
    if not text.strip():
        raise LLMError("Ollama returned an empty response.")

    return text, thinking


def call_llm(
    messages,
    prompt,
    rag_context=None,
    output_schema=None,
    max_tokens=DEFAULT_MAX_TOKENS,
    backend=None,
):
    """Run one examiner turn and return ``(text, thinking)``.

    ``thinking`` is the model's reasoning summary, which may be empty — nothing
    downstream should depend on it being populated.

    Raises LLMError for anything the caller can't parse or recover from.
    """
    selected = active_backend(backend)
    if selected == "anthropic":
        return _call_anthropic(messages, prompt, rag_context, output_schema, max_tokens)
    if selected == "ollama":
        return _call_ollama(messages, prompt, rag_context, output_schema, max_tokens)
    raise LLMError(f"Unknown LLM_BACKEND {selected!r} — expected 'anthropic' or 'ollama'.")
