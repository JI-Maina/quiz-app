# World Cup 2026 Quiz App

A full-stack quiz project for junior school students. The **frontend is complete** (HTML, CSS, JavaScript). Your job is to finish the **Flask API** in `app.py`.

**Theme:** FIFA World Cup 2026 — USA, Canada, Mexico  
**Stack:** Flask (backend) + HTML + CSS + JavaScript (frontend)

---

## What you are building

```
Browser (HTML pages)  →  calls API  →  Flask (app.py)  →  data/store.py
```

| Page | URL | What it does |
| ---- | --- | ------------ |
| Home | http://127.0.0.1:5000/ | Explains the project flow |
| Create | http://127.0.0.1:5000/create | Form to add quiz questions |
| Play | http://127.0.0.1:5000/play | Load questions and answer them |
| Results | http://127.0.0.1:5000/results | See your score and leaderboard |

The pages already work. They call the API — **you write the API code**.

---

## Setup (Windows)

### 1. Open terminal in the project folder

Command Prompt or PowerShell:

```cmd
cd path\to\quiz_app
```

### 2. Create a virtual environment (first time only)

```cmd
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

**PowerShell:** if activation fails, use `.venv\Scripts\Activate.ps1` or switch to Command Prompt.

**Skip venv?** Run `pip install flask` if Flask is already available.

### 3. Start the server

```cmd
python app.py
```

You should see:

```
World Cup 2026 Quiz App
Open: http://127.0.0.1:5000
```

### 4. Open in browser

Go to: **http://127.0.0.1:5000**

**Stop the server:** press `Ctrl + C` in the terminal.

**After editing `app.py`:** stop and run `python app.py` again.

---

## Project structure

```
quiz_app/
├── app.py              ← YOU EDIT THIS (API endpoints)
├── app_solutions.py    ← Teacher answer key (do not copy unless stuck!)
├── requirements.txt
├── README.md
├── data/
│   └── store.py        ← QUESTIONS and RESULTS lists (in memory)
├── templates/          ← HTML pages (done)
│   ├── base.html
│   ├── index.html
│   ├── create.html
│   ├── play.html
│   └── results.html
└── static/
    ├── css/style.css   ← Styles (done)
    └── js/
        ├── create.js   ← Calls POST /api/questions
        ├── play.js     ← Calls GET /api/questions and POST /api/play/submit
        └── results.js  ← Calls GET /api/results
