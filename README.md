<!-- ═══════════════════════════════════════════════════════════════ -->

<!--                     CHARACTER RESONANCE ENGINE                  -->

<!-- ═══════════════════════════════════════════════════════════════ -->

<p align="center">
  <img
    src="https://capsule-render.vercel.app/api?type=waving&color=0:090909,45:171612,100:3b3932&height=190&section=header&text=CHARACTER%20RESONANCE%20ENGINE&fontSize=31&fontColor=e9e4d7&animation=fadeIn&fontAlignY=38"
    width="100%"
    alt="Character Resonance Engine"
  />
</p>

<p align="center">
  <img
    src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=14&duration=3200&pause=1000&color=AAA59B&center=true&vCenter=true&width=720&lines=Every+choice+leaves+a+trace.;Every+trace+forms+a+pattern.;Find+the+fictional+character+you+resonate+with."
    alt="Every choice leaves a trace. Every trace forms a pattern."
  />
</p>

<p align="center">
  <strong>What fictional character resonates with the way you think?</strong>
</p>

<p align="center">
  An adaptive behavioral profiling engine that turns your choices into a
  dynamic personality vector and finds the fictional character whose
  behavioral pattern matches yours.
</p>

<br>

<p align="center">
  <a href="https://characte2r.vercel.app/">
    <img src="https://img.shields.io/badge/%E2%96%B6%20LIVE%20DEMO-e9e4d7?style=for-the-badge&labelColor=11110f&color=3b3932" alt="Live Demo">
  </a>
  <a href="#architecture">
    <img src="https://img.shields.io/badge/%E2%97%87%20ARCHITECTURE-d8d3c8?style=for-the-badge&labelColor=11110f&color=3b3932" alt="Architecture">
  </a>
  <a href="#how-it-works">
    <img src="https://img.shields.io/badge/%E2%97%87%20HOW%20IT%20WORKS-d8d3c8?style=for-the-badge&labelColor=11110f&color=3b3932" alt="How it works">
  </a>
  <a href="#testing">
    <img src="https://img.shields.io/badge/%E2%97%87%20TESTING-d8d3c8?style=for-the-badge&labelColor=11110f&color=3b3932" alt="Testing">
  </a>
</p>

<br>

<p align="center">
  <img src="https://img.shields.io/badge/PYTHON-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FASTAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/NEXT.JS-000000?style=flat-square&logo=next.js&logoColor=white" alt="Next.js">
  <img src="https://img.shields.io/badge/TYPESCRIPT-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/REACT-61DAFB?style=flat-square&logo=react&logoColor=black" alt="React">
</p>

<br>

<p align="center">
  <sub>
    ──────────────────────────────── ✦ ────────────────────────────────
  </sub>
</p>

<p align="center">
  <em>
    A behavioral matching system disguised as a character experience.
  </em>
</p>

<p align="center">
  <sub>MARVEL · DC · AVATAR: THE LAST AIRBENDER · KUNG FU PANDA</sub>
</p>

<p align="center">
  <sub>
    ──────────────────────────────── ✦ ────────────────────────────────
  </sub>
</p>

◇ The Idea

Most personality quizzes work like this:

Question → Answer → Score → Character

Character Resonance Engine takes a different approach.

Your answers are treated as behavioral evidence.

That evidence progressively builds a multi-dimensional profile, while the system continuously decides which question will provide the most useful information next.

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

The result isn't just who you matched with.

It's why.

✦ How It Works

01 — Behavioral Modeling

Every answer can contribute to multiple behavioral dimensions.

The system currently models:

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

Instead of forcing an answer into a single category, behavioral evidence accumulates across the entire vector.

Example:

                    USER PROFILE

ACTION             ████████████████  0.91
ANALYTICAL         ████████████      0.67
EMPATHETIC         ██████████████    0.78
JUSTICE_DRIVEN     ███████████████   0.84
CREATIVE           ███████████       0.61
LOYAL              ████████████████  0.93
...

This gives the system a richer representation than a single personality label.

✦ Adaptive Questioning

The quiz does not simply walk through a fixed list of questions.

The next question is selected according to what the system still needs to learn.

Exploration

