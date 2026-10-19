/**
 * Art Appreciation Quiz Application
 * Handles State, Filtering, Validation, Sound, UI Updates, and Scoring
 */

// Sound Synthesizer via Web Audio API
class SoundFx {
  constructor() {
    this.ctx = null;
    this.muted = false;
  }

  init() {
    if (!this.ctx) {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      if (AudioContext) {
        this.ctx = new AudioContext();
      }
    }
  }

  playCorrect() {
    if (this.muted) return;
    this.init();
    if (!this.ctx) return;

    try {
      const now = this.ctx.currentTime;
      const osc1 = this.ctx.createOscillator();
      const osc2 = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc1.type = "sine";
      osc2.type = "sine";

      osc1.frequency.setValueAtTime(523.25, now); // C5
      osc1.frequency.exponentialRampToValueAtTime(659.25, now + 0.15); // E5

      osc2.frequency.setValueAtTime(659.25, now);
      osc2.frequency.exponentialRampToValueAtTime(783.99, now + 0.15); // G5

      gain.gain.setValueAtTime(0.15, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);

      osc1.connect(gain);
      osc2.connect(gain);
      gain.connect(this.ctx.destination);

      osc1.start(now);
      osc2.start(now);
      osc1.stop(now + 0.35);
      osc2.stop(now + 0.35);
    } catch (e) {
      // Audio autoplay policy
    }
  }

  playIncorrect() {
    if (this.muted) return;
    this.init();
    if (!this.ctx) return;

    try {
      const now = this.ctx.currentTime;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc.type = "sawtooth";
      osc.frequency.setValueAtTime(180, now);
      osc.frequency.exponentialRampToValueAtTime(110, now + 0.25);

      gain.gain.setValueAtTime(0.15, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.3);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start(now);
      osc.stop(now + 0.3);
    } catch (e) {}
  }
}

// App State Manager
class QuizApp {
  constructor() {
    this.sound = new SoundFx();
    this.allQuestions = typeof QUIZ_QUESTIONS !== "undefined" ? QUIZ_QUESTIONS : [];
    this.activeQuestions = [...this.allQuestions];
    this.currentIndex = 0;
    this.isAnswered = false;
    this.isRetryAttempt = false;

    // Scoring State
    this.stats = {
      firstAttemptCorrect: 0,
      minorVariations: 0,
      incorrect: 0,
      retriesUsed: 0,
      streak: 0,
      maxStreak: 0,
      missedQuestions: []
    };

    this.initDOMElements();
    this.bindEvents();
    this.applyFilters();
    this.renderQuestion();
  }

  initDOMElements() {
    // Header & Controls
    this.btnTheme = document.getElementById("btn-theme");
    this.themeIcon = document.getElementById("theme-icon");
    this.btnSound = document.getElementById("btn-sound");
    this.soundIcon = document.getElementById("sound-icon");
    this.btnRestart = document.getElementById("btn-restart");
    this.filterLesson = document.getElementById("filter-lesson");
    this.filterType = document.getElementById("filter-type");
    this.toggleRetry = document.getElementById("toggle-retry");

    // Progress Section
    this.currentQNum = document.getElementById("current-q-num");
    this.totalQNum = document.getElementById("total-q-num");
    this.scorePercentage = document.getElementById("score-percentage");
    this.streakCount = document.getElementById("streak-count");
    this.progressBarFill = document.getElementById("progress-bar-fill");

    // Main Card
    this.quizCard = document.getElementById("quiz-card");
    this.badgeLesson = document.getElementById("badge-lesson");
    this.badgeType = document.getElementById("badge-type");
    this.badgeAttempt = document.getElementById("badge-attempt");
    this.questionText = document.getElementById("question-text");

    // Containers
    this.mcContainer = document.getElementById("mc-container");
    this.tfContainer = document.getElementById("tf-container");
    this.idForm = document.getElementById("id-form");
    this.idInput = document.getElementById("id-input");
    this.btnSubmitId = document.getElementById("btn-submit-id");

    // Feedback
    this.feedbackCard = document.getElementById("feedback-card");
    this.feedbackBadge = document.getElementById("feedback-badge");
    this.feedbackSummary = document.getElementById("feedback-summary-title");
    this.canonicalWrap = document.getElementById("feedback-canonical-wrap");
    this.canonicalText = document.getElementById("feedback-canonical-text");
    this.distinctionWrap = document.getElementById("feedback-distinction-wrap");
    this.distinctionText = document.getElementById("feedback-distinction-text");
    this.alternativesWrap = document.getElementById("feedback-alternatives-wrap");
    this.alternativesText = document.getElementById("feedback-alternatives-text");
    this.explanationText = document.getElementById("feedback-explanation-text");
    this.btnRetry = document.getElementById("btn-retry");
    this.btnNext = document.getElementById("btn-next");

    // Results
    this.resultsCard = document.getElementById("results-card");
    this.finalScorePercent = document.getElementById("final-score-percent");
    this.statTotal = document.getElementById("stat-total");
    this.statFirstCorrect = document.getElementById("stat-first-correct");
    this.statMinorVariations = document.getElementById("stat-minor-variations");
    this.statIncorrect = document.getElementById("stat-incorrect");
    this.missedSection = document.getElementById("missed-review-section");
    this.missedList = document.getElementById("missed-list");
    this.btnRestartResults = document.getElementById("btn-restart-results");
    this.btnReviewMissed = document.getElementById("btn-review-missed");
  }

