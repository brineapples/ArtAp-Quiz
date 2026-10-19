import unicodedata
import re

def normalize_text(text):
    if not text:
        return ""
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    text = text.lower()
    text = re.sub(r'[“”]', '"', text)
    text = re.sub(r'[‘’]', "'", text)
    text = re.sub(r'[–—]', "-", text)
    text = re.sub(r'[^\w\s\-\'/\.]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'[.,;:]+$', '', text)
    return text

def strip_articles(text):
    return re.sub(r'^(the|a|an)\s+', '', text, flags=re.IGNORECASE).strip()

def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    d = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        d[i][0] = i
    for j in range(n + 1):
        d[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            d[i][j] = min(
                d[i - 1][j] + 1,
                d[i][j - 1] + 1,
                d[i - 1][j - 1] + cost
            )
    return d[m][n]

def is_fuzzy_match(user_norm, target_norm):
    u = strip_articles(user_norm)
    t = strip_articles(target_norm)
    if u == t:
        return True, 0
    dist = levenshtein_distance(u, t)
    length = max(len(u), len(t))
    if length <= 4:
        return dist == 0, dist
    if length <= 8:
        return dist <= 1, dist
    return dist <= 2, dist

def validate_identification(user_response, question):
    raw_response = (user_response or "").strip()
    if not raw_response:
        return {
            "classification": "INCORRECT",
            "is_correct": False,
            "user_response": raw_response,
            "canonical_answer": question["canonicalAnswer"],
            "explanation": "No answer was provided.",
            "distinction": question.get("distinction", ""),
            "accepted_alternatives": question.get("acceptedAlternatives", [])
        }

    norm_user = normalize_text(raw_response)
    clean_user = strip_articles(norm_user)

    canonical = question["canonicalAnswer"]
    clean_canonical = strip_articles(normalize_text(canonical))

    all_accepted = [canonical] + question.get("acceptedAlternatives", []) + question.get("acceptedVariations", [])

    # Step 5: Check near-misses
    for nm in question.get("nearMisses", []):
        clean_nm = strip_articles(normalize_text(nm["term"]))
        matched, dist = is_fuzzy_match(clean_user, clean_nm)
        if clean_user == clean_nm or (matched and dist <= 1):
            return {
                "classification": "INCORRECT",
                "sub_type": "NEAR_MISS",
                "is_correct": False,
                "user_response": raw_response,
                "canonical_answer": canonical,
                "matched_near_miss": nm["term"],
                "explanation": f"Your answer '{raw_response}' refers to a related but distinct concept. {nm['reason']}",
                "distinction": question.get("distinction", ""),
                "accepted_alternatives": question.get("acceptedAlternatives", [])
            }

    # Step 2: Check exact and accepted equivalent matches
    for acc in all_accepted:
        clean_acc = strip_articles(normalize_text(acc))
        if clean_user == clean_acc:
            is_exact = (clean_user == clean_canonical)
            return {
                "classification": "CORRECT" if is_exact else "CORRECT — MINOR VARIATION",
                "is_correct": True,
                "user_response": raw_response,
                "canonical_answer": canonical,
                "explanation": "Correct! Matches canonical answer." if is_exact else f"Accepted equivalent term for '{canonical}'.",
                "distinction": question.get("distinction", ""),
                "accepted_alternatives": question.get("acceptedAlternatives", [])
            }

    # Step 3: Check spelling / typographical errors
    for acc in all_accepted:
        clean_acc = strip_articles(normalize_text(acc))
        matched, dist = is_fuzzy_match(clean_user, clean_acc)
        if matched:
            return {
                "classification": "CORRECT — MINOR VARIATION",
                "is_correct": True,
                "user_response": raw_response,
                "canonical_answer": canonical,
                "explanation": f"Correct (minor spelling variation detected). The standard term is '{canonical}'.",
                "distinction": question.get("distinction", ""),
                "accepted_alternatives": question.get("acceptedAlternatives", [])
            }

    # Step 4: Check required keywords
    req_keywords = question.get("requiredKeywords", [])
    if req_keywords:
        missing = [kw for kw in req_keywords if normalize_text(kw) not in clean_user]
        present = [kw for kw in req_keywords if normalize_text(kw) in clean_user]
        if not missing:
            return {
                "classification": "CORRECT — MINOR VARIATION",
                "is_correct": True,
                "user_response": raw_response,
                "canonical_answer": canonical,
                "explanation": f"Correct! Conveys all essential concepts for '{canonical}'.",
                "distinction": question.get("distinction", ""),
                "accepted_alternatives": question.get("acceptedAlternatives", [])
            }
        elif present and len(req_keywords) > 1:
            return {
                "classification": "PARTIALLY CORRECT",
                "is_correct": False,
                "user_response": raw_response,
                "canonical_answer": canonical,
                "explanation": f"Partially correct. Missing essential component(s): {', '.join(missing)}.",
                "distinction": question.get("distinction", ""),
                "accepted_alternatives": question.get("acceptedAlternatives", [])
            }

    # Step 6: Incorrect
    return {
        "classification": "INCORRECT",
        "is_correct": False,
        "user_response": raw_response,
        "canonical_answer": canonical,
        "explanation": f"Incorrect. The required answer is '{canonical}'. {question.get('explanation', '')}",
        "distinction": question.get("distinction", ""),
        "accepted_alternatives": question.get("acceptedAlternatives", [])
    }
