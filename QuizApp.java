import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.text.Normalizer;
import java.util.*;
import java.util.regex.*;

/**
 * Standalone Java Quiz Runner & Validation Engine
 * Art Appreciation (Lessons 1 - 4)
 * Grounded 100% in course materials.
 */
public class QuizApp {

    static class Question {
        int id;
        int lesson;
        String lessonTitle;
        String type; // "multiple_choice", "identification", "true_false"
        String question;
        List<String> options = new ArrayList<>();
        String correctAnswer;
        boolean correctBool;
        String canonicalAnswer;
        List<String> acceptedAlternatives = new ArrayList<>();
        List<String> acceptedVariations = new ArrayList<>();
        List<String> requiredKeywords = new ArrayList<>();
        List<NearMiss> nearMisses = new ArrayList<>();
        String distinction = "";
        String explanation = "";
    }

    static class NearMiss {
        String term;
        String reason;

        NearMiss(String term, String reason) {
            this.term = term;
            this.reason = reason;
        }
    }

    static class ValidationResult {
        String classification;
        boolean isCorrect;
        String canonical;
        String explanation;
        String distinction;
        String matchedNearMiss;

        ValidationResult(String classification, boolean isCorrect, String canonical, String explanation, String distinction) {
            this.classification = classification;
            this.isCorrect = isCorrect;
            this.canonical = canonical;
            this.explanation = explanation;
            this.distinction = distinction;
        }
    }

    // --- Normalization & Distance Algorithms ---

    public static String normalizeText(String input) {
        if (input == null) return "";
        String s = Normalizer.normalize(input, Normalizer.Form.NFD);
        s = s.replaceAll("\\p{M}", ""); // Strip diacritics
        s = s.toLowerCase();
        s = s.replaceAll("[“”]", "\"").replaceAll("[‘’]", "'").replaceAll("[–—]", "-");
        s = s.replaceAll("[^a-z0-9\\s\\-'/.]", " ");
        s = s.replaceAll("\\s+", " ").trim();
        s = s.replaceAll("[.,;:]+$", "");
        return s;
    }

    public static String stripArticles(String input) {
        return input.replaceFirst("^(the|a|an)\\s+", "").trim();
    }

