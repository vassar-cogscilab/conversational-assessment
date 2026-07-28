# CLAUDE.md

Guidance for working in this repository.

## What this is

A conversational assessment app: an LLM "examiner" conducts a short oral exam
with a student about **the mean as a model**, decides turn by turn what it
believes the student does and doesn't understand, and ends with a judgement of
`Poor` or `High`. It is built and deployed — `https://cogsciresearch.vassar.edu/convo/`.

Two pages, both static: `index.html` is the student's chat view, and
`instructor.html` shows the evaluation summary for the current session. The
frontend holds no logic beyond rendering and `localStorage`; every decision is
made by the backend.

One exam turn is:

1. The student's answer is embedded and used to retrieve passages from the
   course text (RAG), which are prepended to that turn's message.
2. The examiner model is called with the whole transcript, the system prompt
   from `backend/examiner_prompt.txt`, and a **JSON schema** it must conform to
   (`EXAMINER_SCHEMA` in `backend/app.py`).
3. The parsed reply yields the next question plus the examiner's belief state;
   the belief is rendered into a sentence and appended to the transcript as the
   assistant turn, so the model reads its own prior beliefs back.
4. After `conversation_state: "finished"` or `MAX_TURNS` (12), the session gets
   an `evaluation_summary`.

## Repository layout

```
frontend/public/   Static frontend — plain HTML/CSS/JS, no bundler.
                   index.html (student), instructor.html (summary view).
backend/           Python/Flask backend (gunicorn) run under pm2 as "convo-api" (port 3001).
                   app.py (routes + session store), llm.py (model calls),
                   examiner_prompt.txt (the examiner's system prompt).
RAG_5-9/           Course-text corpus + vector DB used by the live backend
                   (Voyage AI embeddings). Deployed alongside the backend.
RAG_5-9_ollama/    Parallel copy embedded with a local Ollama model. Reference
                   only — not used by the live backend. See its README.
testing/           Offline trial harness (simulated student vs. examiner).
deploy/            Apache reverse-proxy config installed on the server.
.github/workflows/ deploy.yml — push-to-main auto-deploy.
DEPLOY.md          Full deployment runbook (server setup, secrets, ops).
```

## Deployment — the critical constraints

The app is served under a **subpath** on a shared lab server, not at a domain
root. This shapes how the app must be built. Full details in `DEPLOY.md`; the
non-negotiables:

| URL | Served by |
| --- | --- |
| `https://cogsciresearch.vassar.edu/convo/` | Static files in `/var/www/html/convo/` (Apache, directly) |
| `https://cogsciresearch.vassar.edu/convo/api/` | Apache proxy → `http://127.0.0.1:3001` (Flask/gunicorn + pm2) |

1. **Frontend must use base path `/convo/`.** It currently ships as plain files
   from `frontend/public` with no build step, and calls the API via the
   **relative** path `api/...`, which is what makes the subpath work. If you add
   a bundler, set the base (Vite `base: '/convo/'`, CRA `"homepage": "/convo"`,
   Next `basePath: '/convo'`) or every asset and route 404s; emit to
   `frontend/dist`, set `FRONTEND_SRC: frontend/dist` in
   `.github/workflows/deploy.yml`, and uncomment its build step.
2. **All API routes live under `/convo/api/`.** The bare `/api/` route on the
   server belongs to a different app — do not use it. The backend itself sees
   prefix-stripped paths (e.g. request to `/convo/api/health` arrives as
   `/health`).
3. **Backend listens on port 3001, bound to `127.0.0.1`.** Public traffic only
   comes through Apache. Port 3000 is taken by another app.

## How deploys happen

Push to `main` → GitHub Actions rsyncs the frontend, the backend, and `RAG_5-9/`
to the EC2 box and runs `pm2 startOrReload`. No manual steps; it can also be
triggered from the Actions tab.

`RAG_5-9/` lands at `~/RAG_5-9` — a **sibling** of `~/convo-api`, not inside it,
because `app.py` resolves it as `BASE_DIR.parent / "RAG_5-9"`. Moving either one
without the other breaks startup.

## Environment / runtime notes

- Server: Amazon Linux 2023, **Apache (httpd)** — not nginx. **No Docker**; the
  convention is static folders + pm2-managed processes. Match that style — pm2
  (running under Node/nvm) supervises the Python process too.
- The backend is **Python/Flask served by gunicorn**, run from a project
  virtualenv (`backend/venv`). Deps are pinned in `backend/requirements.txt`;
  the deploy creates the venv if missing and `pip install`s into it on every
  push. pm2 launches `./venv/bin/gunicorn app:app` (see `ecosystem.config.js`).
- The backend loads `.env` via `python-dotenv` (`load_dotenv()` in `app.py`).
  The deploy writes that `.env` from the `LLM_API_KEY` secret as
  `ANTHROPIC_API_KEY`. `/convo/api/health` reports `hasApiKey` to confirm it
  loaded (without exposing the key), plus the active `backend` and `model`.
- Secrets/env: copy `.env.example` → real `.env` (gitignored). Document any new
  env var you introduce.
- **The deploy rewrites `~/convo-api/.env` wholesale on every push.** Anything
  set by hand on the server is lost on the next deploy — wire new vars through
  the `Write backend .env` step in `deploy.yml` (secrets via `secrets.`,
  non-secret config via repo `vars.`).
