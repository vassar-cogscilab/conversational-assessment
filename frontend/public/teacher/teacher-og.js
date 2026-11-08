const INITIAL_MESSAGE = "Everyone thinks of the mean as the central tendency or average, but explain what it is for the mean to be a model?";
const local = /*http://127.0.0.1:3001*/ "api"

const chatEl = document.querySelector(".conversation");
const classEL = document.querySelector(".conversations");
const chatForm = document.querySelectorAll(".form");
const submitBtn = document.querySelector("submit");
const clearBtn = document.getElementById("clear-btn");
const printBtn = document.querySelector(".print-btn");

const revealBox = document.querySelector('.reveal');
const continueBtn = document.querySelector('.instructions .continue-btn');
const instructionBox = document.querySelector('.instructions');

const infoBox = document.querySelector('.info');

const tabs = document.querySelectorAll(".menu-btn");
const tabContents = document.querySelectorAll(".tab");

function showTab() {
  const id = location.hash.slice(1);
  const valid = [...tabContents].some(tc => tc.id === id);
  const active = valid ? id : tabContents[0].id;

  tabContents.forEach(tc => tc.classList.toggle("active", tc.id === active));
  tabs.forEach(btn =>
    btn.classList.toggle("active", btn.dataset.tabTarget === "#" + active)
  );
}

tabs.forEach(btn => {
  btn.addEventListener("click", () => {
    location.hash = btn.dataset.tabTarget;
  });
});

window.addEventListener("hashchange", showTab);
showTab();

function appendConversation(content, id) {
  const div = document.createElement("div");
  div.className = "conversation-block";
  classEL.appendChild(div);
  div.textContent = content;

  div.dataset.id = id;
  div.textContent = content;

  div.addEventListener("click", async () => {
      await loadSession(id);
      location.hash = "#student";
      document.querySelectorAll(".conversation-block").forEach(d => {
        d.classList.toggle("active", d.dataset.id === sessionId);
      });
    }); 
}

function appendMessage(role, content, info) {
  const parent = document.createElement("div");
  parent.className = "message-container";
  chatEl.appendChild(parent);
  chatEl.scrollTo({ top: chatEl.scrollHeight, behavior: "smooth" });

  const div = document.createElement("div");
  div.className = "message " + role +"1";
  div.id = "teacher-message";
  div.textContent = content;
  parent.appendChild(div);

  const wrapper = document.createElement("div");
  wrapper.className = "info-wrapper";
  parent.appendChild(wrapper);
  const div2 = document.createElement("div");
  div2.className = "chat-info";
  div2.textContent = info;
  wrapper.appendChild(div2);

  parent.addEventListener("click", () => {
    div.classList.toggle("expanded");
    wrapper.classList.toggle("expanded");
    parent.classList.toggle("expanded");
  });
}

const ADMIN_TOKEN = "90822e1c670473f0bfe405062128b4f61a41820a196c1d8790923d88675d09ad"; // see security note below

const res = await fetch(`${local}/admin/sessions`, {
  method: "GET",
  headers: { "X-Admin-Token": ADMIN_TOKEN },
});
if (!res.ok) {
  console.error("Failed to load session", res.status);
}
const data = await res.json();
data.sessions.forEach(s => {
  appendConversation(`Session ID: ${s.session_id}\nCurrent Question: ${s.current_question}\nTurns: ${s.turns}\nCompleted: ${s.has_summary}`, s.session_id);
});

let sessionId = localStorage.getItem("session_id") || null;
if (sessionId) await loadSession(sessionId);

async function loadSession(id) {
  sessionId = id;
  try { localStorage.setItem("session_id", id); } catch (e) {}
  const res2 = await fetch(`${local}/admin/sessions/${sessionId}`, {
    method: "GET",
    headers: { "X-Admin-Token": ADMIN_TOKEN },
  });
  if (!res2.ok) {
    console.error("Failed to load session", res2.status);
    return;
  }
  const session = await res2.json();

  chatEl.innerHTML = "";

  session.messages.forEach((msg, index) => {
    const studentTurn = session.turn_log[(index-1)/2];
    const examinerTurn = session.turn_log[(index-2)/2];
    if (studentTurn) {
      const info = 
        "Belief: " + studentTurn.belief + 
        "\n\nRelevant Concepts: " + studentTurn.relevant_concepts + 
        "\n\nTarget Misconceptions: " + studentTurn.target_misconceptions;
      appendMessage(msg.role, msg.content, info);
    }
    else if(examinerTurn) {
      appendMessage(msg.role, msg.content, "Reasoning: " + examinerTurn.reasoning);
    }
    else {
      appendMessage(msg.role, msg.content, "No Information Yet");
    }
  });
}

chatForm.forEach(form => {
  form.addEventListener("submit", e => {
    e.preventDefault();
    console.log("Form submitted smoothly without a page refresh!");
  });
});