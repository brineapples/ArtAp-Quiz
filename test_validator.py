import json
from validator import validate_identification

with open('questions.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

q2 = next(q for q in qs if q['id'] == 2)
q39 = next(q for q in qs if q['id'] == 39)
q98 = next(q for q in qs if q['id'] == 98)

tests = [
    (q2, 'Understanding Context', 'CORRECT'),
    (q2, '   context   ', 'CORRECT — MINOR VARIATION'),
    (q2, 'Interpreting Meaning', 'INCORRECT'),
    (q39, 'chiaroscuro', 'CORRECT'),
    (q39, 'chiarscuro', 'CORRECT — MINOR VARIATION'),
    (q39, 'sfumato', 'INCORRECT'),
    (q98, 'lost-wax technique', 'CORRECT — MINOR VARIATION'),
    (q98, 'lost wax', 'CORRECT — MINOR VARIATION'),
    (q98, 'wax', 'PARTIALLY CORRECT'),
    (q98, 'random answer', 'INCORRECT')
]

all_passed = True
for q, ans, exp in tests:
    res = validate_identification(ans, q)
    c = res["classification"]
    matched = (c == exp)
    if not matched:
        all_passed = False
    print(f"[{'PASS' if matched else 'FAIL'}] Input: {ans!r:25} -> Result: {c:25} (Expected: {exp})")
    if res.get("sub_type") == "NEAR_MISS":
        print(f"      Near miss caught: {res['matched_near_miss']} | {res['explanation']}")

if all_passed:
    print("\nALL 10 VALIDATION TEST CASES PASSED PERFECTLY!")
else:
    print("\nSome tests differed.")
