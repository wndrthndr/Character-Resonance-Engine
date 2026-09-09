import random

from engine.ranking_engine import RankingEngine
from data.characters import CHARACTER_REGISTRY


# ============================================================
# CONFIG
# ============================================================

NOISE_LEVEL = 0.05
ROBUSTNESS_RUNS = 25
RANDOM_SEED = 42


# ============================================================
# EXACT CHARACTER PROFILES
# ============================================================

TEST_PROFILES = [
    {
        "expected": "Batman",
        "franchise": "dc",
        "vector": [
            0.92, 1.00, 0.54, 0.94,
            0.46, 0.72, 0.96, 1.00,
            0.26, 0.84, 0.98, 0.48
        ],
    },
    {
        "expected": "Superman",
        "franchise": "dc",
        "vector": [
            0.98, 0.76, 1.00, 1.00,
            0.24, 0.54, 0.98, 0.92,
            0.54, 0.52, 0.76, 0.10
        ],
    },
    {
        "expected": "Toph",
        "franchise": "atla",
        "vector": [
            0.96, 0.76, 0.48, 0.64,
            0.42, 0.86, 0.62, 0.74,
            0.68, 0.92, 0.80, 0.98
        ],
    },
    {
        "expected": "Po",
        "franchise": "kung_fu_panda",
        "vector": [
            0.94, 0.54, 0.94, 0.90,
            0.34, 0.88, 0.96, 0.72,
            1.00, 0.76, 0.60, 0.34
        ],
    },
]


# ============================================================
# CONFUSION / MIDPOINT PAIRS
#
# The midpoint between two character profiles should normally
# still produce one of those two characters as the top result.
# ============================================================

CONFUSION_PAIRS = [
    {
        "franchise": "dc",
        "character_a": "Batman",
        "vector_a": [
            0.92, 1.00, 0.54, 0.94,
            0.46, 0.72, 0.96, 1.00,
            0.26, 0.84, 0.98, 0.48
        ],
        "character_b": "Superman",
        "vector_b": [
            0.98, 0.76, 1.00, 1.00,
            0.24, 0.54, 0.98, 0.92,
            0.54, 0.52, 0.76, 0.10
        ],
    },
    {
        "franchise": "atla",
        "character_a": "Toph",
        "vector_a": [
            0.96, 0.76, 0.48, 0.64,
            0.42, 0.86, 0.62, 0.74,
            0.68, 0.92, 0.80, 0.98
        ],
        "character_b": "Zuko",
        "vector_b": [
            0.92, 0.64, 0.74, 0.86,
            0.72, 0.34, 0.96, 0.92,
            0.22, 0.42, 0.72, 0.74
        ],
    },
    {
        "franchise": "kung_fu_panda",
        "character_a": "Po",
        "vector_a": [
            0.94, 0.54, 0.94, 0.90,
            0.34, 0.88, 0.96, 0.72,
            1.00, 0.76, 0.60, 0.34
        ],
        "character_b": "Monkey",
        "vector_b": [
            0.90, 0.72, 0.74, 0.78,
            0.42, 0.86, 0.94, 0.82,
            0.90, 0.82, 0.70, 0.48
        ],
    },
]


# ============================================================
# BASIC SELF-RANKING TEST
# ============================================================

def run_test(test):
    expected = test["expected"]
    franchise = test["franchise"]
    vector = test["vector"]

    candidates = CHARACTER_REGISTRY.get(franchise, [])

    if not candidates:
        return {
            "expected": expected,
            "predicted": "NO CANDIDATES",
            "score": None,
            "correct": False,
        }

    rankings = RankingEngine.rank_characters(
        user_vector=vector,
        candidates=candidates,
    )

    if not rankings:
        return {
            "expected": expected,
            "predicted": "NO RESULT",
            "score": None,
            "correct": False,
        }

    predicted = rankings[0]["name"]

    return {
        "expected": expected,
        "predicted": predicted,
        "score": rankings[0]["score"],
        "correct": predicted.lower() == expected.lower(),
    }


# ============================================================
# ADD RANDOM NOISE
# ============================================================

def add_noise(vector, noise_level=NOISE_LEVEL):
    noisy_vector = []

    for value in vector:
        noise = random.uniform(
            -noise_level,
            noise_level
        )

        noisy_value = value + noise

        # Keep values inside the valid 0-1 range.
        noisy_value = max(
            0.0,
            min(1.0, noisy_value)
        )

        noisy_vector.append(noisy_value)

    return noisy_vector


# ============================================================
# ROBUSTNESS TEST
# ============================================================

def run_robustness_test(test):
    expected = test["expected"]
    franchise = test["franchise"]
    original_vector = test["vector"]

    candidates = CHARACTER_REGISTRY.get(franchise, [])

    if not candidates:
        return {
            "expected": expected,
            "passed": 0,
            "total": ROBUSTNESS_RUNS,
        }

    passed = 0

    for _ in range(ROBUSTNESS_RUNS):

        noisy_vector = add_noise(
            original_vector
        )

        rankings = RankingEngine.rank_characters(
            user_vector=noisy_vector,
            candidates=candidates,
        )

        if not rankings:
            continue

        predicted = rankings[0]["name"]

        if predicted.lower() == expected.lower():
            passed += 1

    return {
        "expected": expected,
        "passed": passed,
        "total": ROBUSTNESS_RUNS,
    }


