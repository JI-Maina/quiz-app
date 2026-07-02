"""
TEACHER ANSWER KEY — full working API implementations.
Copy each function body into app.py when students are stuck or for demo.
"""

from datetime import datetime

from flask import jsonify, request

from data.store import QUESTIONS, RESULTS, next_question_id, next_result_id


def fetch_questions():
    quiz_list = []
    for q in QUESTIONS:
        quiz_list.append({
            "id": q["id"],
            "question": q["question"],
            "options": q["options"],
        })
    return jsonify({"count": len(quiz_list), "questions": quiz_list})


def create_question():
    data = request.get_json()
    if not data or "question" not in data:
        return jsonify({"error": "Missing question"}), 400
    if "options" not in data or "answer" not in data:
        return jsonify({"error": "Missing options or answer"}), 400
    if not isinstance(data["options"], list) or len(data["options"]) < 2:
        return jsonify({"error": "Need at least 2 options"}), 400

    new_q = {
        "id": next_question_id(),
        "question": data["question"],
        "options": data["options"],
        "answer": data["answer"],
        "fun_fact": data.get("fun_fact", ""),
    }
    QUESTIONS.append(new_q)
    return jsonify({
        "success": True,
        "id": new_q["id"],
        "message": "Question created!",
    }), 201


def submit_quiz():
    data = request.get_json()
    if not data or "answers" not in data:
        return jsonify({"error": "Missing answers"}), 400

    player_name = data.get("player_name", "Player")
    answers = data["answers"]
    details = []
    score = 0

    for q in QUESTIONS:
        student_ans = answers.get(str(q["id"]), "").strip()
        is_correct = student_ans.lower() == q["answer"].strip().lower()
        if is_correct:
            score += 1
        details.append({
            "question_id": q["id"],
            "correct": is_correct,
            "your_answer": student_ans,
            "correct_answer": q["answer"],
        })

    total = len(QUESTIONS)
    percentage = round((score / total) * 100) if total > 0 else 0

    result = {
        "id": next_result_id(),
        "player_name": player_name,
        "score": score,
        "total": total,
        "percentage": percentage,
        "details": details,
        "timestamp": datetime.now().isoformat(),
    }
    RESULTS.append(result)

    return jsonify({
        "id": result["id"],
        "player_name": player_name,
        "score": score,
        "total": total,
        "percentage": percentage,
        "details": details,
        "message": "Correct! Goal!" if score == total else "Quiz complete!",
    })


def get_all_results():
    return jsonify({
        "count": len(RESULTS),
        "results": list(reversed(RESULTS)),
    })


def get_one_result(result_id):
    for r in RESULTS:
        if r["id"] == result_id:
            return jsonify(r)
    return jsonify({"error": "Result not found"}), 404
