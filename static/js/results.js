/**
 * Results page — shows last score from sessionStorage + loads GET /api/results
 */

const latestHero = document.getElementById("latest-result");
const latestScore = document.getElementById("latest-score");
const latestName = document.getElementById("latest-name");
const loadingEl = document.getElementById("results-loading");
const errorEl = document.getElementById("results-error");
const emptyEl = document.getElementById("results-empty");
const listSection = document.getElementById("results-list-section");
const listEl = document.getElementById("results-list");
const detailsSection = document.getElementById("details-section");
const detailsEl = document.getElementById("details-list");

function showLastResultFromSession() {
  const raw = sessionStorage.getItem("lastQuizResult");
  if (!raw) return;

  try {
    const data = JSON.parse(raw);
    latestHero.hidden = false;
    latestScore.textContent = data.score + " / " + data.total;
    latestName.textContent = (data.player_name || "Player") + " — " + (data.percentage || 0) + "%";

    if (data.details && data.details.length > 0) {
      detailsSection.hidden = false;
      detailsEl.innerHTML = "";

      data.details.forEach(function (item) {
        const card = document.createElement("div");
        card.className =
          "detail-card " + (item.correct ? "detail-card--correct" : "detail-card--wrong");
        card.innerHTML =
          "<strong>Question " +
          item.question_id +
          (item.correct ? " ✓" : " ✗") +
          "</strong>" +
          "Your answer: " +
          escapeHtml(item.your_answer || "—") +
          "<br>Correct: " +
          escapeHtml(item.correct_answer || "—");
        detailsEl.appendChild(card);
      });
    }
  } catch (e) {
    /* ignore bad session data */
  }
}

function escapeHtml(text) {
  const div = document.createElement("div");
  div.textContent = text;
  return div.innerHTML;
}

async function loadAllResults() {
  try {
    const response = await fetch("/api/results");
    const data = await response.json();

    loadingEl.hidden = true;

    if (response.status === 501) {
      errorEl.hidden = false;
      errorEl.textContent =
        "Results API not ready. Complete get_all_results() in app.py — then refresh.";
      errorEl.className = "message-box message-box--info";
      return;
    }

    if (!response.ok) {
      errorEl.hidden = false;
      errorEl.textContent = data.error || "Failed to load results.";
      errorEl.className = "message-box message-box--error";
      return;
    }

    const results = data.results || [];

    if (results.length === 0) {
      emptyEl.hidden = false;
      return;
    }

    listSection.hidden = false;
    listEl.innerHTML = "";

    results.forEach(function (r) {
      const row = document.createElement("div");
      row.className = "result-row";
      row.innerHTML =
        '<span class="result-row-name">' +
        escapeHtml(r.player_name || "Player") +
        "</span>" +
        '<span class="result-row-score">' +
        r.score +
        " / " +
        r.total +
        " (" +
        (r.percentage || 0) +
        "%)</span>";
      listEl.appendChild(row);
    });
  } catch (err) {
    loadingEl.hidden = true;
    errorEl.hidden = false;
    errorEl.textContent = "Could not reach the server. Is python app.py running?";
    errorEl.className = "message-box message-box--error";
  }
}

showLastResultFromSession();
loadAllResults();
