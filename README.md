<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:6D28D9,50:9333EA,100:EC4899&height=220&section=header&text=Character%20Resonance%20Engine&fontSize=46&fontColor=ffffff&fontAlignY=38&animation=fadeIn&desc=Which%20fictional%20character%20thinks%20the%20way%20you%20do%3F&descAlignY=58&descSize=18" alt="header banner"/>

<br/>

<a href="https://characte2r.vercel.app/">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2600&pause=900&color=C084FC&center=true&vCenter=true&width=650&lines=Answers+aren't+scores.+They're+evidence.;12-dimensional+behavioral+profiling;Adaptive+questioning+%E2%80%94+the+quiz+learns+as+you+play;Not+%22you+are+Batman%22.+Why+you+are+Batman." alt="typing animation"/>
</a>

<br/><br/>

<img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white"/>
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white"/>
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white"/>

<br/><br/>

<img src="https://img.shields.io/badge/self--ranking-100%25-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/robustness-100%25%20(100%2F100)-brightgreen?style=flat-square"/>
<img src="https://img.shields.io/badge/dimensions-12-blueviolet?style=flat-square"/>
<img src="https://img.shields.io/badge/universes-4-orange?style=flat-square"/>
<img src="https://img.shields.io/badge/license-MIT-informational?style=flat-square"/>

<br/><br/>

<a href="https://characte2r.vercel.app/"><b>🎮 Live Demo</b></a> ·
<a href="#-architecture"><b>🏗 Architecture</b></a> ·
<a href="#-how-it-works"><b>⚙ How it Works</b></a> ·
<a href="#-testing--evaluation"><b>🧪 Testing</b></a> ·
<a href="#-running-locally"><b>🚀 Run Locally</b></a>

</div>

<br/>

<img width="100%" src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.gif"/>

## 💡 The Idea

Most personality quizzes work like this:

> `Question → Answer → Score → Character`

**Character Resonance Engine** treats every answer as **behavioral evidence** rather than a scoring point. That evidence progressively builds a multi-dimensional profile — while the system continuously decides which question will teach it the most, next.

<div align="center">

```
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
 ┌──────┼──────┐
 ▼      ▼      ▼
EXPLORE DISCOVER REFINE
 │      │      │
 └──────┼──────┘
        ▼
 CHARACTER RANKING
        │
        ▼
 MATCH EXPLANATION
```

</div>

> The result isn't just **who** you matched with. It's **why**.

<br/>

## ⚙ How It Works

### 01 · Behavioral Modeling

Every answer can contribute to **multiple** behavioral dimensions at once — nothing is forced into a single bucket.

<div align="center">

| Dimension | | Dimension |
|:--|:--:|:--|
| 🗡 `ACTION` | | 🧩 `ANALYTICAL` |
| 💞 `EMPATHETIC` | | ⚖ `JUSTICE_DRIVEN` |
| 🚀 `AMBITIOUS` | | 🎨 `CREATIVE` |
| 🤝 `LOYAL` | | 🎯 `DISCIPLINED` |
| 😂 `HUMOROUS` | | 🔍 `CURIOUS` |
| 🛠 `PRAGMATIC` | | 🔥 `REBELLIOUS` |

</div>

**Example profile:**

```text
ACTION            ████████████████░░  0.91
LOYAL             ████████████████░░  0.93
JUSTICE_DRIVEN    ███████████████░░░  0.84
EMPATHETIC        ██████████████░░░░  0.78
ANALYTICAL        █████████████░░░░░  0.67
CREATIVE          ████████████░░░░░░  0.61
```

<br/>

### 02 · Adaptive Questioning

The quiz never walks a fixed script — the **next question is chosen live**, based on what the engine still needs to learn.

<table align="center">
<tr>
<td width="33%" valign="top">

**🔭 Exploration**

Early questions cast a wide net across all 12 dimensions to build broad coverage fast.

</td>
<td width="33%" valign="top">

**🔦 Discovery**

Once evidence accumulates, the engine hunts for the question that best *separates* the leading candidates.

</td>
<td width="33%" valign="top">

**🎯 Refinement**

Final questions attack the last pocket of uncertainty between the top contenders.

</td>
</tr>
</table>

<div align="center">

`EXPLORATION` → `DISCOVERY` → `REFINEMENT`

</div>

<br/>

### 03 · Character Matching

Every character lives in the **same** 12D behavioral space as the user. Instead of one similarity metric, the ranking engine blends several signals:

<div align="center">

| Signal | Weight |
|:--|:--:|
| 🎯 Signature similarity | **55%** |
| 💪 Strong trait matching | **20%** |
| 📈 Profile similarity | **15%** |
| 📐 Cosine similarity | **10%** |
| ⚠ Contradiction penalty | *applied separately* |

</div>

<br/>

### 04 · Match Explanation

The engine doesn't stop at `You are Batman — 87%`. It shows the receipts.