Early questions establish broad behavioral coverage.

"What kind of decision would you make?"
            ↓
Broad behavioral evidence

Discovery

Once enough evidence exists, the system looks for questions that distinguish between competing character profiles.

Candidate A ─────┐
                  ├── Which question separates them?
Candidate B ─────┘

Refinement

Later questions focus on unresolved differences between the strongest candidates.

TOP CANDIDATES
      ↓
Remaining uncertainty
      ↓
Most useful question
      ↓
Sharper profile

This creates a three-stage selection strategy:

EXPLORATION
     ↓
DISCOVERY
     ↓
REFINEMENT

✦ Character Matching

Each character exists inside the same behavioral space as the user.

The ranking engine combines multiple signals instead of relying on one similarity metric.

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

Current ranking configuration:

Signal

Weight

Signature similarity

55%

Strong trait matching

20%

Profile similarity

15%

Cosine similarity

10%

Contradiction penalty

Applied separately

The result is a ranked set of characters rather than a simple yes/no classification.

✦ Match Explanation

The engine doesn't stop at:

You are Batman — 87%.

It exposes the strongest signals behind the match.

WHY THIS ONE

ACTION             YOU 91%     BATMAN 92%
ANALYTICAL         YOU 86%     BATMAN 100%
LOYAL              YOU 94%     BATMAN 96%
PRAGMATIC          YOU 90%     BATMAN 98%

The interface can then translate those values into human-readable explanations.

The goal is to make the result feel interpretable rather than arbitrary.

✦ Architecture

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

✦ Project Structure

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

✦ Supported Universes

The archive currently contains characters from:

<div align="center">

MARVEL · DC · AVATAR: THE LAST AIRBENDER · KUNG FU PANDA

</div>

The character registry is designed so new characters and franchises can be added without changing the core matching architecture.

✦ Testing

The project includes a dedicated evaluation harness for validating the ranking system.

Self-Ranking

Known character vectors are passed directly into the ranking engine.

Batman       → Batman
Superman     → Superman
Toph         → Toph
Po           → Po

Result: 4 / 4 — 100%

Robustness

The same character vectors are perturbed with random noise of up to ±0.05 across the 12 behavioral dimensions.

Characters tested:       4
Runs per character:     25
Total runs:            100

Correct:               100
Incorrect:               0

Robustness:          100.0%

A fixed random seed is used to make the test reproducible.

Confusion Testing

The evaluation harness also creates blended profiles between character pairs to identify areas where character profiles occupy similar regions of the behavioral space.

This helps expose ambiguous regions rather than hiding them.

✦ Running Locally

Backend

cd backend

Create a virtual environment:

python -m venv venv

Windows

venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Start FastAPI

uvicorn main:app --reload

Backend:

http://localhost:8000

Frontend

cd frontend

Install dependencies:

npm install

Start the development server:

npm run dev

Frontend:

http://localhost:3000

✦ Run the Tests

From the backend directory:

python -m tests.evaluate_matching

The evaluation suite currently covers:

✓ Exact self-ranking
✓ Noisy-vector robustness
✓ Character confusion

✦ Design Philosophy

The application is intentionally presented as a character-matching experience, not as a scientific personality assessment.

The behavioral model is designed to create an interesting, explainable relationship between:

CHOICE
  ↓
BEHAVIOR
  ↓
PATTERN
  ↓
CHARACTER

The system does not claim to determine who someone objectively is.

It asks something more interesting:

Which fictional character reflects the pattern in the choices you make?

✦ Tech Stack

Frontend

Next.js

React

TypeScript

Tailwind CSS

Backend

Python

FastAPI

Pydantic

Core Engine

12-dimensional behavioral vectors

Adaptive question selection

Multi-signal ranking

Character profile modeling

Match explanation

Automated evaluation

✦ Roadmap

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

✦ Final Thought

<div align="center">

FICTIONAL CHARACTERS ARE MIRRORS.

We don't recognize ourselves in a character because we share their story.

We recognize something in the way they think, react, decide, and behave.

Every choice leaves a trace.

Every trace forms a pattern.

</div>

<p align="center">
  <sub>Character Resonance Engine · AX-0900</sub>
</p>
