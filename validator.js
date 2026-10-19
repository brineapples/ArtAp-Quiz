/**
 * Identification Answer Validation Engine
 * Implements the 8-Step Validation Pipeline specified in the requirements.
 */

function normalizeText(text) {
  if (!text) return "";
  return text
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "") // Remove diacritics / accents
    .toLowerCase()
    .replace(/[“”]/g, '"')
    .replace(/[‘’]/g, "'")
    .replace(/[–—]/g, "-")
    .replace(/[^\w\s\-'/.]/g, " ") // Keep alphanumeric, hyphens, slashes, periods
    .replace(/\s+/g, " ")
    .trim()
    .replace(/[.,;:]+$/, ""); // Remove trailing punctuation
}

function stripArticles(text) {
  return text.replace(/^(the|a|an)\s+/i, "").trim();
}

function levenshteinDistance(s1, s2) {
  const m = s1.length;
  const n = s2.length;
  const d = [];

  for (let i = 0; i <= m; i++) {
    d[i] = [i];
  }
  for (let j = 0; j <= n; j++) {
    d[0][j] = j;
  }

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      const cost = s1[i - 1] === s2[j - 1] ? 0 : 1;
      d[i][j] = Math.min(
        d[i - 1][j] + 1,      // deletion
        d[i][j - 1] + 1,      // insertion
        d[i - 1][j - 1] + cost // substitution
      );
    }
  }
  return d[m][n];
}

function isFuzzyMatch(userNorm, targetNorm) {
  const u = stripArticles(userNorm);
  const t = stripArticles(targetNorm);

  if (u === t) return { match: true, distance: 0 };

  const dist = levenshteinDistance(u, t);
  const len = Math.max(u.length, t.length);

  // For very short terms (<= 4 chars, like "hue", "line", "form", "ink"), require exact match (0 distance)
  if (len <= 4) {
    return { match: dist === 0, distance: dist };
  }
  // Medium terms (5 to 8 chars, like "pencil", "rhythm", "fresco") allow max 1 typo
  if (len <= 8) {
    return { match: dist <= 1, distance: dist };
  }
  // Long terms (>= 9 chars, like "chiaroscuro", "calligraphy", "encaustic") allow up to 2 typos
  return { match: dist <= 2, distance: dist };
}

