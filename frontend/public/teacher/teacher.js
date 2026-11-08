// Local dev talks to Flask directly; on the server, "api" resolves relative to
// the page (/convo/api/...) and the reverse proxy forwards it to Flask.
const local = ["127.0.0.1", "localhost"].includes(location.hostname)
  ? "http://127.0.0.1:3001"
  : "api";
 
// ---------- Elements ----------
const chatEl = document.querySelector(".conversation");
const classEL = document.querySelector(".conversations");
const ratingForm = document.getElementById("rating-form");
const ratingStatus = document.getElementById("rating-status");
 
const tabs = document.querySelectorAll(".menu-btn");
const tabContents = document.querySelectorAll(".tab");
 
// ---------- State ----------
let sessionId = safeGet("session_id");
const ratingsInFlight = new Set(); // session ids with a rating request in progress
 
// ---------- Small helpers ----------
function safeGet(key) {
  try { return localStorage.getItem(key); } catch { return null; }
}
function safeSet(key, value) {
  try { localStorage.setItem(key, value); } catch {}
}
 
// Admin token: asked for in the page itself (prompt() is blocked in sandboxed
// iframes), kept in sessionStorage for this tab only, never hardcoded.
let adminToken = null;
try { adminToken = sessionStorage.getItem("admin_token"); } catch {}
 
function askForAdminToken() {
  return new Promise(resolve => {
    const overlay = document.createElement("div");
    overlay.style.cssText =
      "position:fixed;inset:0;background:rgba(0,0,0,.5);display:flex;align-items:center;justify-content:center;z-index:9999";
 
    const form = document.createElement("form");
    form.style.cssText =
      "background:#fff;color:#000;padding:20px;border-radius:8px;display:flex;flex-direction:column;gap:10px;min-width:280px";
 
    const label = document.createElement("label");
    label.textContent = "Admin token";
 
    const input = document.createElement("input");
    input.type = "password";
    input.autocomplete = "off";
 
    const btn = document.createElement("button");
    btn.type = "submit";
    btn.textContent = "Continue";
 
    form.append(label, input, btn);
    overlay.appendChild(form);
    document.body.appendChild(overlay);
    input.focus();
 
    form.addEventListener("submit", e => {
      e.preventDefault();
      const token = input.value.trim();
      if (!token) return;
      overlay.remove();
      resolve(token);
    });
  });
}
 
async function ensureAdminToken() {
  if (!adminToken) {
    adminToken = await askForAdminToken();
    try { sessionStorage.setItem("admin_token", adminToken); } catch {}
  }
  return adminToken;
}
 
// On a 401 the stored token is wrong: clear it, ask again, and retry once.
async function adminFetch(path) {
  let res;
  for (let attempt = 0; attempt < 2; attempt++) {
    const token = await ensureAdminToken();
    res = await fetch(`${local}${path}`, {
      method: "GET",
      headers: { "X-Admin-Token": token },
    });
    if (res.status !== 401) return res;
    adminToken = null;
    try { sessionStorage.removeItem("admin_token"); } catch {}
  }
  return res;
}
 
function getRaterId() {
  let id = safeGet("rater_id");
  if (!id) {
    id = crypto.randomUUID();
    safeSet("rater_id", id);
  }
  return id;
}
 
// ---------- Event listeners (attached first, so nothing below can stop them) ----------
ratingForm?.addEventListener("submit", async e => {
  e.preventDefault(); // always first, so the page can never reload
 
  const id = sessionId;
  if (!id || ratingsInFlight.has(id)) return; // ignores double-clicks and Enter spam
  ratingsInFlight.add(id);
 
  // Read the values BEFORE disabling: disabled fields are excluded from FormData
  const data = new FormData(ratingForm);
  const payload = {
    session_id: id,
    rater_id: getRaterId(),
    understanding_feedback: data.get("understanding-feedback"),
    question_feedback: data.get("question-feedback"),
    question_rating: data.get("question-rating"),
    comment: data.get("comment") || "",
  };
 
  setRatingLocked(true, "Submitting…");
  try {
    const token = await ensureAdminToken();
    const res = await fetch(`${local}/rating`, {
      method: "POST",
      headers: { "Content-Type": "application/json", "X-Admin-Token": token },
      body: JSON.stringify(payload),
    });
 
    // 409 = this rater already submitted for this session, so stay locked
    if (res.ok || res.status === 409) {
      safeSet(ratedKey(id), "1");
      if (sessionId === id) setRatingLocked(true, "Thanks, your response was submitted.");
    } else if (res.status === 401) {
      // Wrong or expired token: forget it so the next attempt asks again
      adminToken = null;
      try { sessionStorage.removeItem("admin_token"); } catch {}
      if (sessionId === id) setRatingLocked(false, "Admin token was rejected. Submit again to re-enter it.");
    } else if (res.status === 400) {
      const body = await res.json().catch(() => ({}));
      console.error("Rating rejected by server:", body, "payload:", payload);
      const messages = {
        invalid_rating: "Please choose a rating from 1 to 7.",
        invalid_feedback: "Please answer both yes/no/not enough evidence questions.",
        comment_too_long: "Your comment is too long (2000 characters max).",
        invalid_rater: "Rater id problem. Clear localStorage and reload.",
      };
      if (sessionId === id) {
        setRatingLocked(false, messages[body.error] || `Rejected by server (${body.error || "unknown"}).`);
      }
    } else {
      throw new Error("Server returned " + res.status);
    }
  } catch (err) {
    console.error(err);
    // Only unlock on failure
    if (sessionId === id) setRatingLocked(false, "Couldn't submit. Please try again.");
  } finally {
    ratingsInFlight.delete(id);
  }
});
 