  bindEvents() {
    // Theme toggle
    this.btnTheme.addEventListener("click", () => {
      document.body.classList.toggle("theme-light");
      document.body.classList.toggle("theme-dark");
      const isDark = document.body.classList.contains("theme-dark");
      this.themeIcon.textContent = isDark ? "🌙" : "☀️";
      localStorage.setItem("artap_theme", isDark ? "dark" : "light");
    });

    // Sound toggle
    this.btnSound.addEventListener("click", () => {
      this.sound.muted = !this.sound.muted;
      this.soundIcon.textContent = this.sound.muted ? "🔇" : "🔊";
    });

    // Restart button
    this.btnRestart.addEventListener("click", () => this.restartQuiz());
    this.btnRestartResults.addEventListener("click", () => this.restartQuiz());

    // Filters
    this.filterLesson.addEventListener("change", () => {
      this.applyFilters();
      this.restartQuiz();
    });

    this.filterType.addEventListener("change", () => {
      this.applyFilters();
      this.restartQuiz();
    });

    // Form submission for Identification
    this.idForm.addEventListener("submit", (e) => {
      e.preventDefault();
      if (this.isAnswered) return;
      this.handleIdentificationSubmit();
    });

    // Next question
    this.btnNext.addEventListener("click", () => this.nextQuestion());

    // Retry question
    this.btnRetry.addEventListener("click", () => this.retryCurrentQuestion());

    // Review missed only
    this.btnReviewMissed.addEventListener("click", () => {
      if (this.stats.missedQuestions.length > 0) {
        this.activeQuestions = [...this.stats.missedQuestions];
        this.restartQuiz(false);
      }
    });

    // Keyboard Shortcuts
    window.addEventListener("keydown", (e) => {
      if (e.target.tagName === "INPUT" && e.key !== "Enter") {
        return; // Allow typing in input
      }

      if (this.isAnswered) {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          this.nextQuestion();
        }
        return;
      }

      const q = this.activeQuestions[this.currentIndex];
      if (!q) return;

      if (q.type === "multiple_choice") {
        const keyMap = { "1": "A", "2": "B", "3": "C", "4": "D", "a": "A", "b": "B", "c": "C", "d": "D" };
        const opt = keyMap[e.key.toLowerCase()];
        if (opt) {
          e.preventDefault();
          this.handleMultipleChoiceSubmit(opt);
        }
      } else if (q.type === "true_false") {
        if (e.key.toLowerCase() === "t" || e.key === "1") {
          e.preventDefault();
          this.handleTrueFalseSubmit(true);
        } else if (e.key.toLowerCase() === "f" || e.key === "2") {
          e.preventDefault();
          this.handleTrueFalseSubmit(false);
        }
      }
    });

