const chatEl = document.querySelector(".chat");
const chatForm = document.querySelector(".input");
const inputField = document.getElementById("input");
const submitBtn = document.getElementById("submit-btn");
const clearBtn = document.getElementById("clear-btn");
const printBtn = document.querySelector(".print-btn");

const revealBox = document.querySelector('.reveal');
const testBox = document.querySelector('.test');
const continueBtn = document.querySelector('.instructions .continue-btn');
const instructionBox = document.querySelector('.instructions');

const infoBox = document.querySelector('.info');

const local = ["127.0.0.1", "localhost"].includes(location.hostname)
  ? "http://127.0.0.1:3001"
  : "api";

// Older versions could save the text "null" or "undefined" as the session id,
// so treat those as "no session".
const savedId = localStorage.getItem("session_id");
let sessionId = savedId && savedId !== "null" && savedId !== "undefined" ? savedId : null;

// ---------- Session id + instructor link ----------
// The link is rebuilt every time the session id changes, so it never shows a
// stale id (or "null") after a new session starts.
function renderSessionInfo() {
  infoBox.replaceChildren("Instructor View: ");
  if (!sessionId) {
    infoBox.append("starting a session…");
    return;
  }
  const link = document.createElement("a");
  // Relative to this page, so it works locally and at /convo/ on the server
  link.href = `teacher/#student/${encodeURIComponent(sessionId)}`;
  link.textContent = `student-${sessionId}`;
  link.target = "_blank";
  link.rel = "noopener";
  infoBox.appendChild(link);
}

function setSessionId(id) {
  sessionId = id;
  localStorage.setItem("session_id", id);
  renderSessionInfo();
}

renderSessionInfo();

// ---------- Instructions panel ----------
function showInitialView() {
  if (localStorage.getItem("seen_instructions") == "false") {
    instructionBox.style.display = "flex";
    testBox.style.display = "none";
    return;
  }
  else {
    instructionBox.style.display = "none";
    testBox.style.display = "flex";
  }
}

continueBtn.addEventListener("click", () => {
  localStorage.setItem("seen_instructions", "true");
  testBox.style.display = "flex";
  instructionBox.style.display = "none";
});

// ---------- Messages ----------
function renderMessage(role, content) {
  const div = document.createElement("div");
  div.className = "message " + role;
  div.textContent = content;
  chatEl.appendChild(div);
  chatEl.scrollTo({ top: chatEl.scrollHeight, behavior: "smooth" });
}

// persist = false for notices that shouldn't come back after a reload
function appendMessage(role, content, persist = true) {
  renderMessage(role, content);
  if (!persist) return;

  const history = JSON.parse(localStorage.getItem("chat_display") || "[]");
  history.push({ role, content });
  localStorage.setItem("chat_display", JSON.stringify(history));
}

// ---------- Sessions ----------
async function startNewSession() {
  const res = await fetch(`${local}/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ session_id: null, input: null }),
  });
  if (!res.ok) throw new Error("Could not start a session (" + res.status + ")");

  const data = await res.json();
  if (!data.session_id) throw new Error("Server did not return a session id");

  localStorage.removeItem("chat_display");
  chatEl.innerHTML = "";
  setSessionId(data.session_id);
  appendMessage("assistant", data.server_message);
}

window.onload = async function () {
  localStorage.setItem("seen_instructions", "false");
  showInitialView();

  try {
    let history = null;
    try { history = JSON.parse(localStorage.getItem("chat_display") || "null"); } catch {}

    if (sessionId && Array.isArray(history) && history.length) {
      history.forEach(msg => renderMessage(msg.role, msg.content));
      renderSessionInfo();
    } else {
      await startNewSession();
    }
  } catch (err) {
    console.error("Error:", err);
    appendMessage("assistant", "Error: Could not reach the backend AI server.", false);
  }
};

// ---------- Input ----------
inputField.addEventListener("keydown", function (e) {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    submitBtn.click();
  }
});

chatForm.addEventListener("submit", async function (e) {
  e.preventDefault();

  const userInputValue = inputField.value.trim();
  if (!userInputValue) return;
  if (!sessionId) return; // still starting up

  appendMessage("user", userInputValue);
  inputField.value = "";
  submitBtn.disabled = true;

  const typingEl = document.createElement("div");
  typingEl.className = "typing-indicator";
  typingEl.innerHTML = "<span></span><span></span><span></span>";
  chatEl.appendChild(typingEl);
  chatEl.scrollTo({ top: chatEl.scrollHeight, behavior: "smooth" });

  try {
    const res = await fetch(`${local}/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ session_id: sessionId, input: userInputValue }),
    });

    typingEl.remove();

    if (res.status === 404) {
      // The server no longer knows this session (for example it was reset).
      // Start a fresh one and give the person their text back.
      await startNewSession();
      appendMessage(
        "assistant",
        "Your earlier session had expired, so a new conversation was started. Please send your message again.",
        false
      );
      inputField.value = userInputValue;
      return;
    }

    if (!res.ok) throw new Error("Server returned an error");

    const data = await res.json();
    appendMessage("assistant", data.server_message || "No response from server.");
  } catch (err) {
    typingEl.remove();
    console.error("Error:", err);
    appendMessage("assistant", "Error: Could not reach the backend AI server.");
  } finally {
    submitBtn.disabled = false;
    inputField.focus();
  }
});

clearBtn.addEventListener("click", async function () {
  if (!confirm("Are you sure you want to start a new chat? Your current session will be cleared.")) return;
  try {
    await startNewSession();
  } catch (err) {
    console.error("Error:", err);
    appendMessage("assistant", "Error: Could not start a new session. Please try again.", false);
  }
});

printBtn.addEventListener("click", function () {
  window.print();
});