- **The server runs Python 3.9.** PEP 604 unions (`str | None`) raise a
  `TypeError` at import time there even though they parse fine locally; use
  `from __future__ import annotations` in any module that wants them.
  `list[str]` is fine (3.9 has PEP 585).

## Sessions — why there is exactly one worker

Sessions live in a plain in-memory dict in `app.py`, written to
`backend/sessions.json` after every mutation and reloaded at startup, so a
restart doesn't lose history. That file is gitignored and is also what the
`/admin/sessions` endpoints read.

**This requires a single gunicorn worker** (`--workers 1`, set in
`ecosystem.config.js`). A second worker would keep its own copy of the dict and
the two would clobber each other's writes to disk. Raising the worker count
means replacing the session store first — it is not a config knob.

Each session records the transcript, the retrieved RAG context per turn, and a
`turn_log` holding the examiner's reasoning and belief for each turn. The
reasoning is the model's own thinking output, not a restatement it was asked to
produce, which is why it's trustworthy as an audit trail.

## The examiner's LLM backend

`backend/llm.py` is the single entry point for model calls, shared by
`backend/app.py` and `testing/run_trials.py` so the trial harness can't drift
from what the deployed examiner does. It has two interchangeable backends,
selected by the `LLM_BACKEND` env var:

- `anthropic` (**default**) — Claude via the Anthropic API.
- `ollama` — a self-hosted Ollama server on the lab's GPU box (`lambda-server`),
  reached over Tailscale. Uses Ollama's **native** `/api/chat`, not its
  OpenAI-compatible `/v1` endpoint: only the native one exposes `think` and
  `format` together, and dropping either would cost the admin-visible reasoning
  trail (`turn_log[].reasoning`) or the schema guarantee.

Anthropic stays the default deliberately — the Ollama path adds a dependency on
the tailnet and on one GPU box being up, and keeping the fallback one env var
away makes an outage a config change rather than a rollback. Flip backends by
setting the `LLM_BACKEND` **repository variable** and re-running the deploy.

Both backends return the same `(text, thinking)` pair, so callers never branch.
`/convo/api/string` returns **503** (not 500) when a backend is unreachable or
returns something unparseable, and does not write to the session until the turn
has fully succeeded — the transcript must stay strictly alternating or the
session is permanently wedged.

## RAG

`RAG_5-9/` is the live path: chunked course text embedded with Voyage AI
(`voyage-4-large`, 1024-dim), stored in `data/my_contextual_db/contextual_vector_db.pkl`.
It needs `VOYAGE_API_KEY` and outbound internet — swapping the examiner's LLM
backend does not change this.

`RAG_5-9_ollama/` is the same corpus embedded with a local Ollama model
(`nomic-embed-text`, 768-dim). **The two `.pkl` files are not interchangeable** —
pairing one folder's database with the other's `database_engine.py` silently
returns meaningless similarity results rather than erroring.

## Testing

`testing/run_trials.py` runs simulated exams: a student-persona bot answers the
examiner, and the harness reports whether the examiner reached the persona's
expected verdict. Four personas (two `Poor`, two `High`) live in
`testing/ccode_student_prompts/`; results land in `testing/*_results.json`.

It imports `backend/llm.py`, so `--examiner-backend` / `--student-backend` let
you A/B a backend change. Keep the student on Anthropic when varying the
examiner — otherwise both sides of the conversation move at once and the numbers
aren't attributable.

It embeds via `RAG_5-9_ollama`, so it needs a **local** `ollama serve` with
`nomic-embed-text` pulled. That is separate from, and unrelated to, the
`LLM_BACKEND=ollama` setting, which points at the remote GPU box.

> `testing/batch_questioner.py` is stale and does not run: it reads
> `questioner_prompt.txt`, `evaluator_prompt.txt`, and `testing/RAG_5-9/`, none
> of which exist in the repo. `testing/claude_student_prompts/` is likewise
> unreferenced by the current harness. Fix or delete rather than copying either
> as a pattern.

## Cautions

- **It's a shared production server** hosting many other people's experiments
  under `/var/www/html`. A broken Apache config takes them all down — always
  `sudo apachectl configtest` before `sudo systemctl reload httpd`.
- TLS is Let's Encrypt with auto-renewal via a `certbot-renew.timer` systemd
  timer (cron is not installed on this box).
- The frontend renders examiner questions with `textContent`, so any Markdown
  the model emits reaches the student as literal asterisks. Keep the examiner
  answering in plain prose.

## Conventions

- Keep the frontend a static build deployed to the docroot; keep the backend a
  single pm2 service. Don't introduce Docker/containers — it fights the grain of
  this server.
- **Call the LLM only from the backend.** The frontend must never hold an API
  key, and the Caddy-fronted campus gateway can't serve browsers anyway: its
  CORS preflight is unauthenticated and returns 401.
- The examiner runs `claude-sonnet-5` by default; override with `ANTHROPIC_MODEL`
  (or `OLLAMA_MODEL` on the Ollama path) rather than hardcoding a model. Keep API
  keys in env, never in the repo.
- Model calls go through `backend/llm.py`. Adding a second call site that talks
  to a provider SDK directly re-creates the drift between the app and the trial
  harness that `llm.py` exists to prevent.