    // Restore saved theme
    const savedTheme = localStorage.getItem("artap_theme");
    if (savedTheme === "light") {
      document.body.classList.remove("theme-dark");
      document.body.classList.add("theme-light");
      this.themeIcon.textContent = "☀️";
    }
  }

  applyFilters() {
    const lessonVal = this.filterLesson.value;
    const typeVal = this.filterType.value;

    this.activeQuestions = this.allQuestions.filter((q) => {
      const matchLesson = (lessonVal === "all") || (q.lesson.toString() === lessonVal);
      const matchType = (typeVal === "all") || (q.type === typeVal);
      return matchLesson && matchType;
    });

    if (this.activeQuestions.length === 0) {
      this.activeQuestions = [...this.allQuestions];
    }
  }

  restartQuiz(resetFilters = true) {
    if (resetFilters) {
      this.applyFilters();
    }
    this.currentIndex = 0;
    this.isAnswered = false;
    this.isRetryAttempt = false;
    this.stats = {
      firstAttemptCorrect: 0,
      minorVariations: 0,
      incorrect: 0,
      retriesUsed: 0,
      streak: 0,
      maxStreak: 0,
      missedQuestions: []
    };

    this.resultsCard.style.display = "none";
    this.quizCard.style.display = "block";
    this.updateProgress();
    this.renderQuestion();
  }

  renderQuestion() {
    this.isAnswered = false;
    const q = this.activeQuestions[this.currentIndex];

    if (!q) {
      this.showResults();
      return;
    }

    // Reset feedback
    this.feedbackCard.style.display = "none";
    this.btnRetry.style.display = "none";

    // Set Badges
    this.badgeLesson.textContent = `Lesson ${q.lesson}`;
    const typeLabels = {
      multiple_choice: "Multiple Choice",
      identification: "Identification",
      true_false: "True or False"
    };
    this.badgeType.textContent = typeLabels[q.type] || q.type;
    this.badgeAttempt.style.display = this.isRetryAttempt ? "inline-block" : "none";

    // Question Text
    this.questionText.textContent = q.question;

    // Toggle Inputs
    this.mcContainer.style.display = "none";
    this.tfContainer.style.display = "none";
    this.idForm.style.display = "none";

    if (q.type === "multiple_choice") {
      this.renderMultipleChoice(q);
    } else if (q.type === "true_false") {
      this.renderTrueFalse(q);
    } else if (q.type === "identification") {
      this.renderIdentification(q);
    }

    this.updateProgress();
  }

  renderMultipleChoice(q) {
    this.mcContainer.innerHTML = "";
    this.mcContainer.style.display = "flex";

    q.options.forEach((optStr) => {
      const letter = optStr.charAt(0);
      const text = optStr.substring(2).trim();

      const btn = document.createElement("button");
      btn.className = "btn-option";
      btn.dataset.letter = letter;

      btn.innerHTML = `
        <span class="opt-letter">${letter}</span>
        <span class="opt-text">${text}</span>
      `;

      btn.addEventListener("click", () => {
        if (!this.isAnswered) {
          this.handleMultipleChoiceSubmit(letter);
        }
      });

      this.mcContainer.appendChild(btn);
    });
  }

  renderTrueFalse(q) {
    this.tfContainer.style.display = "grid";
    const buttons = this.tfContainer.querySelectorAll(".btn-tf");
    buttons.forEach((btn) => {
      btn.disabled = false;
      btn.className = `btn-tf ${btn.dataset.value === "true" ? "btn-tf-true" : "btn-tf-false"}`;
      btn.onclick = () => {
        if (!this.isAnswered) {
          this.handleTrueFalseSubmit(btn.dataset.value === "true");
        }
      };
    });
  }

  renderIdentification(q) {
    this.idForm.style.display = "flex";
    this.idInput.value = "";
    this.idInput.disabled = false;
    this.btnSubmitId.disabled = false;
    setTimeout(() => this.idInput.focus(), 50);
  }

  handleMultipleChoiceSubmit(selectedLetter) {
    this.isAnswered = true;
    const q = this.activeQuestions[this.currentIndex];
    const validation = validateMultipleChoice(selectedLetter, q);

    // Highlight options
    const buttons = this.mcContainer.querySelectorAll(".btn-option");
    buttons.forEach((btn) => {
      btn.disabled = true;
      if (btn.dataset.letter === validation.correctAnswer) {
        btn.classList.add("correct-choice");
      }
      if (btn.dataset.letter === selectedLetter && !validation.isCorrect) {
        btn.classList.add("incorrect-choice");
      }
    });

    this.processValidationResult(validation, q);
  }

  handleTrueFalseSubmit(selectedVal) {
    this.isAnswered = true;
    const q = this.activeQuestions[this.currentIndex];
    const validation = validateTrueFalse(selectedVal, q);

    const buttons = this.tfContainer.querySelectorAll(".btn-tf");
    buttons.forEach((btn) => {
      btn.disabled = true;
      const val = btn.dataset.value === "true";
      if (val === validation.correctAnswer) {
        btn.style.borderColor = "var(--success)";
        btn.style.backgroundColor = "var(--success-bg)";
      } else if (val === selectedVal && !validation.isCorrect) {
        btn.style.borderColor = "var(--danger)";
        btn.style.backgroundColor = "var(--danger-bg)";
      }
    });

    this.processValidationResult(validation, q);
  }

  handleIdentificationSubmit() {
    const rawVal = this.idInput.value.trim();
    if (!rawVal) {
      this.idInput.focus();
      return;
    }

    this.isAnswered = true;
    this.idInput.disabled = true;
    this.btnSubmitId.disabled = true;

    const q = this.activeQuestions[this.currentIndex];
    const validation = validateIdentification(rawVal, q);
    this.processValidationResult(validation, q);
  }

  processValidationResult(res, question) {
    const isFirstAttempt = !this.isRetryAttempt;

    if (res.isCorrect) {
      this.sound.playCorrect();
      this.stats.streak++;
      if (this.stats.streak > this.stats.maxStreak) {
        this.stats.maxStreak = this.stats.streak;
      }

      if (isFirstAttempt) {
        this.stats.firstAttemptCorrect++;
      }
      if (res.classification === "CORRECT — MINOR VARIATION") {
        this.stats.minorVariations++;
      }
    } else {
      this.sound.playIncorrect();
      this.stats.streak = 0;
      if (isFirstAttempt) {
        this.stats.incorrect++;
        this.stats.missedQuestions.push(question);
      }
    }

    this.showFeedback(res, question);
    this.updateProgress();
  }

  showFeedback(res, question) {
    this.feedbackCard.style.display = "flex";

    // Set Badge and Style
    this.feedbackBadge.className = "feedback-badge";
    if (res.classification === "CORRECT") {
      this.feedbackBadge.classList.add("badge-correct");
      this.feedbackBadge.textContent = "CORRECT";
      this.feedbackSummary.textContent = "Exactly right!";
    } else if (res.classification === "CORRECT — MINOR VARIATION") {
      this.feedbackBadge.classList.add("badge-minor");
      this.feedbackBadge.textContent = "CORRECT — MINOR VARIATION";
      this.feedbackSummary.textContent = "Accepted with minor variation / spelling tolerance.";
    } else if (res.classification === "PARTIALLY CORRECT") {
      this.feedbackBadge.classList.add("badge-partial");
      this.feedbackBadge.textContent = "PARTIALLY CORRECT";
      this.feedbackSummary.textContent = "Key concept elements were identified, but crucial components are missing.";
    } else if (res.subType === "NEAR_MISS") {
      this.feedbackBadge.classList.add("badge-nearmiss");
      this.feedbackBadge.textContent = "INCORRECT — NEAR MISS";
      this.feedbackSummary.textContent = "Commonly confused or closely related concept.";
    } else {
      this.feedbackBadge.classList.add("badge-incorrect");
      this.feedbackBadge.textContent = "INCORRECT";
      this.feedbackSummary.textContent = "Incorrect answer.";
    }

    // Canonical Answer
    if (question.type === "multiple_choice") {
      const correctOpt = question.options.find(o => o.startsWith(question.correctAnswer));
      this.canonicalText.textContent = correctOpt || question.correctAnswer;
    } else if (question.type === "true_false") {
      this.canonicalText.textContent = question.correctAnswer ? "TRUE" : "FALSE";
    } else {
      this.canonicalText.textContent = question.canonicalAnswer;
    }

    // Distinction
    if (question.distinction) {
      this.distinctionWrap.style.display = "block";
      this.distinctionText.textContent = question.distinction;
    } else {
      this.distinctionWrap.style.display = "none";
    }

    // Accepted alternatives
    if (question.acceptedAlternatives && question.acceptedAlternatives.length > 0) {
      this.alternativesWrap.style.display = "block";
      this.alternativesText.textContent = question.acceptedAlternatives.join(", ");
    } else {
      this.alternativesWrap.style.display = "none";
    }

    // Explanation
    this.explanationText.textContent = res.explanation || question.explanation || "";

    // Retry option
    const canRetry = !res.isCorrect && this.toggleRetry.checked && !this.isRetryAttempt;
    if (canRetry) {
      this.btnRetry.style.display = "inline-flex";
    } else {
      this.btnRetry.style.display = "none";
    }

    // Focus next button
    this.btnNext.focus();
  }

  retryCurrentQuestion() {
    this.isRetryAttempt = true;
    this.stats.retriesUsed++;
    this.renderQuestion();
  }

  nextQuestion() {
    this.isRetryAttempt = false;
    this.currentIndex++;
    if (this.currentIndex >= this.activeQuestions.length) {
      this.showResults();
    } else {
      this.renderQuestion();
    }
  }

  updateProgress() {
    const total = this.activeQuestions.length;
    const current = Math.min(this.currentIndex + 1, total);

    this.currentQNum.textContent = current;
    this.totalQNum.textContent = total;

    // Score calculation based on first-attempt accuracy
    const answeredCount = this.currentIndex + (this.isAnswered ? 1 : 0);
    const pct = answeredCount > 0 ? Math.round((this.stats.firstAttemptCorrect / answeredCount) * 100) : 0;

    this.scorePercentage.textContent = `${pct}%`;
    this.streakCount.textContent = this.stats.streak;

    const progressPct = total > 0 ? ((this.currentIndex) / total) * 100 : 0;
    this.progressBarFill.style.width = `${Math.max(progressPct, 1)}%`;
  }

  showResults() {
    this.quizCard.style.display = "none";
    this.resultsCard.style.display = "block";

    const total = this.activeQuestions.length;
    const finalPct = total > 0 ? Math.round((this.stats.firstAttemptCorrect / total) * 100) : 0;

    this.finalScorePercent.textContent = `${finalPct}%`;
    this.statTotal.textContent = total;
    this.statFirstCorrect.textContent = this.stats.firstAttemptCorrect;
    this.statMinorVariations.textContent = this.stats.minorVariations;
    this.statIncorrect.textContent = this.stats.incorrect;

    if (this.stats.missedQuestions.length > 0) {
      this.missedSection.style.display = "block";
      this.btnReviewMissed.style.display = "inline-flex";
      this.missedList.innerHTML = "";

      this.stats.missedQuestions.forEach((q, idx) => {
        const item = document.createElement("div");
        item.className = "missed-item";

        let correctLabel = "";
        if (q.type === "multiple_choice") {
          correctLabel = q.options.find(o => o.startsWith(q.correctAnswer)) || q.correctAnswer;
        } else if (q.type === "true_false") {
          correctLabel = q.correctAnswer ? "TRUE" : "FALSE";
        } else {
          correctLabel = q.canonicalAnswer;
        }

        item.innerHTML = `
          <div class="q-title">${idx + 1}. [Lesson ${q.lesson} - ${q.type.replace('_', ' ').toUpperCase()}] ${q.question}</div>
          <div class="canonical-ans"><strong>Answer:</strong> ${correctLabel}</div>
          <p style="margin-top: 4px; color: var(--text-muted); font-size: 0.85rem;">${q.explanation}</p>
        `;
        this.missedList.appendChild(item);
      });
    } else {
      this.missedSection.style.display = "none";
      this.btnReviewMissed.style.display = "none";
    }
  }
}

// Initialize on DOMContentLoaded
document.addEventListener("DOMContentLoaded", () => {
  window.app = new QuizApp();
});
