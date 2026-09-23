const INITIAL_MESSAGE = "Everyone thinks of the mean as the central tendency or average, but why do you think we use it to represent a bunch of data?";
const local = /*"http://127.0.0.1:3001"*/ "api"

const chatEl = document.getElementById("chat");
const chatForm = document.querySelector(".input");
const inputField = document.getElementById("input");
const submitBtn = document.getElementById("submit-btn");
const clearBtn = document.getElementById("clear-btn");
const printBtn = document.querySelector(".print-btn");

const revealBox = document.querySelector('.reveal');
const testBox = document.querySelector('.test');
const continueBtn = document.querySelector('.instructions .continue-btn');
const instructionBox = document.querySelector('.instructions');

let sessionId = localStorage.getItem("session_id") || null;

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

function appendMessage(role, content) {
  const div = document.createElement("div");
  div.className = "message " + role;
  div.textContent = content;
  chatEl.appendChild(div);
  chatEl.scrollTo({ top: chatEl.scrollHeight, behavior: "smooth" });

  const history = JSON.parse(localStorage.getItem("chat_display") || "[]");
  history.push({ role, content });
  localStorage.setItem("chat_display", JSON.stringify(history));
}

async function startNewSession() {
  const res = await fetch(`${local}/new_chat`, { method: "POST" });
  const data = await res.json();
  sessionId = data.session_id;
  localStorage.setItem("session_id", sessionId);
  localStorage.removeItem("chat_display");
  chatEl.innerHTML = "";
  appendMessage("assistant", INITIAL_MESSAGE);
}

window.onload = async function () {
  const stored = localStorage.getItem("chat_display");
  localStorage.setItem("seen_instructions", "false");
  showInitialView();
  if (stored && sessionId) {
    JSON.parse(stored).forEach(msg => {
      const div = document.createElement("div");
      div.className = "message " + msg.role;
      div.textContent = msg.content;
      chatEl.appendChild(div);
    });
    chatEl.scrollTo({ top: chatEl.scrollHeight, behavior: "smooth" });
  } else {
    await startNewSession();
  }
};

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

  appendMessage("user", userInputValue);
  inputField.value = "";
  submitBtn.disabled = true;

  const typingEl = document.createElement("div");
  typingEl.className = "typing-indicator";
  typingEl.innerHTML = "<span></span><span></span><span></span>";
  chatEl.appendChild(typingEl);
  chatEl.scrollTo({ top: chatEl.scrollHeight, behavior: "smooth" });

  try {
    const res = await fetch(`${local}/string`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ session_id: sessionId, input: userInputValue }),
    });

    typingEl.remove();

    if (res.status === 404) {
      await startNewSession();
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
  await startNewSession();
});

printBtn.addEventListener("click", function () {
  window.print();
});

async function loadSummary() {
  if (!sessionId) return;
  try {
    const res = await fetch(`${local}/summary?session_id=${sessionId}`);
    if (!res.ok) return;
    const data = await res.json();
    if (data.evaluation_summary) {
      revealBox.textContent = data.evaluation_summary;
      revealBox.classList.remove("placeholder");
    }
  } catch (err) {
    revealBox.textContent = "Could not load summary — backend unavailable.";
  }
}

