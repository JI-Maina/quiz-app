/**
 * Create page — sends new questions to POST /api/questions
 */

const form = document.getElementById("create-form");
const messageBox = document.getElementById("create-message");

function showMessage(text, type) {
  messageBox.hidden = false;
  messageBox.textContent = text;
  messageBox.className = "message-box message-box--" + type;
}

form.addEventListener("submit", async function (event) {
  event.preventDefault();

  const payload = {
    question: document.getElementById("question").value.trim(),
    options: [
      document.getElementById("option-a").value.trim(),
      document.getElementById("option-b").value.trim(),
      document.getElementById("option-c").value.trim(),
    ],
    answer: document.getElementById("answer").value.trim(),
    fun_fact: document.getElementById("fun-fact").value.trim(),
  };

  try {
    const response = await fetch("/api/questions", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    const data = await response.json();

    if (response.ok) {
      showMessage("Question saved! ID: " + data.id + " — " + (data.message || "Success"), "success");
      form.reset();
    } else if (response.status === 501) {
      showMessage(
        "API not ready yet. Complete create_question() in app.py — then try again!",
        "info"
      );
    } else {
      showMessage(data.error || "Something went wrong.", "error");
    }
  } catch (err) {
    showMessage("Could not reach the server. Is python app.py running?", "error");
  }
});