// ---------- Rating lock ----------
function ratedKey(id) {
  return `rated:${id}`;
}
 
function setRatingLocked(locked, message = "") {
  if (!ratingForm) return;
  ratingForm.querySelectorAll("input, textarea, button").forEach(el => (el.disabled = locked));
  if (ratingStatus) ratingStatus.textContent = message;
}
 
// Call whenever the active session changes
function syncRatingState() {
  if (!ratingForm) return;
  if (!sessionId) {
    setRatingLocked(true, "Select a conversation to rate it.");
  } else if (safeGet(ratedKey(sessionId)) === "1") {
    setRatingLocked(true, "Thanks, your response was submitted.");
  } else if (ratingsInFlight.has(sessionId)) {
    setRatingLocked(true, "Submitting…");
  } else {
    setRatingLocked(false, "");
  }
}
 
// ---------- Tabs ----------
function showTab() {
  if (!tabContents.length) return;
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
 
// ---------- Conversation list ----------
function markActiveConversation() {
  document.querySelectorAll(".conversation-block").forEach(d => {
    d.classList.toggle("active", d.dataset.id === sessionId);
  });
}
 
function appendConversation(content, id) {
  const div = document.createElement("div");
  div.className = "conversation-block";
  div.dataset.id = id;
  div.textContent = content;
  classEL.appendChild(div);
 
  div.addEventListener("click", async () => {
    await loadSession(id);
    location.hash = "#student";
    markActiveConversation();
  });
}
 
// ---------- Messages ----------
function appendMessage(role, content, info) {
  const parent = document.createElement("div");
  parent.className = "message-container";
  chatEl.appendChild(parent);
 
  const div = document.createElement("div");
  div.className = "message " + role + "1";
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
 
async function loadSession(id) {
  sessionId = id;
  safeSet("session_id", id);
 
  try {
    const res = await adminFetch(`/admin/sessions/${encodeURIComponent(id)}`);
    if (!res.ok) {
      console.error("Failed to load session", res.status);
      return;
    }
    const session = await res.json();
    const turnLog = session.turn_log || [];
 
    chatEl.innerHTML = "";
 
    session.messages.forEach((msg, index) => {
      // Fractional indexes (odd/even mismatch) return undefined, which is intended
      const studentTurn = turnLog[(index - 1) / 2];
      const examinerTurn = turnLog[(index - 2) / 2];
 
      if (studentTurn) {
        const info =
          "Belief: " + studentTurn.belief +
          "\n\nRelevant Concepts: " + studentTurn.relevant_concepts +
          "\n\nTarget Misconceptions: " + studentTurn.target_misconceptions;
        appendMessage(msg.role, msg.content, info);
      } else if (examinerTurn) {
        appendMessage(msg.role, msg.content, "Reasoning: " + examinerTurn.reasoning);
      } else {
        appendMessage(msg.role, msg.content, "No Information Yet");
      }
    });
 
    chatEl.scrollTo({ top: chatEl.scrollHeight, behavior: "smooth" });
    ratingForm?.reset();
  } catch (err) {
    console.error("Error loading session:", err);
  } finally {
    syncRatingState();
    markActiveConversation();
  }
}
 
// ---------- Startup ----------
async function init() {
  syncRatingState(); // correct lock state immediately, before any network call
  try {
    const res = await adminFetch("/admin/sessions");
    if (!res.ok) throw new Error("Failed to load sessions: " + res.status);
    const data = await res.json();
 
    data.sessions.forEach(s => {
      appendConversation(
        `Session ID: ${s.session_id}\nCurrent Question: ${s.current_question}\nTurns: ${s.turns}\nCompleted: ${s.has_summary}`,
        s.session_id
      );
    });
 
    if (sessionId) await loadSession(sessionId);
    else markActiveConversation();
  } catch (err) {
    console.error(err);
  }
}
 
init();