    public static int levenshteinDistance(String s1, String s2) {
        int m = s1.length(), n = s2.length();
        int[][] d = new int[m + 1][n + 1];
        for (int i = 0; i <= m; i++) d[i][0] = i;
        for (int j = 0; j <= n; j++) d[0][j] = j;

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                int cost = s1.charAt(i - 1) == s2.charAt(j - 1) ? 0 : 1;
                d[i][j] = Math.min(
                    Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1),
                    d[i - 1][j - 1] + cost
                );
            }
        }
        return d[m][n];
    }

    public static boolean isFuzzyMatch(String u, String t) {
        String su = stripArticles(u);
        String st = stripArticles(t);
        if (su.equals(st)) return true;
        int dist = levenshteinDistance(su, st);
        int len = Math.max(su.length(), st.length());
        if (len <= 4) return dist == 0;
        if (len <= 8) return dist <= 1;
        return dist <= 2;
    }

    public static ValidationResult validateIdentification(String userResponse, Question q) {
        String raw = (userResponse != null) ? userResponse.trim() : "";
        if (raw.isEmpty()) {
            return new ValidationResult("INCORRECT", false, q.canonicalAnswer, "No answer provided.", q.distinction);
        }

        String normUser = normalizeText(raw);
        String cleanUser = stripArticles(normUser);

        String canonical = q.canonicalAnswer;
        String cleanCanonical = stripArticles(normalizeText(canonical));

        // Step 5: Check near-misses
        for (NearMiss nm : q.nearMisses) {
            String cleanNM = stripArticles(normalizeText(nm.term));
            if (cleanUser.equals(cleanNM) || isFuzzyMatch(cleanUser, cleanNM)) {
                ValidationResult vr = new ValidationResult(
                    "INCORRECT", false, canonical,
                    "Your answer refers to a related but distinct concept: " + nm.reason,
                    q.distinction
                );
                vr.matchedNearMiss = nm.term;
                return vr;
            }
        }

        List<String> allAccepted = new ArrayList<>();
        allAccepted.add(canonical);
        allAccepted.addAll(q.acceptedAlternatives);
        allAccepted.addAll(q.acceptedVariations);

        // Step 2: Exact and accepted equivalent matches
        for (String acc : allAccepted) {
            String cleanAcc = stripArticles(normalizeText(acc));
            if (cleanUser.equals(cleanAcc)) {
                boolean isExact = cleanUser.equals(cleanCanonical);
                return new ValidationResult(
                    isExact ? "CORRECT" : "CORRECT — MINOR VARIATION",
                    true, canonical,
                    isExact ? "Matches canonical answer." : "Accepted equivalent term for '" + canonical + "'.",
                    q.distinction
                );
            }
        }

        // Step 3: Check spelling / typographical errors
        for (String acc : allAccepted) {
            String cleanAcc = stripArticles(normalizeText(acc));
            if (isFuzzyMatch(cleanUser, cleanAcc)) {
                return new ValidationResult(
                    "CORRECT — MINOR VARIATION",
                    true, canonical,
                    "Correct (minor spelling variation detected). The standard term is '" + canonical + "'.",
                    q.distinction
                );
            }
        }

        // Step 4: Check required keywords
        if (!q.requiredKeywords.isEmpty()) {
            List<String> missing = new ArrayList<>();
            List<String> present = new ArrayList<>();
            for (String kw : q.requiredKeywords) {
                if (cleanUser.contains(normalizeText(kw))) {
                    present.add(kw);
                } else {
                    missing.add(kw);
                }
            }

            if (missing.isEmpty()) {
                return new ValidationResult(
                    "CORRECT — MINOR VARIATION", true, canonical,
                    "Correct! Conveys all essential concepts for '" + canonical + "'.",
                    q.distinction
                );
            } else if (!present.isEmpty() && q.requiredKeywords.size() > 1) {
                return new ValidationResult(
                    "PARTIALLY CORRECT", false, canonical,
                    "Partially correct. Missing essential component(s): " + String.join(", ", missing) + ".",
                    q.distinction
                );
            }
        }

        return new ValidationResult(
            "INCORRECT", false, canonical,
            "Incorrect. The required answer is '" + canonical + "'. " + q.explanation,
            q.distinction
        );
    }

    // Minimal JSON Parser for questions.json
    public static List<Question> loadQuestions(String jsonPath) throws Exception {
        String content = Files.readString(Paths.get(jsonPath), StandardCharsets.UTF_8);
        List<Question> list = new ArrayList<>();

        // Simple regex-based field extractor across JSON objects
        Pattern objPattern = Pattern.compile("\\{[^{}]+(?:\\{[^{}]*\\}[^{}]*)*\\}");
        Matcher matcher = Pattern.compile("\\{\\s*\"id\":\\s*(\\d+)[^\\}]+\\}", Pattern.DOTALL).matcher(content);

        // We can use a clean line-based scanner for questions.json since it is well formatted
        String[] blocks = content.split("\"id\":");
        for (int i = 1; i < blocks.length; i++) {
            String b = "\"id\":" + blocks[i];
            Question q = new Question();
            q.id = Integer.parseInt(extractValue(b, "\"id\":\\s*(\\d+)"));
            q.lesson = Integer.parseInt(extractValue(b, "\"lesson\":\\s*(\\d+)"));
            q.lessonTitle = extractString(b, "lessonTitle");
            q.type = extractString(b, "type");
            q.question = extractString(b, "question");
            q.explanation = extractString(b, "explanation");

            if ("multiple_choice".equals(q.type)) {
                q.correctAnswer = extractString(b, "correctAnswer");
                q.options = extractStringArray(b, "options");
            } else if ("true_false".equals(q.type)) {
                String cb = extractValue(b, "\"correctAnswer\":\\s*(true|false)");
                q.correctBool = Boolean.parseBoolean(cb);
            } else if ("identification".equals(q.type)) {
                q.canonicalAnswer = extractString(b, "canonicalAnswer");
                q.distinction = extractString(b, "distinction");
                q.acceptedAlternatives = extractStringArray(b, "acceptedAlternatives");
                q.acceptedVariations = extractStringArray(b, "acceptedVariations");
                q.requiredKeywords = extractStringArray(b, "requiredKeywords");

                // Near misses
                Pattern nmPat = Pattern.compile("\\{\\s*\"term\":\\s*\"([^\"]+)\",\\s*\"reason\":\\s*\"([^\"]+)\"\\s*\\}");
                Matcher nmMat = nmPat.matcher(b);
                while (nmMat.find()) {
                    q.nearMisses.add(new NearMiss(nmMat.group(1), nmMat.group(2)));
                }
            }
            list.add(q);
        }
        return list;
    }

    private static String extractValue(String block, String regex) {
        Matcher m = Pattern.compile(regex).matcher(block);
        return m.find() ? m.group(1).trim() : "";
    }

    private static String extractString(String block, String key) {
        Matcher m = Pattern.compile("\"" + key + "\":\\s*\"(.*?)\"(?:,|\\n|\\r)", Pattern.DOTALL).matcher(block);
        return m.find() ? m.group(1).replace("\\\"", "\"").replace("\\n", " ").trim() : "";
    }

    private static List<String> extractStringArray(String block, String key) {
        List<String> result = new ArrayList<>();
        Matcher m = Pattern.compile("\"" + key + "\":\\s*\\[(.*?)\\]", Pattern.DOTALL).matcher(block);
        if (m.find()) {
            String inner = m.group(1);
            Matcher strM = Pattern.compile("\"(.*?)\"").matcher(inner);
            while (strM.find()) {
                result.add(strM.group(1).replace("\\\"", "\"").trim());
            }
        }
        return result;
    }

    // --- Main Interactive Terminal Runner ---

    public static void main(String[] args) {
        System.out.println("===============================================================");
        System.out.println("  ART APPRECIATION - 100-QUESTION EXAMINER & VALIDATION ENGINE");
        System.out.println("  Grounded Strictly in Lessons 1 to 4 Source Materials");
        System.out.println("===============================================================\n");

        List<Question> questions;
        try {
            questions = loadQuestions("questions.json");
            System.out.println("Loaded " + questions.size() + " verified questions successfully!\n");
        } catch (Exception e) {
            System.err.println("Could not load questions.json: " + e.getMessage());
            return;
        }

        Scanner scanner = new Scanner(System.in, StandardCharsets.UTF_8);

        int total = questions.size();
        int firstAttemptCorrect = 0;
        int minorVariations = 0;
        int incorrect = 0;

        for (int i = 0; i < total; i++) {
            Question q = questions.get(i);
            System.out.println("---------------------------------------------------------------");
            System.out.println("Question " + (i + 1) + " of " + total + " [" + q.lessonTitle + " | " + q.type.toUpperCase() + "]");
            System.out.println("Q: " + q.question);

            boolean isCorrect = false;
            String classification = "";

            if ("multiple_choice".equals(q.type)) {
                for (String opt : q.options) {
                    System.out.println("   " + opt);
                }
                System.out.print("\nYour choice (A, B, C, D): ");
                if (!scanner.hasNextLine()) break;
                String input = scanner.nextLine().trim().toUpperCase();
                isCorrect = input.equals(q.correctAnswer.toUpperCase());
                classification = isCorrect ? "CORRECT" : "INCORRECT";

                System.out.println("\n[RESULT] " + classification);
                System.out.println("Correct Answer: " + q.correctAnswer);
                System.out.println("Explanation: " + q.explanation);

            } else if ("true_false".equals(q.type)) {
                System.out.print("\nYour answer (T/True or F/False): ");
                if (!scanner.hasNextLine()) break;
                String input = scanner.nextLine().trim().toLowerCase();
                boolean userBool = input.startsWith("t") || input.equals("1");
                isCorrect = (userBool == q.correctBool);
                classification = isCorrect ? "CORRECT" : "INCORRECT";

                System.out.println("\n[RESULT] " + classification);
                System.out.println("Correct Truth Value: " + (q.correctBool ? "TRUE" : "FALSE"));
                System.out.println("Explanation: " + q.explanation);

            } else if ("identification".equals(q.type)) {
                System.out.print("\nYour answer: ");
                if (!scanner.hasNextLine()) break;
                String input = scanner.nextLine().trim();

                ValidationResult vr = validateIdentification(input, q);
                isCorrect = vr.isCorrect;
                classification = vr.classification;

                System.out.println("\n[RESULT] " + vr.classification);
                System.out.println("Canonical Answer: " + vr.canonical);
                if (vr.distinction != null && !vr.distinction.isEmpty()) {
                    System.out.println("Concept Distinction: " + vr.distinction);
                }
                if (!q.acceptedAlternatives.isEmpty()) {
                    System.out.println("Accepted Alternatives: " + String.join(", ", q.acceptedAlternatives));
                }
                System.out.println("Explanation: " + vr.explanation);
            }

            if (isCorrect) {
                firstAttemptCorrect++;
                if (classification.contains("MINOR VARIATION")) {
                    minorVariations++;
                }
            } else {
                incorrect++;
            }

            double currentScore = ((double) firstAttemptCorrect / (i + 1)) * 100.0;
            System.out.printf("Current Score: %.1f%% (%d correct out of %d)\n\n", currentScore, firstAttemptCorrect, (i + 1));
        }

        System.out.println("===============================================================");
        System.out.println("                       QUIZ COMPLETED!");
        System.out.println("===============================================================");
        double finalScore = ((double) firstAttemptCorrect / total) * 100.0;
        System.out.printf("Final First-Attempt Score: %.1f%%\n", finalScore);
        System.out.println("Total Questions: " + total);
        System.out.println("First-Attempt Correct: " + firstAttemptCorrect);
        System.out.println("Accepted Minor Variations: " + minorVariations);
        System.out.println("Incorrect: " + incorrect);
        System.out.println("===============================================================");
    }
}