```

---

## Your tasks — complete the API in this order

Open `app.py`. Each function has a **TODO** block and hints. Replace the `return ... 501` stub with your real code.

### Task 1: Create questions — `POST /api/questions`

**Function:** `create_question()`

**What it should do:**

1. Read JSON from the request: `data = request.get_json()`
2. Check that `question`, `options`, and `answer` are present
3. Create a new question with `id` from `next_question_id()`
4. Append it to the `QUESTIONS` list (from `data.store`)
5. Return success JSON with the new id

**Test:** Go to **Create** page, fill the form, click Save. You should see "Question saved!"

---

### Task 2: Fetch questions — `GET /api/questions`

**Function:** `fetch_questions()`

**What it should do:**

1. Loop through `QUESTIONS`
2. Return `id`, `question`, and `options` only — **do not send `answer`**
3. Return JSON: `{"count": N, "questions": [...]}`

**Test:** Go to **Play** page. Questions should load (after you created some in Task 1).

---

### Task 3: Submit answers — `POST /api/play/submit`

**Function:** `submit_quiz()`

**What it should do:**

1. Read JSON: `player_name` and `answers` (dict like `{"1": "option A", "2": "option B"}`)
2. For each question in `QUESTIONS`, check if the student's answer matches (use `.lower()`)
3. Count correct answers and build a `details` list
4. Save the result to `RESULTS` using `next_result_id()`
5. Return `score`, `total`, `percentage`, and `details`

**Test:** Play the quiz, submit your name and answers. You should be redirected to **Results**.

---

### Task 4: Get all results — `GET /api/results`

**Function:** `get_all_results()`

**What it should do:**

1. Return all items in `RESULTS` (newest first is best)
2. Return JSON: `{"count": N, "results": [...]}`

**Test:** Go to **Results** page. Leaderboard should show past scores.

---

### Task 5 (optional): Get one result — `GET /api/results/<id>`

**Function:** `get_one_result(result_id)`

**What it should do:**

1. Find the result where `r["id"] == result_id`
2. Return it as JSON, or 404 if not found

---

## API reference

### `POST /api/questions` — create question

**Request body:**

```json
{
  "question": "Which three countries host World Cup 2026?",
  "options": ["USA, Canada, Mexico", "Brazil, Argentina, Chile", "England, France, Germany"],
  "answer": "USA, Canada, Mexico",
  "fun_fact": "First time three countries host together!"
}
```

**Success response (201):**

```json
{
  "success": true,
  "id": 1,
  "message": "Question created!"
}
```

---

### `GET /api/questions` — fetch questions (no answers)

**Success response (200):**

```json
{
  "count": 2,
  "questions": [
    {
      "id": 1,
      "question": "Which three countries host World Cup 2026?",
      "options": ["USA, Canada, Mexico", "Brazil, Argentina, Chile", "England, France, Germany"]
    }
  ]
}
```

---

### `POST /api/play/submit` — submit quiz

**Request body:**

```json
{
  "player_name": "Amina",
  "answers": {
    "1": "USA, Canada, Mexico",
    "2": "48 teams"
  }
}
```

**Success response (200):**

```json
{
  "id": 1,
  "player_name": "Amina",
  "score": 2,
  "total": 2,
  "percentage": 100,
  "details": [
    {
      "question_id": 1,
      "correct": true,
      "your_answer": "USA, Canada, Mexico",
      "correct_answer": "USA, Canada, Mexico"
    }
  ],
  "message": "Correct! Goal!"
}
```

---

### `GET /api/results` — all results

**Success response (200):**

```json
{
  "count": 1,
  "results": [
    {
      "id": 1,
      "player_name": "Amina",
      "score": 2,
      "total": 2,
      "percentage": 100,
      "details": [...],
      "timestamp": "2026-06-18T10:30:00"
    }
  ]
}
```

---

## Full test flow

1. Start server: `python app.py`
2. Open http://127.0.0.1:5000/create
3. Add 2–3 World Cup questions
4. Open http://127.0.0.1:5000/play
5. Enter your name, answer all questions, click **Submit Answers**
6. Check http://127.0.0.1:5000/results for your score and leaderboard

---

## Troubleshooting

| Problem | Fix |
| -------- | --- |
| `'python' is not recognized` | Install Python from [python.org](https://www.python.org/) and tick **Add Python to PATH** |
| `ModuleNotFoundError: flask` | Run `pip install flask` or `pip install -r requirements.txt` |
| `API not ready yet` on page | That endpoint is still a stub — complete the TODO in `app.py` |
| Browser: connection refused | Run `python app.py` first |
| Changes not showing | Stop server (`Ctrl + C`), run `python app.py` again |
| Create works but Play is empty | Create at least one question first on the Create page |
| Wrong answer always marked wrong | Answer must match an option exactly (capital letters are ignored) |
| Windows Firewall popup | Click **Allow access** |

---

## For teachers

- **`app_solutions.py`** contains full working implementations for every endpoint.
- Students should try the TODOs first; use solutions only for demo or if stuck.
- Data is stored **in memory** — restarting the server clears questions and results.
- Suggested lesson order: Task 1 → 2 → 3 → 4, testing in the browser after each one.

---

## Sample World Cup questions to add

- Which three countries are hosting FIFA World Cup 2026? → **USA, Canada, Mexico**
- How many teams play at World Cup 2026? → **48 teams**
- Which continent hosts World Cup 2026? → **North America**
- What sport is the FIFA World Cup about? → **Football (soccer)**

---

**Good luck — shout GOAL! when your API works!**
