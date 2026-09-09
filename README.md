# ◈ Character Resonance Engine

<p align="center">
  <strong>What fictional character resonates with the way you think?</strong>
</p>

<p align="center">
  An adaptive behavioral profiling engine that turns your choices into a dynamic personality vector and finds the fictional character whose behavioral pattern matches yours.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square\&logo=python\&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square\&logo=fastapi\&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square\&logo=next.js\&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square\&logo=typescript\&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square\&logo=react\&logoColor=black)

</p>

<p align="center">

**[Live Demo](#)** · **[Architecture](#architecture)** · **[How-it-works](#how-it-works)** · **[Testing](#testing)**

</p>

---

## ◇ The Idea

Most personality quizzes work like this:

```text
Question → Answer → Score → Character
```

Character Resonance Engine takes a different approach.

Your answers are treated as **behavioral evidence**.

That evidence progressively builds a multi-dimensional profile, while the system continuously decides which question will provide the most useful information next.

```text
                 YOUR CHOICES
                      │
                      ▼
              BEHAVIORAL EVIDENCE
                      │
                      ▼
                12D PROFILE
                      │
                      ▼
            ADAPTIVE QUESTIONING
                      │
             ┌────────┼────────┐
             ▼        ▼        ▼
        EXPLORATION DISCOVERY REFINEMENT
             │        │        │
             └────────┼────────┘
                      ▼
              CHARACTER RANKING
                      │
                      ▼
               MATCH EXPLANATION
```

The result isn't just **who you matched with**.

It's **why**.

---

# ◈ How It Works

## 01 — Behavioral Modeling

Every answer can contribute to multiple behavioral dimensions.

The system currently models:

```text
ACTION
ANALYTICAL
EMPATHETIC
JUSTICE_DRIVEN
AMBITIOUS
CREATIVE
LOYAL
DISCIPLINED
HUMOROUS
CURIOUS
PRAGMATIC
REBELLIOUS
```

Instead of forcing an answer into a single category, behavioral evidence accumulates across the entire vector.

Example:

```text
                    USER PROFILE

ACTION             ████████████████  0.91
ANALYTICAL         ████████████      0.67
EMPATHETIC         ██████████████    0.78
JUSTICE_DRIVEN     ███████████████   0.84
CREATIVE           ███████████       0.61
LOYAL              ████████████████  0.93
...
```

This gives the system a richer representation than a single personality label.

---

# ◈ Adaptive Questioning

The quiz does not simply walk through a fixed list of questions.

The next question is selected according to what the system still needs to learn.

### Exploration

Early questions establish broad behavioral coverage.

```text
"What kind of decision would you make?"
            ↓
Broad behavioral evidence
```

### Discovery

Once enough evidence exists, the system looks for questions that distinguish between competing character profiles.

```text
Candidate A ─────┐
                  ├── Which question separates them?
Candidate B ─────┘
```

### Refinement

Later questions focus on unresolved differences between the strongest candidates.

```text
TOP CANDIDATES
      ↓
Remaining uncertainty
      ↓
Most useful question
      ↓
Sharper profile
```

This creates a three-stage selection strategy:

```text
EXPLORATION
     ↓
DISCOVERY
     ↓
REFINEMENT
```

---

# ◈ Character Matching

Each character exists inside the same behavioral space as the user.

The ranking engine combines multiple signals instead of relying on one similarity metric.

```text
USER VECTOR
     │
     ├── Signature similarity
     ├── Strong trait matching
     ├── Profile similarity
     ├── Cosine similarity
     └── Contradiction penalty
              │
              ▼
        FINAL RANKING
```

Current ranking configuration:

| Signal                |             Weight |
| --------------------- | -----------------: |
| Signature similarity  |                55% |
| Strong trait matching |                20% |
| Profile similarity    |                15% |
| Cosine similarity     |                10% |
| Contradiction penalty | Applied separately |

The result is a ranked set of characters rather than a simple yes/no classification.

---

# ◈ Match Explanation

The engine doesn't stop at:

> **You are Batman — 87%.**

It exposes the strongest signals behind the match.

```text
WHY THIS ONE

ACTION             YOU 91%     BATMAN 92%
ANALYTICAL         YOU 86%     BATMAN 100%
LOYAL              YOU 94%     BATMAN 96%
PRAGMATIC          YOU 90%     BATMAN 98%
```

The interface can then translate those values into human-readable explanations.

The goal is to make the result feel **interpretable rather than arbitrary**.

---

# ◈ Architecture

```text
┌──────────────────────────────────────────────────────────────┐
│                         FRONTEND                             │
│                                                              │
│             Next.js + React + TypeScript                     │
│                                                              │
└──────────────────────────────┬───────────────────────────────┘
                               │
                               │ HTTP
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                         FASTAPI                              │
│                                                              │
│                    Quiz / API Layer                          │
│                                                              │
└──────────────────────────────┬───────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                       QUIZ SERVICE                            │
│                                                              │
│     Session state · responses · progression · evaluation     │
│                                                              │
└───────────────┬──────────────────────────────┬───────────────┘
                │                              │
                ▼                              ▼
┌──────────────────────────┐      ┌────────────────────────────┐
│   QUESTION SELECTOR      │      │      BEHAVIOR ENGINE       │
│                          │      │                            │
│ Exploration              │      │ Answer → Evidence          │
│ Discovery                │      │ Evidence → 12D Vector     │
│ Refinement               │      │                            │
└────────────┬─────────────┘      └──────────────┬─────────────┘
             │                                   │
             └────────────────┬──────────────────┘
                              ▼
                 ┌─────────────────────────┐
                 │     RANKING ENGINE      │
                 │                         │
                 │ Multi-signal scoring    │
                 │ Character comparison    │
                 │ Match explanation       │
                 └────────────┬────────────┘
                              │
                              ▼
                       CHARACTER RESULT
```

---

# ◈ Project Structure

```text
character-resonance-engine/
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── public/
│   └── ...
│
├── backend/
│   │
│   ├── data/
│   │   ├── behavior_profiles.py
│   │   ├── character_registry.py
│   │   └── questions.py
│   │
│   ├── engine/
│   │   ├── behavior_engine.py
│   │   ├── question_selector.py
│   │   ├── quiz_engine.py
│   │   └── ranking_engine.py
│   │
│   ├── models/
│   │   ├── behavior.py
│   │   ├── compact_option.py
│   │   └── ...
│   │
│   ├── services/
│   │   ├── question_service.py
│   │   └── quiz_service.py
│   │
│   ├── tests/
│   │   └── evaluate_matching.py
│   │
│   └── main.py
│
└── README.md
```

---

# ◈ Supported Universes

The archive currently contains characters from:

<div align="center">

**MARVEL** · **DC** · **AVATAR: THE LAST AIRBENDER** · **KUNG FU PANDA**

</div>

The character registry is designed so new characters and franchises can be added without changing the core matching architecture.

---

# ◈ Testing

The project includes a dedicated evaluation harness for validating the ranking system.

### Self-Ranking

Known character vectors are passed directly into the ranking engine.

```text
Batman       → Batman
Superman     → Superman
Toph         → Toph
Po           → Po
```

**Result: 4 / 4 — 100%**

### Robustness

The same character vectors are perturbed with random noise of up to ±0.05 across the 12 behavioral dimensions.

```text
Characters tested:       4
Runs per character:     25
Total runs:            100

Correct:               100
Incorrect:               0

Robustness:          100.0%
```

A fixed random seed is used to make the test reproducible.

### Confusion Testing

The evaluation harness also creates blended profiles between character pairs to identify areas where character profiles occupy similar regions of the behavioral space.

This helps expose ambiguous regions rather than hiding them.

---

# ◈ Running Locally

## Backend

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

### Windows

```powershell
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start FastAPI

```bash
uvicorn main:app --reload
```

Backend:

```text
http://localhost:8000
```

---

## Frontend

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Frontend:

```text
http://localhost:3000
```

---

# ◈ Run the Tests

From the backend directory:

```bash
python -m tests.evaluate_matching
```

The evaluation suite currently covers:

```text
✓ Exact self-ranking
✓ Noisy-vector robustness
✓ Character confusion
```

---

# ◈ Design Philosophy

The application is intentionally presented as a **character-matching experience**, not as a scientific personality assessment.

The behavioral model is designed to create an interesting, explainable relationship between:

```text
CHOICE
  ↓
BEHAVIOR
  ↓
PATTERN
  ↓
CHARACTER
```

The system does not claim to determine who someone objectively is.

It asks something more interesting:

> **Which fictional character reflects the pattern in the choices you make?**

---

# ◈ Tech Stack

### Frontend

* Next.js
* React
* TypeScript
* Tailwind CSS

### Backend

* Python
* FastAPI
* Pydantic

### Core Engine

* 12-dimensional behavioral vectors
* Adaptive question selection
* Multi-signal ranking
* Character profile modeling
* Match explanation
* Automated evaluation

---

# ◈ Roadmap

```text
[x] Behavioral vector model
[x] Character profile system
[x] Adaptive question selection
[x] Multi-signal ranking
[x] Match explanations
[x] Evaluation harness
[x] Robustness testing
[ ] Expanded character archive
[ ] Larger evaluation dataset
[ ] Automated profile calibration
[ ] Improved ambiguity handling
[ ] Additional universes
```

---

# ◈ Final Thought

<div align="center">

### FICTIONAL CHARACTERS ARE MIRRORS.

We don't recognize ourselves in a character because we share their story.

We recognize something in the way they **think, react, decide, and behave.**

**Every choice leaves a trace.**

**Every trace forms a pattern.**

</div>

---

<p align="center">
  <sub>Character Resonance Engine · AX-0900</sub>
</p>
