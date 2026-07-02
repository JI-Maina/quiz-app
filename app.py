"""
World Cup 2026 Quiz App — Flask backend + HTML frontend

PAGE ROUTES (already working):
  GET  /          → Home
  GET  /create    → Create questions page
  GET  /play      → Play quiz page
  GET  /results   → Results page

API ROUTES (students complete the TODO sections):
  GET  /api/questions       → Fetch all questions (no answers)
  POST /api/questions       → Create a new question
  POST /api/play/submit     → Submit answers, get score
  GET  /api/results         → Fetch all past results
  GET  /api/results/<id>    → Fetch one result by id
"""

from datetime import datetime
from flask import Flask, jsonify, render_template, request
from data.store import QUESTIONS, RESULTS, next_question_id, next_result_id

app = Flask(__name__)


# ---------------------------------------------------------------------------
# PAGE ROUTES — serve the frontend (already done)
# ---------------------------------------------------------------------------


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create")
def create_page():
    return render_template("create.html")


@app.route("/play")
def play_page():
    return render_template("play.html")


@app.route("/results")
def results_page():
    return render_template("results.html")


# ---------------------------------------------------------------------------
# API: FETCH QUESTIONS
# GET /api/questions
# ---------------------------------------------------------------------------


@app.route("/api/questions", methods=["GET"])
def fetch_questions():
    """
    TODO — Students implement this:

    1. Loop through QUESTIONS from data.store
    2. For each question, return id, question, and options ONLY
       (do NOT send "answer" — players must not see it!)
    3. Return JSON like:
       {
         "count": 3,
         "questions": [
           {"id": 1, "question": "...", "options": ["A", "B", "C"]},
           ...
         ]
       }


    Hint:
       quiz_list = []
       for q in QUESTIONS:
           quiz_list.append({
               "id": q["id"],
               "question": q["question"],
               "options": q["options"],
           })
       return jsonify({"count": len(quiz_list), "questions": quiz_list})
    """
    return (
        jsonify(
            {
                "error": "Not implemented yet",
                "hint": "Complete fetch_questions() in app.py",
            }
        ),
        501,
    )


# ---------------------------------------------------------------------------
# API: CREATE QUESTION
# POST /api/questions
# Body JSON: {"question": "...", "options": ["A","B","C"], "answer": "A", "fun_fact": "..."}
# ---------------------------------------------------------------------------


@app.route("/api/questions", methods=["POST"])
def create_question():
    """
    TODO — Students implement this:

    1. Read JSON from the request: data = request.get_json()
    2. Check required fields: question, options (list), answer
    3. Build a new question dict with id from next_question_id()
    4. Append to QUESTIONS list
    5. Return success JSON with the new id

    Hint:
       data = request.get_json()
       if not data or "question" not in data:
           return jsonify({"error": "Missing question"}), 400


       new_q = {
           "id": next_question_id(),
           "question": data["question"],
           "options": data["options"],
           "answer": data["answer"],
           "fun_fact": data.get("fun_fact", ""),
       }
       QUESTIONS.append(new_q)
       return jsonify({"success": True, "id": new_q["id"], "message": "Question created!"}), 201
    """
    return (
        jsonify(
            {
                "error": "Not implemented yet",
                "hint": "Complete create_question() in app.py",
            }
        ),
        501,
    )


# ---------------------------------------------------------------------------
# API: SUBMIT QUIZ
# POST /api/play/submit
# Body JSON: {"player_name": "Amina", "answers": {"1": "option A", "2": "option B"}}
# ---------------------------------------------------------------------------


@app.route("/api/play/submit", methods=["POST"])
def submit_quiz():
    """
    TODO — Students implement this:

    1. Read JSON: player_name and answers (dict of question_id → chosen answer)
    2. For each question in QUESTIONS, check if answers[str(q["id"])] matches q["answer"]
       (use .lower() on both sides to ignore capital letters)
    3. Count correct answers
    4. Build a details list: [{question_id, correct, your_answer, correct_answer}, ...]
    5. Save result to RESULTS using next_result_id()
    6. Return score, total, percentage, details, and result id


    Hint for checking:
       student_ans = answers.get(str(q["id"]), "")
       is_correct = student_ans.strip().lower() == q["answer"].strip().lower()
    """
    return (
        jsonify(
            {
                "error": "Not implemented yet",
                "hint": "Complete submit_quiz() in app.py",
            }
        ),
        501,
    )


# ---------------------------------------------------------------------------
# API: GET ALL RESULTS
# GET /api/results
# ---------------------------------------------------------------------------


@app.route("/api/results", methods=["GET"])
def get_all_results():
    """
    TODO — Students implement this:

    1. Return all items in RESULTS (newest first is nicer)
    2. JSON shape:
       {"count": 2, "results": [...]}


    Hint:
       return jsonify({"count": len(RESULTS), "results": list(reversed(RESULTS))})
    """
    return (
        jsonify(
            {
                "error": "Not implemented yet",
                "hint": "Complete get_all_results() in app.py",
            }
        ),
        501,
    )


# ---------------------------------------------------------------------------
# API: GET ONE RESULT
# GET /api/results/<id>
# ---------------------------------------------------------------------------


@app.route("/api/results/<int:result_id>", methods=["GET"])
def get_one_result(result_id):
    """
    TODO — Students implement this:

    1. Find the result in RESULTS where r["id"] == result_id
    2. If not found, return 404
    3. If found, return that result as JSON


    Hint:
       for r in RESULTS:
           if r["id"] == result_id:
               return jsonify(r)
       return jsonify({"error": "Result not found"}), 404
    """
    return (
        jsonify(
            {
                "error": "Not implemented yet",
                "hint": "Complete get_one_result() in app.py",
            }
        ),
        501,
    )


# ---------------------------------------------------------------------------
# Run the app
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 55)
    print("  World Cup 2026 Quiz App")
    print("  Open: http://127.0.0.1:5000")
    print("=" * 55)
    app.run(debug=True)
