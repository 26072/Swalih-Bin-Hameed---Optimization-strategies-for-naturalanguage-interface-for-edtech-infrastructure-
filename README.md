# EduBot — EdTech CLI Chatbot

> **Project:** Optimization Strategies for Natural Language Interface for EdTech Infrastructure  
> **Roll No:** PRJN26-127  
> **Technology:** Python, Basic String Matching  
> **Tool:** VS Code

---

## 📖 Overview

EduBot is a **Command-Line Interface (CLI) Chatbot** built in Python for an EdTech platform. It uses **basic string matching** (exact, phrase, and keyword scanning) to understand student queries and return pre-defined, helpful responses — covering courses, assignments, grades, schedules, and more.

---

## 📁 Project Structure

```
edtech_chatbot/
│
├── chatbot.py          # Main entry point — CLI loop
├── matcher.py          # Matching engine (3-strategy NLP)
├── knowledge_base.py   # All keywords + responses (the "brain")
├── requirements.txt    # Dependencies
├── chat_history.log    # Auto-generated session log
│
├── tests/
│   └── test_chatbot.py # Unit tests (unittest + pytest)
│
└── docs/
    ├── Project_Proposal.md
    ├── HLD.md
    ├── LLD.md
    └── Final_Report.md
```

---

## 🚀 How to Run

### Step 1 — Open VS Code Terminal

```bash
cd edtech_chatbot
```

### Step 2 — Run the Chatbot

```bash
python chatbot.py
```

### Step 3 — Interact!

Type any of these commands when the chatbot starts:

| What You Type            | What It Does                   |
|--------------------------|-------------------------------|
| `hello` / `hi`           | Greeting                       |
| `help`                   | Show all available commands    |
| `show status`            | Platform status dashboard      |
| `list courses`           | Browse available courses       |
| `enroll`                 | How to enroll in a course      |
| `course fee`             | Fee structure                  |
| `assignment status`      | View assignment progress       |
| `submit assignment`      | Submission steps               |
| `grades`                 | View your grades               |
| `progress`               | Course completion progress     |
| `schedule`               | Upcoming class schedule        |
| `faculty`                | Instructor information         |
| `login`                  | Login/password help            |
| `resources`              | Study material links           |
| `quiz`                   | Quiz and assessment info       |
| `contact`                | Contact support                |
| `exit` / `bye`           | Quit the chatbot               |

---

## 🧪 Running Tests

```bash
# Using pytest (recommended)
pip install pytest
pytest tests/test_chatbot.py -v

# Using built-in unittest
python tests/test_chatbot.py
```

---

## ⚙️ How It Works

The matching engine (`matcher.py`) uses **3 strategies in order**:

```
User Input
    │
    ▼
1. EXACT MATCH     → "hello" == "hello"          ✅ Return response
    │ (no match)
    ▼
2. PHRASE MATCH    → "show status" in input       ✅ Return response
    │ (no match)
    ▼
3. WORD SCAN       → any word in input ∈ keywords ✅ Return response
    │ (no match)
    ▼
4. FALLBACK        → "I didn't understand..."
```

---

## 📄 Documents

All academic documents are in the `docs/` folder:

| Document             | Description                          |
|----------------------|--------------------------------------|
| `Project_Proposal.md`| Project objectives and plan          |
| `HLD.md`             | High-Level Design (architecture)     |
| `LLD.md`             | Low-Level Design (code logic detail) |
| `Final_Report.md`    | Complete project report              |

---

## 🛠️ Technologies Used

- **Language:** Python 3.x (Standard Library only)
- **Concepts:** String Matching, CLI Design, NLP basics, Unit Testing
- **Tool:** VS Code
- **Testing:** `unittest` / `pytest`

---

*Roll No: PRJN26-127 | EduBot CLI Chatbot | Final Year Project*