# ============================================================
# CREATE MIDPOINT VECTOR
# ============================================================

def midpoint(vector_a, vector_b):
    return [
        (a + b) / 2
        for a, b in zip(vector_a, vector_b)
    ]


# ============================================================
# CONFUSION TEST
# ============================================================

def run_confusion_test(test):
    franchise = test["franchise"]
    character_a = test["character_a"]
    character_b = test["character_b"]

    vector = midpoint(
        test["vector_a"],
        test["vector_b"],
    )

    candidates = CHARACTER_REGISTRY.get(
        franchise,
        []
    )

    if not candidates:
        return {
            "character_a": character_a,
            "character_b": character_b,
            "predicted": "NO CANDIDATES",
            "valid": False,
        }

    rankings = RankingEngine.rank_characters(
        user_vector=vector,
        candidates=candidates,
    )

    if not rankings:
        return {
            "character_a": character_a,
            "character_b": character_b,
            "predicted": "NO RESULT",
            "valid": False,
        }

    predicted = rankings[0]["name"]

    valid = predicted.lower() in {
        character_a.lower(),
        character_b.lower(),
    }

    return {
        "character_a": character_a,
        "character_b": character_b,
        "predicted": predicted,
        "score": rankings[0]["score"],
        "valid": valid,
    }


# ============================================================
# MAIN
# ============================================================

def main():

    random.seed(RANDOM_SEED)

    # ========================================================
    # 1. BASIC SELF-RANKING
    # ========================================================

    print()
    print("=" * 60)
    print("        CHARACTER MATCHING EVALUATION")
    print("=" * 60)
    print()

    results = []

    for test in TEST_PROFILES:

        result = run_test(test)

        results.append(result)

        status = (
            "PASS"
            if result["correct"]
            else "FAIL"
        )

        print(
            f"{status:<6}"
            f"{result['expected']:<15}"
            f"-> {result['predicted']:<15}"
            f"Score: {result.get('score', '-')}"
        )

    total = len(results)

    passed = sum(
        result["correct"]
        for result in results
    )

    accuracy = (
        passed / total * 100
        if total
        else 0
    )

    print()
    print("-" * 60)
    print(f"Tests:       {total}")
    print(f"Passed:      {passed}")
    print(f"Failed:      {total - passed}")
    print(f"Accuracy:    {accuracy:.1f}%")
    print("-" * 60)


    # ========================================================
    # 2. ROBUSTNESS TEST
    # ========================================================

    print()
    print("=" * 60)
    print("             ROBUSTNESS TEST")
    print("=" * 60)
    print()

    print(
        f"Noise level: ±{NOISE_LEVEL}"
    )

    print(
        f"Runs per character: {ROBUSTNESS_RUNS}"
    )

    print(
        f"Random seed: {RANDOM_SEED}"
    )

    print()

    robustness_results = []

    for test in TEST_PROFILES:

        result = run_robustness_test(test)

        robustness_results.append(result)

        percentage = (
            result["passed"]
            / result["total"]
            * 100
            if result["total"]
            else 0
        )

        status = (
            "PASS"
            if result["passed"] == result["total"]
            else "CHECK"
        )

        print(
            f"{status:<7}"
            f"{result['expected']:<15}"
            f"{result['passed']:>2}"
            f"/{result['total']:<3}"
            f" ({percentage:.1f}%)"
        )

    total_runs = sum(
        result["total"]
        for result in robustness_results
    )

    total_passed = sum(
        result["passed"]
        for result in robustness_results
    )

    overall_robustness = (
        total_passed
        / total_runs
        * 100
        if total_runs
        else 0
    )

    print()
    print("-" * 60)
    print(f"Robustness runs: {total_runs}")
    print(f"Correct:         {total_passed}")
    print(f"Incorrect:       {total_runs - total_passed}")
    print(f"Robustness:      {overall_robustness:.1f}%")
    print("-" * 60)


    # ========================================================
    # 3. CONFUSION / MIDPOINT TEST
    # ========================================================

    print()
    print("=" * 60)
    print("             CONFUSION TEST")
    print("=" * 60)
    print()

    confusion_results = []

    for test in CONFUSION_PAIRS:

        result = run_confusion_test(test)

        confusion_results.append(result)

        status = (
            "PASS"
            if result["valid"]
            else "CHECK"
        )

        pair = (
            f"{result['character_a']}"
            f" / "
            f"{result['character_b']}"
        )

        print(
            f"{status:<7}"
            f"{pair:<25}"
            f"-> {result['predicted']:<15}"
            f"Score: {result.get('score', '-')}"
        )

    confusion_total = len(
        confusion_results
    )

    confusion_passed = sum(
        result["valid"]
        for result in confusion_results
    )

    confusion_accuracy = (
        confusion_passed
        / confusion_total
        * 100
        if confusion_total
        else 0
    )

    print()
    print("-" * 60)
    print(
        f"Pairs tested: {confusion_total}"
    )
    print(
        f"Valid results: {confusion_passed}"
    )
    print(
        f"Unexpected:    "
        f"{confusion_total - confusion_passed}"
    )
    print(
        f"Confusion score: "
        f"{confusion_accuracy:.1f}%"
    )
    print("-" * 60)
    print()


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()