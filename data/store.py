"""
In-memory storage for the quiz app.
Students use these lists in their API endpoint code.
"""

# Each question: {"id", "question", "options", "answer", "fun_fact" (optional)}
QUESTIONS = []

# Each result: {"id", "player_name", "score", "total", "percentage", "details", "timestamp"}
RESULTS = []

# Helper: call this when you need the next question id
def next_question_id():
    if not QUESTIONS:
        return 1
    return max(q["id"] for q in QUESTIONS) + 1


def next_result_id():
    if not RESULTS:
        return 1
    return max(r["id"] for r in RESULTS) + 1
