# Art Appreciation (ArtAp) — 100-Question Quiz & Answer Validation System

A rigorous, source-grounded quiz generator and answer validation system based strictly on **Lessons 1 to 4** of Art Appreciation. Designed for seamless execution on both desktop PCs and mobile smartphones, with zero clutter and zero irrelevant course mechanics (such as assignment deadlines or submission links).

---

## 🚀 Live Demo & GitHub Pages Deployment

This repository is structured for **1-click deployment on GitHub Pages**:

1. Push this repository to GitHub.
2. Go to **Settings** > **Pages**.
3. Under **Build and deployment** > **Source**, select **Deploy from a branch**.
4. Choose the `main` branch and `/ (root)` folder, then click **Save**.
5. Your live quiz will be available at:  
   `https://<your-username>.github.io/<repository-name>/`

---

## 📁 Repository Structure

```text
ArtAp Quiz/
├── index.html            # Main web application entry point (GitHub Pages ready)
├── style.css             # Modern responsive stylesheet (Dark/Light themes, mobile-first)
├── app.js                # State management, sound synthesis (Web Audio API), UI events
├── validator.js          # Client-side 8-Step Identification Answer Validation Engine
├── questions.js          # Complete 100-question database (JavaScript format)
├── questions.json        # Complete 100-question database (JSON format)
├── QuizApp.java          # Standalone Java terminal runner and validation engine
├── validator.py          # Python implementation of the validation engine
├── test_validator.py     # Automated test suite for the validation algorithm
├── generate_questions.py # Source extraction & question generation script
└── README.md             # Project documentation
```

---

## 🎯 Quiz Features

- **100 Comprehensive Questions**:
  - **Lesson 1: Introduction to Art Appreciation** (25 Questions)
  - **Lesson 2: Language of Art: Elements of Art** (25 Questions)
  - **Lesson 3: Principles of Design and Psychology in Art** (25 Questions)
  - **Lesson 4: Materials and Techniques** (25 Questions)
- **Balanced Formats**:
  - 36 Multiple Choice Questions (plausible distractors, unambiguous single answer).
  - 32 Identification Questions (evaluated through the 8-step validation pipeline).
  - 32 True or False Questions (independently verifiable, meaningful factual error corrections).
- **8-Step Identification Answer Validation Pipeline**:
  1. *Normalization*: Case normalization, whitespace collapsing, harmless punctuation stripping, Unicode diacritic removal.
  2. *Exact & Accepted Equivalents*: Evaluates canonical answers, acronyms, and synonyms.
  3. *Levenshtein Distance Typo Tolerance*: Tolerates unmistakable typos based on word length thresholds without compromising meaning.
  4. *Semantic & Keyword Verification*: Ensures all required components of multi-part answers are present.
  5. *Near-Miss & Ambiguity Detection*: Prevents confusing related terms (e.g., Sfumato vs. Chiaroscuro; Proportion vs. Scale; Medium vs. Technique).
  6. *Grading Classifications*: `CORRECT`, `CORRECT — MINOR VARIATION`, `PARTIALLY CORRECT`, `INCORRECT`.
  7. *Detailed Feedback & Source Grounding*: Canonical answers, distinctions from near-misses, and lecture explanations.
  8. *Questionable Answer Re-evaluation*.
- **Interactive UI**:
  - Fully responsive on mobile phones and PC screens.
  - Dark mode by default with light mode toggle.
  - Interactive Web Audio sound effects (pure synthetic audio, no external asset loading needed).
  - Lesson filter, question type filter, and optional retry mode.
  - First-attempt accuracy score tracking and streak counter.
  - End-of-quiz performance report and missed question review.

---

## ☕ Running Locally

### Option A: In the Browser (No installation needed)
Simply double-click `index.html` or open it with any web browser, or start a local server:
```bash
python -m http.server 8000
```
Open `http://localhost:8000` in your browser.

### Option B: Standalone Java Terminal Runner
Compile and run with OpenJDK 21+:
```bash
javac QuizApp.java
java QuizApp
```

### Option C: Run Validation Test Suite (Python)
```bash
python test_validator.py
```
