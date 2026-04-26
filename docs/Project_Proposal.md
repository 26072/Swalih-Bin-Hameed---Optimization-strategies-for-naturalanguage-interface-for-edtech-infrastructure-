# PROJECT PROPOSAL

---

**Project Title:** Optimization Strategies for Natural Language Interface for EdTech Infrastructure

**Project ID:** PRJN26-127

**Roll No:** PRJN26-127

**Technology:** Python, Basic String Matching

**Tool:** VS Code

**Submission Date:** April 2026

---

## 1. Introduction

The rapid evolution of digital education has created a significant demand for intelligent, automated systems that can assist students in navigating educational platforms efficiently. Chatbots — conversational agents that simulate human interaction — have emerged as a powerful interface layer between students and educational platforms.

This project proposes the design and development of **EduBot**, a Command-Line Interface (CLI) chatbot for an EdTech platform. EduBot uses Python and basic string matching techniques to answer common student queries related to courses, assignments, grades, schedules, and platform support.

---

## 2. Problem Statement

Students interacting with EdTech platforms often face challenges in finding timely answers to routine queries such as:

- "What courses are available?"
- "What is my assignment deadline?"
- "How do I enroll in a course?"
- "What is my grade?"

Answering these queries typically requires navigating complex portals or waiting for human support agents. A CLI-based chatbot can provide **instant, structured responses** to such queries without requiring internet-dependent UI systems.

---

## 3. Objectives

The primary objectives of this project are:

1. **Build a CLI chatbot** using Python that accepts natural language input from students.
2. **Implement basic string matching** techniques to interpret user queries.
3. **Design a structured knowledge base** of pre-defined EdTech responses.
4. **Develop a command loop** that continuously accepts and responds to student input.
5. **Apply DevOps practices** through unit testing and session logging.
6. **Produce complete documentation** — Proposal, HLD, LLD, and Final Report.

---

## 4. Scope

### In Scope:
- Command-line interface (no GUI or web interface)
- Pre-defined responses for common EdTech queries
- Basic string/keyword matching (no ML or deep learning)
- Unit testing with Python's `unittest` / `pytest`
- Session logging to a local `.log` file
- Documentation for academic submission

### Out of Scope:
- Integration with real student databases or APIs
- Natural Language Processing using ML models
- Web or mobile interface
- Real-time data (grades, assignments are simulated)

---

## 5. Proposed Solution

EduBot is structured into three core modules:

| Module              | Role                                           |
|---------------------|------------------------------------------------|
| `chatbot.py`        | CLI loop — reads input, displays responses     |
| `matcher.py`        | 3-strategy keyword matching engine             |
| `knowledge_base.py` | Dictionary of keywords and pre-defined answers |

**Matching Strategy (3-tier):**
1. **Exact Match** — Input equals a keyword exactly
2. **Phrase Match** — A keyword phrase is contained in the input
3. **Word Scan** — Any individual keyword word appears in input tokens
4. **Fallback** — Polite error message with suggestions

---

## 6. Technology Stack

| Component     | Technology              |
|---------------|-------------------------|
| Language      | Python 3.x              |
| Matching      | Basic String Matching   |
| Testing       | `unittest`, `pytest`    |
| Logging       | Python `time` module    |
| IDE           | VS Code                 |
| Version Ctrl  | Git (recommended)       |

---

## 7. Dataset / Knowledge Base

The knowledge base is **industry-relevant and open-source in design**, meaning:
- All responses are modeled after real EdTech platform FAQs (Coursera, NPTEL, Udemy patterns)
- The `KEYWORD_MAP` contains **200+ keywords** across **20+ intent categories**
- The `RESPONSES` dictionary provides structured, informative answers for each intent
- No proprietary data is used — the system is fully self-contained

---

## 8. Project Timeline

| Phase | Activity                          | Duration   |
|-------|-----------------------------------|------------|
| 1     | Requirement Analysis & Proposal   | Week 1     |
| 2     | High-Level Design (HLD)           | Week 1-2   |
| 3     | Low-Level Design (LLD)            | Week 2     |
| 4     | Core Development (Python code)    | Week 2-3   |
| 5     | Testing & Debugging               | Week 3-4   |
| 6     | Documentation & Final Report      | Week 4     |
| 7     | Submission & Demo                 | Week 4     |

---

## 9. Learning Outcomes

Upon completion of this project, the student will:

1. Understand the fundamentals of **natural language interface design**
2. Gain proficiency in **Python programming** — loops, functions, dictionaries, modules
3. Learn **basic string matching** — a foundational NLP technique
4. Apply **software engineering practices** — modular design, unit testing, logging
5. Experience **AI/DevOps workflows** — testing pipelines, version control, documentation
6. Understand **chatbot architecture** and intent-response mapping

---

## 10. Expected Deliverables

| Deliverable           | Description                                  |
|-----------------------|----------------------------------------------|
| `chatbot.py`          | Main CLI chatbot program                     |
| `matcher.py`          | Keyword matching engine                      |
| `knowledge_base.py`   | All keywords and responses                   |
| `test_chatbot.py`     | Unit test suite (30+ test cases)             |
| `README.md`           | Setup and usage guide                        |
| `Project_Proposal.md` | This document                                |
| `HLD.md`              | High-Level Design document                   |
| `LLD.md`              | Low-Level Design document                    |
| `Final_Report.md`     | Complete project report                      |

---

## 11. Conclusion

EduBot demonstrates how even simple, foundational programming concepts — Python dictionaries, string matching, and CLI loops — can be combined to create a meaningful, usable product. This project bridges the gap between basic programming skills and real-world AI/DevOps application in the EdTech domain.

---

*Submitted by: PRJN26-127 | Final Year Project | April 2026*