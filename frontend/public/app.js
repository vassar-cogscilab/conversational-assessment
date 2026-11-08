const local = /*"api"*/ "http://127.0.0.1:3001"
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

let sessionId = localStorage.getItem("session_id") || null;

infoBox.textContent = "Session ID: " + sessionId;

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

  const history = JSON.parse(localStorage.getItem("chat_display") || "[]");
  history.push({ role, content });
  localStorage.setItem("chat_display", JSON.stringify(history));
}

async function startNewSession() {
  const res = await fetch(`${local}/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ session_id: null, input: null }),
  });
  const data = await res.json();
  sessionId = data.session_id;
  localStorage.setItem("session_id", sessionId);
  localStorage.removeItem("chat_display");
  chatEl.innerHTML = "";
  appendMessage("assistant", data.server_message);
  sessionId = localStorage.getItem("session_id") || null;
}

window.onload = async function () {
  const stored = localStorage.getItem("chat_display");
  localStorage.setItem("seen_instructions", "false");
  showInitialView();
  if (stored && sessionId) {
    JSON.parse(stored).forEach(msg => {
        chatEl.scrollTo({ top: chatEl.scrollHeight, behavior: "smooth" });

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
    const res = await fetch(`${local}/chat`, {
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