```text
WHY THIS ONE

ACTION          YOU 91%   ██████████░  BATMAN 92%  ██████████░
ANALYTICAL      YOU 86%   █████████░░  BATMAN 100% ███████████
LOYAL           YOU 94%   ███████████  BATMAN 96%  ███████████
PRAGMATIC       YOU 90%   █████████░░  BATMAN 98%  ███████████
```

The interface translates that side-by-side comparison into a plain-language explanation — the result feels **interpretable**, not arbitrary.

<br/>

## 🏗 Architecture

```
┌───────────────────────────────────────────────────────────┐
│                        FRONTEND                            │
│               Next.js · React · TypeScript                 │
└──────────────────────────────┬──────────────────────────────┘
                                │ HTTP
                                ▼
┌───────────────────────────────────────────────────────────┐
│                         FASTAPI                             │
│                     Quiz / API Layer                        │
└──────────────────────────────┬──────────────────────────────┘
                                ▼
┌───────────────────────────────────────────────────────────┐
│                       QUIZ SERVICE                          │
│      session state · responses · progression · evaluation   │
└────────────────┬───────────────────────────┬────────────────┘
                  ▼                           ▼
   ┌───────────────────────┐    ┌───────────────────────────┐
   │   QUESTION SELECTOR    │    │      BEHAVIOR ENGINE       │
   │  exploration/discovery/│    │  answer → evidence →       │
   │       refinement       │    │      12D vector             │
   └────────────┬────────────┘    └──────────────┬─────────────┘
                └──────────────┬──────────────────┘
                                ▼
                 ┌──────────────────────────┐
                 │      RANKING ENGINE       │
                 │  multi-signal scoring ·   │
                 │  comparison · explanation │
                 └────────────┬───────────────┘
                                ▼
                        CHARACTER RESULT
```

<details>
<summary><b>📂 Project Structure</b></summary>

```
character-resonance-engine/
│
├── frontend/
│   ├── app/
│   ├── components/
│   └── public/
│
├── backend/
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
│   │   └── compact_option.py
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

</details>

<br/>

## 🌌 Supported Universes

<div align="center">

<img src="https://skillicons.dev/icons?i=nextjs,react,ts,tailwind,py,fastapi&theme=dark" />

<br/><br/>

**MARVEL** · **DC** · **AVATAR: THE LAST AIRBENDER** · **KUNG FU PANDA**

</div>

The character registry is built so new characters and franchises can be dropped in **without touching the core matching architecture**.

<br/>

## 🧪 Testing & Evaluation

A dedicated harness (`backend/tests/evaluate_matching.py`) stress-tests the ranking engine.

<div align="center">

<table>
<tr><th>Suite</th><th>Result</th></tr>
<tr><td>🎯 Self-Ranking (Batman, Superman, Toph, Po)</td><td><img src="https://img.shields.io/badge/4%2F4-100%25-brightgreen?style=flat-square"/></td></tr>
<tr><td>🌪 Robustness (±0.05 noise, 4 chars × 25 runs)</td><td><img src="https://img.shields.io/badge/100%2F100-100%25-brightgreen?style=flat-square"/></td></tr>
<tr><td>🔀 Confusion Testing (blended profile pairs)</td><td><img src="https://img.shields.io/badge/ambiguity-mapped-blue?style=flat-square"/></td></tr>
</table>

</div>

A fixed random seed keeps every run reproducible.

```bash
# from the backend directory
python -m tests.evaluate_matching
```

<br/>

## 🚀 Running Locally

<table>
<tr>
<td width="50%" valign="top">

### Backend

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt
uvicorn main:app --reload
```

📍 `http://localhost:8000`

</td>
<td width="50%" valign="top">

### Frontend

```bash
cd frontend
npm install
npm run dev
```

📍 `http://localhost:3000`

</td>
</tr>
</table>

<br/>

## 🧭 Design Philosophy

<div align="center">

The app is presented as a **character-matching experience** — not a scientific personality assessment.

```
CHOICE → BEHAVIOR → PATTERN → CHARACTER
```

It doesn't claim to determine who someone objectively *is*.
It asks something more interesting:

**Which fictional character reflects the pattern in the choices you make?**

</div>

<br/>

## 🗺 Roadmap

- [x] Behavioral vector model
- [x] Character profile system
- [x] Adaptive question selection
- [x] Multi-signal ranking
- [x] Match explanations
- [x] Evaluation harness
- [x] Robustness testing
- [ ] Expanded character archive
- [ ] Larger evaluation dataset
- [ ] Automated profile calibration
- [ ] Improved ambiguity handling
- [ ] Additional universes

<br/>

<div align="center">

<img width="100%" src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.gif"/>

### Fictional characters are mirrors.

*We don't recognize ourselves in a character because we share their story.*
*We recognize something in the way they think, react, decide, and behave.*

**Every choice leaves a trace. Every trace forms a pattern.**

<br/>

<sub>Character Resonance Engine · AX-0900</sub>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:EC4899,50:9333EA,100:6D28D9&height=120&section=footer"/>

</div>
