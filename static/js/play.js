/**
 * Play page — loads GET /api/questions, submits POST /api/play/submit
 */

const loadingEl = document.getElementById("play-loading");
const errorEl = document.getElementById("play-error");
const emptyEl = document.getElementById("play-empty");
const formEl = document.getElementById("play-form");
const containerEl = document.getElementById("questions-container");
const submitMsgEl = document.getElementById("submit-message");

let loadedQuestions = [];

function showError(text) {
  errorEl.hidden = false;
  errorEl.textContent = text;
  errorEl.className = "message-box message-box--error";
}

function renderQuestions(questions) {
  containerEl.innerHTML = "";

  questions.forEach(function (q, index) {
    const card = document.createElement("div");
    card.className = "question-card";
    card.innerHTML = "<h3>Q" + (index + 1) + ". " + escapeHtml(q.question) + "</h3>";

    q.options.forEach(function (option) {
      const label = document.createElement("label");
      label.className = "option-label";

      const radio = document.createElement("input");
      radio.type = "radio";
      radio.name = "q-" + q.id;
      radio.value = option;
      radio.required = true;

      label.appendChild(radio);
      label.appendChild(document.createTextNode(" " + option));
      card.appendChild(label);
    });

    containerEl.appendChild(card);
  });
}

function escapeHtml(text) {
  const div = document.createElement("div");
  div.textContent = text;
  return div.innerHTML;
}

async function loadQuestions() {
  try {
    const response = await fetch("/api/questions");
    const data = await response.json();

    loadingEl.hidden = true;

    if (response.status === 501) {
      showError(
        "Fetch API not ready. Complete fetch_questions() in app.py, then refresh this page."
      );
      return;
    }

    if (!response.ok) {
      showError(data.error || "Failed to load questions.");
      return;
    }

    loadedQuestions = data.questions || [];

    if (loadedQuestions.length === 0) {
      emptyEl.hidden = false;
      return;
    }

    renderQuestions(loadedQuestions);
    formEl.hidden = false;
  } catch (err) {
    loadingEl.hidden = true;
    showError("Could not reach the server. Is python app.py running?");
  }
}

formEl.addEventListener("submit", async function (event) {
  event.preventDefault();

  const playerName = document.getElementById("player-name").value.trim();
  const answers = {};

  loadedQuestions.forEach(function (q) {
    const selected = document.querySelector('input[name="q-' + q.id + '"]:checked');
    if (selected) {
      answers[String(q.id)] = selected.value;
    }
  });

  const payload = {
    player_name: playerName,
    answers: answers,
  };

  submitMsgEl.hidden = false;
  submitMsgEl.textContent = "Submitting...";
  submitMsgEl.className = "status-box";

  try {
    const response = await fetch("/api/play/submit", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    const data = await response.json();

    if (response.ok) {
      sessionStorage.setItem("lastQuizResult", JSON.stringify(data));
      window.location.href = "/results";
    } else if (response.status === 501) {
      submitMsgEl.className = "message-box message-box--info";
      submitMsgEl.textContent =
        "Submit API not ready. Complete submit_quiz() in app.py — then try again!";
    } else {
      submitMsgEl.className = "message-box message-box--error";
      submitMsgEl.textContent = data.error || "Submit failed.";
    }
  } catch (err) {
    submitMsgEl.className = "message-box message-box--error";
    submitMsgEl.textContent = "Could not reach the server.";
  }
});

loadQuestions();
