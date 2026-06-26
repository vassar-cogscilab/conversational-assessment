const INITIAL_MESSAGE = "Everyone thinks of the mean as the central tendency or average, but explain what it is for the mean to be a model?";

const USER_INSTRUCTION = "Silently assess the student's understanding according to the workflow. If the student has shown strong understanding of at least 3 different topics, provide the final assessment summary. Otherwise, respond naturally in 15 to 50 words and ask only one adaptive follow-up question. Do not show internal assessments, round numbers, workflow details, or labels.";
const WRAP_UP = "Begin finishing this conversation";

const chatEl = document.getElementById("chat");
const chatForm = document.getElementById("form");
const inputField = document.getElementById("input");
const submitBtn = document.getElementById("submit-btn");
const clearBtn = document.getElementById("clear-btn");

let currentTurns = 0;
let localHistory = [];

function appendMessage(role, content) {
  const div = document.createElement("div");
  div.className = "message " + role;
  div.textContent = content;
  chatEl.appendChild(div);
  chatEl.scrollTo({ top: chatEl.scrollHeight, behavior: "smooth" });
  localHistory.push({ role, content });
  localStorage.setItem("chat_history", JSON.stringify(localHistory));
}

window.onload = function () {
  const stored = localStorage.getItem("chat_history");
  if (stored) {
    localHistory = JSON.parse(stored);
    const snapshot = [...localHistory];
    localHistory = [];
    chatEl.innerHTML = "";
    snapshot.forEach(msg => appendMessage(msg.role, msg.content));
  } else {
    appendMessage("assistant", INITIAL_MESSAGE);
  }
};

inputField.addEventListener("keydown", function (e) {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    submitBtn.click();
  }
});

function clearChatHistory() {
  localStorage.removeItem("chat_history");
  localHistory = [];
  chatEl.innerHTML = "";
}

chatForm.addEventListener("submit", function (e) {
  e.preventDefault();

  const userInputValue = inputField.value;
  if (!userInputValue) return;

  appendMessage("user", userInputValue);

  const fullHistory = [...localHistory];
  const lastIndex = fullHistory.length - 1;

  if (currentTurns <= 7) {
    fullHistory[lastIndex] = { role: "user", content: userInputValue + "\n" + USER_INSTRUCTION };
  }
  if (currentTurns > 7) {
    fullHistory[lastIndex] = { role: "user", content: userInputValue + "\n" + USER_INSTRUCTION + "\n" + WRAP_UP };
  }
  if (currentTurns === 9) {
    fullHistory[lastIndex] = { role: "user", content: userInputValue + "\n" + "respond to the user but then YOU MUST say goodbye" };
  }

  inputField.value = "";
  submitBtn.disabled = true;

  const dataToSend = {
    input: userInputValue,
    readMessages: localHistory,
    messages: fullHistory,
    turns: currentTurns,
  };

  fetch("http://127.0.0.1:3001/string", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(dataToSend),
  })
    .then(res => {
      if (!res.ok) throw new Error("Server returned an error");
      return res.json();
    })
    .then(data => {
      const aiResponse = data.server_message || data.response || "No response field found in server data.";
      appendMessage("assistant", aiResponse);
    })
    .catch(err => {
      console.error("Error:", err);
      appendMessage("assistant", `Error: Could not reach the backend AI server. Turn: ${currentTurns}`);
    })
    .finally(() => {
      submitBtn.disabled = false;
      inputField.focus();
    });

  currentTurns++;
});

clearBtn.addEventListener("click", function () {
  if (!confirm("Are you sure you want to start a new chat? Your current session will be cleared.")) return;
  clearChatHistory();
  appendMessage("assistant", INITIAL_MESSAGE);
  currentTurns = 0;
});
