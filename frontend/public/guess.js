const INITIAL_MESSAGE = "Everyone thinks of the mean as the central tendency or average, but explain what it is for the mean to be a model?";
const local = "http://127.0.0.1:3001" /*"api"*/;

const chatEl = document.getElementById("chat");
const chatForm = document.getElementById("form");
const inputField = document.getElementById("input");
const submitBtn = document.getElementById("submit-btn");
const clearBtn = document.getElementById("clear-btn");
const poorBtn = document.getElementById("guess-poor-btn");
const highBtn = document.getElementById("guess-high-btn");

let sessionId = localStorage.getItem("guess_session_id") || null;

function appendMessage(role, content) {
  const div = document.createElement("div");
  div.className = "message " + role;
  div.textContent = content;
  chatEl.appendChild(div);
  chatEl.scrollTo({ top: chatEl.scrollHeight, behavior: "smooth" });

  const history = JSON.parse(localStorage.getItem("guess_chat_display") || "[]");
  history.push({ role, content });
  localStorage.setItem("guess_chat_display", JSON.stringify(history));
}

function setGuessingEnabled(enabled) {
  poorBtn.disabled = !enabled;
  highBtn.disabled = !enabled;
  submitBtn.disabled = !enabled;
  inputField.disabled = !enabled;
}

async function startNewGame() {
  setGuessingEnabled(false);
  const res = await fetch(`${local}/guess/new_chat`, { method: "POST" });
  const data = await res.json();
  sessionId = data.session_id;
  localStorage.setItem("guess_session_id", sessionId);
  localStorage.removeItem("guess_chat_display");
  chatEl.innerHTML = "";
  appendMessage("user", INITIAL_MESSAGE);
  appendMessage("assistant", data.student_reply);
  setGuessingEnabled(true);
}

window.onload = async function () {
  const stored = localStorage.getItem("guess_chat_display");
  if (stored && sessionId) {
    JSON.parse(stored).forEach(msg => {
      const div = document.createElement("div");
      div.className = "message " + msg.role;
      div.textContent = msg.content;
      chatEl.appendChild(div);
    });
    chatEl.scrollTo({ top: chatEl.scrollHeight, behavior: "smooth" });
    setGuessingEnabled(true);
  } else {
    await startNewGame();
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
  setGuessingEnabled(false);

  const typingEl = document.createElement("div");
  typingEl.className = "typing-indicator";
  typingEl.innerHTML = "<span></span><span></span><span></span>";
  chatEl.appendChild(typingEl);
  chatEl.scrollTo({ top: chatEl.scrollHeight, behavior: "smooth" });

  try {
    const res = await fetch(`${local}/guess/message`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ session_id: sessionId, input: userInputValue }),
    });

    typingEl.remove();

    if (res.status === 404) {
      await startNewGame();
      return;
    }

    if (!res.ok) {
      const errData = await res.json().catch(() => ({}));
      if (errData.error === "turn_limit_reached") {
        appendMessage("assistant", "The student is done answering questions — time to lock in your guess.");
        return;
      }
      if (errData.error === "already_guessed") {
        appendMessage("assistant", "You already locked in a guess for this student — start a New Student to play again.");
        return;
      }
      throw new Error("Server returned an error");
    }

    const data = await res.json();
    appendMessage("assistant", data.student_reply || "No response from the student.");
  } catch (err) {
    typingEl.remove();
    console.error("Error:", err);
    appendMessage("assistant", "Error: Could not reach the backend AI server.");
  } finally {
    setGuessingEnabled(true);
    inputField.focus();
  }
});

async function submitGuess(guess) {
  if (!sessionId) return;
  setGuessingEnabled(false);
  try {
    await fetch(`${local}/guess/reveal`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ session_id: sessionId, guess }),
    });
  } catch (err) {
    console.error("Error submitting guess:", err);
  }
  window.location.href = "guess-reveal.html";
}

poorBtn.addEventListener("click", () => submitGuess("Poor"));
highBtn.addEventListener("click", () => submitGuess("High"));

clearBtn.addEventListener("click", async function () {
  if (!confirm("Start over with a new student? Your current conversation will be cleared.")) return;
  await startNewGame();
});