function validateIdentification(userResponse, question) {
  const rawResponse = (userResponse || "").trim();
  if (!rawResponse) {
    return {
      classification: "INCORRECT",
      isCorrect: false,
      userResponse: rawResponse,
      canonicalAnswer: question.canonicalAnswer,
      explanation: "No answer was provided.",
      distinction: question.distinction || "",
      acceptedAlternatives: question.acceptedAlternatives || []
    };
  }

  // Step 1: Normalize
  const normUser = normalizeText(rawResponse);
  const cleanUser = stripArticles(normUser);

  const canonical = question.canonicalAnswer;
  const normCanonical = normalizeText(canonical);
  const cleanCanonical = stripArticles(normCanonical);

  const allAccepted = [
    canonical,
    ...(question.acceptedAlternatives || []),
    ...(question.acceptedVariations || [])
  ];

  // Step 5 Check First: Detect near-misses and known confused concepts
  if (question.nearMisses && question.nearMisses.length > 0) {
    for (const nm of question.nearMisses) {
      const normNM = normalizeText(nm.term);
      const cleanNM = stripArticles(normNM);
      const fuzzy = isFuzzyMatch(cleanUser, cleanNM);
      if (cleanUser === cleanNM || (fuzzy.match && fuzzy.distance <= 1)) {
        return {
          classification: "INCORRECT",
          subType: "NEAR_MISS",
          isCorrect: false,
          userResponse: rawResponse,
          canonicalAnswer: canonical,
          matchedNearMiss: nm.term,
          explanation: `Your answer '${rawResponse}' refers to a related but distinct concept. ${nm.reason}`,
          distinction: question.distinction || "",
          acceptedAlternatives: question.acceptedAlternatives || []
        };
      }
    }
  }

  // Step 2: Check exact and accepted equivalent matches
  for (const acc of allAccepted) {
    const normAcc = normalizeText(acc);
    const cleanAcc = stripArticles(normAcc);
    if (cleanUser === cleanAcc) {
      const isExactCanonical = (cleanUser === cleanCanonical);
      return {
        classification: isExactCanonical ? "CORRECT" : "CORRECT — MINOR VARIATION",
        isCorrect: true,
        userResponse: rawResponse,
        canonicalAnswer: canonical,
        explanation: `Correct! ${isExactCanonical ? 'Matches canonical answer.' : `Accepted equivalent term for '${canonical}'.`}`,
        distinction: question.distinction || "",
        acceptedAlternatives: question.acceptedAlternatives || []
      };
    }
  }

  // Step 3: Check spelling and typographical errors
  for (const acc of allAccepted) {
    const normAcc = normalizeText(acc);
    const cleanAcc = stripArticles(normAcc);
    const fuzzy = isFuzzyMatch(cleanUser, cleanAcc);
    if (fuzzy.match) {
      return {
        classification: "CORRECT — MINOR VARIATION",
        isCorrect: true,
        userResponse: rawResponse,
        canonicalAnswer: canonical,
        explanation: `Correct (minor spelling variation detected). The standard term is '${canonical}'.`,
        distinction: question.distinction || "",
        acceptedAlternatives: question.acceptedAlternatives || []
      };
    }
  }

  // Step 4: Validate meaning and essential concepts / keywords
  if (question.requiredKeywords && question.requiredKeywords.length > 0) {
    const missing = question.requiredKeywords.filter(
      kw => !cleanUser.includes(normalizeText(kw))
    );
    const present = question.requiredKeywords.filter(
      kw => cleanUser.includes(normalizeText(kw))
    );

    if (missing.length === 0) {
      // All required keywords are present
      return {
        classification: "CORRECT — MINOR VARIATION",
        isCorrect: true,
        userResponse: rawResponse,
        canonicalAnswer: canonical,
        explanation: `Correct! Conveys all essential concepts for '${canonical}'.`,
        distinction: question.distinction || "",
        acceptedAlternatives: question.acceptedAlternatives || []
      };
    } else if (present.length > 0 && question.requiredKeywords.length > 1) {
      // Partial credit criteria: some required keywords present but not all
      return {
        classification: "PARTIALLY CORRECT",
        isCorrect: false,
        userResponse: rawResponse,
        canonicalAnswer: canonical,
        explanation: `Partially correct. Missing key concept component(s): ${missing.join(", ")}.`,
        distinction: question.distinction || "",
        acceptedAlternatives: question.acceptedAlternatives || []
      };
    }
  }

  // Step 6: Final Incorrect Assignment
  return {
    classification: "INCORRECT",
    isCorrect: false,
    userResponse: rawResponse,
    canonicalAnswer: canonical,
    explanation: `Incorrect. The required answer is '${canonical}'. ${question.explanation || ""}`,
    distinction: question.distinction || "",
    acceptedAlternatives: question.acceptedAlternatives || []
  };
}

// Validator for Multiple Choice
function validateMultipleChoice(userOptionLetter, question) {
  const chosen = (userOptionLetter || "").trim().toUpperCase();
  const correct = (question.correctAnswer || "").trim().toUpperCase();
  const isCorrect = chosen === correct;

  return {
    classification: isCorrect ? "CORRECT" : "INCORRECT",
    isCorrect: isCorrect,
    selectedOption: chosen,
    correctAnswer: correct,
    explanation: question.explanation
  };
}

// Validator for True or False
function validateTrueFalse(userBool, question) {
  const userVal = Boolean(userBool);
  const correctVal = Boolean(question.correctAnswer);
  const isCorrect = userVal === correctVal;

  return {
    classification: isCorrect ? "CORRECT" : "INCORRECT",
    isCorrect: isCorrect,
    userAnswer: userVal,
    correctAnswer: correctVal,
    explanation: question.explanation
  };
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = {
    normalizeText,
    stripArticles,
    levenshteinDistance,
    isFuzzyMatch,
    validateIdentification,
    validateMultipleChoice,
    validateTrueFalse
  };
}
