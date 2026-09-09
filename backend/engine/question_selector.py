from typing import List, Optional
import random
import math

from models import CompactQuestion, VectorCharacterProfile
from data.behavior_profiles import BEHAVIOR_PROFILES
from engine.ranking_engine import RankingEngine


class QuestionSelector:
    """
    Adaptive question selector.

    Architecture
    ------------

    The quiz is divided into three phases:

        1. EXPLORATION
           Questions 1-4
           Broad personality coverage.

           IMPORTANT:
           The user's answers do NOT influence which
           questions are selected during this phase.

           Instead, the selector tries to cover different
           personality dimensions across the first four
           questions.

        2. DISCOVERY
           Questions 5-6
           Start using the user's personality evidence and
           character discrimination.

        3. REFINEMENT
           Questions 7+
           Focus on unresolved differences between
           remaining characters.

    The goal is to avoid this feedback loop:

        Q1 answer
          ↓
        Character A becomes #1
          ↓
        Q2 selected because it favors A
          ↓
        Character A becomes even stronger
          ↓
        Q3 selected around A
          ↓
        Character A dominates

    Instead:

        Q1-Q4 = independent exploration
        Q5-Q6 = light adaptation
        Q7+   = strong adaptation
    """

    # ==========================================================
    # CONFIGURATION
    # ==========================================================

    EXPLORATION_END = 4
    DISCOVERY_END = 6

    # Number of candidates used during refinement.
    REFINEMENT_CANDIDATES = 10

    # Randomness prevents identical question paths.
    RANDOM_WEIGHT = 0.20

    # Prevents one trait from dominating question selection.
    MAX_TRAIT_WEIGHT = 1.0

    # Number of personality dimensions.
    NUM_TRAITS = 12

    # ==========================================================
    # MAIN SELECTOR
    # ==========================================================

    @classmethod
    def select_next(
        cls,
        user_vector: List[float],
        answered_questions: List[str],
        question_pool: List[CompactQuestion],
        candidates: List[VectorCharacterProfile]
    ) -> Optional[CompactQuestion]:

        remaining = [
            question
            for question in question_pool
            if question.id not in answered_questions
        ]

        if not remaining:
            return None

        questions_answered = len(
            answered_questions
        )

        # ------------------------------------------------------
        # PHASE 1
        #
        # Questions 1-4.
        #
        # IMPORTANT:
        # The user's selected answers are NOT used to determine
        # the question path.
        #
        # We only look at which personality dimensions have
        # already been tested by previous QUESTIONS.
        # ------------------------------------------------------

        if questions_answered < cls.EXPLORATION_END:

            return cls._select_exploration_question(
                remaining=remaining,
                answered_questions=answered_questions,
                question_pool=question_pool
            )

        # ------------------------------------------------------
        # PHASE 2
        #
        # Questions 5-6.
        #
        # Character discrimination begins.
        # ------------------------------------------------------

        if questions_answered < cls.DISCOVERY_END:

            return cls._select_discovery_question(
                remaining=remaining,
                user_vector=user_vector,
                candidates=candidates
            )

        # ------------------------------------------------------
        # PHASE 3
        #
        # Questions 7+.
        #
        # Refine the profile.
        # ------------------------------------------------------

        return cls._select_refinement_question(
            remaining=remaining,
            user_vector=user_vector,
            candidates=candidates
        )

    # ==========================================================
    # PHASE 1 — EXPLORATION
    # ==========================================================

    @classmethod
    def _select_exploration_question(
        cls,
        remaining: List[CompactQuestion],
        answered_questions: List[str],
        question_pool: List[CompactQuestion]
    ) -> CompactQuestion:
        """
        Select questions 1-4.

        The user's answers are deliberately ignored.

        Instead, the selector looks at which traits were already
        tested by previous questions and prefers questions that
        explore different personality dimensions.

        This makes the first four questions independent from
        the current character ranking.
        """

        # ------------------------------------------------------
        # Build a map of questions by ID.
        # ------------------------------------------------------

        question_map = {
            question.id: question
            for question in question_pool
        }

        # ------------------------------------------------------
        # Track which personality dimensions have already been
        # explored by previous QUESTIONS.
        #
        # IMPORTANT:
        #
        # We do NOT look at the selected option.
        #
        # If a question contains:
        #
        #     ACTION + BOLD
        #     ANALYTICAL + CURIOUS
        #
        # then the question contributes those dimensions to
        # exploration coverage regardless of what the user chose.
        # ------------------------------------------------------

        covered_traits = [
            0.0
        ] * cls.NUM_TRAITS

        for question_id in answered_questions:

            previous_question = question_map.get(
                question_id
            )

            if previous_question is None:
                continue

            previous_vector = cls._question_vector(
                previous_question
            )

            for i in range(
                min(
                    len(covered_traits),
                    len(previous_vector)
                )
            ):

                covered_traits[i] += abs(
                    previous_vector[i]
                )

        # ------------------------------------------------------
        # Score remaining questions.
        # ------------------------------------------------------

        scored = []

        for question in remaining:

            question_vector = cls._question_vector(
                question
            )

            # How much this question explores traits that
            # previous questions haven't explored much.
            coverage_score = (
                cls._exploration_coverage_score(
                    question_vector=question_vector,
                    covered_traits=covered_traits
                )
            )

            # How different the four answer options are.
            diversity = cls._option_diversity(
                question
            )

            # Final exploration score.
            #
            # Coverage is more important than option diversity.
            #
            # Randomness is intentionally small so that we still
            # get varied quizzes without losing personality coverage.
            score = (
                coverage_score * 0.70
                + diversity * 0.30
                + random.uniform(
                    0.0,
                    cls.RANDOM_WEIGHT
                )
            )

            scored.append(
                (
                    score,
                    question
                )
            )

        if not scored:
            return random.choice(
                remaining
            )

        scored.sort(
            key=lambda item: item[0],
            reverse=True
        )

        # ------------------------------------------------------
        # Don't always choose the mathematically best question.
        #
        # Choosing randomly among the top few gives us:
        #
        # - broad coverage
        # - different quiz paths
        # - less deterministic behavior
        # ------------------------------------------------------

        top_count = min(
            4,
            len(scored)
        )

        return random.choice(
            scored[:top_count]
        )[1]

    # ==========================================================
    # EXPLORATION COVERAGE
    # ==========================================================

    @staticmethod
    def _exploration_coverage_score(
        question_vector: List[float],
        covered_traits: List[float]
    ) -> float:
        """
        Rewards questions that explore personality dimensions
        that previous exploration questions have not covered much.

        Example:

            Previous questions heavily tested:
                ANALYTICAL
                CURIOUS

            Candidate question tests:
                CREATIVE
                EMPATHETIC

            -> high score

        Candidate question tests:
                ANALYTICAL
                CURIOUS

            -> lower score

        This is intentionally a SOFT preference rather than a
        hard rule. We don't want to force every question to use
        completely different traits.
        """

        if not question_vector:
            return 0.0

        score = 0.0
        total_strength = 0.0

        length = min(
            len(question_vector),
            len(covered_traits)
        )

        for i in range(length):

            strength = abs(
                question_vector[i]
            )

            if strength <= 0:
                continue

            # Traits that haven't appeared much receive a larger
            # novelty value.
            #
            # coverage = 0 -> novelty = 1
            # coverage = 1 -> novelty = 0.5
            # coverage = 2 -> novelty = 0.33
            novelty = 1.0 / (
                1.0 + covered_traits[i]
            )

            score += (
                strength * novelty
            )

            total_strength += strength

        if total_strength <= 0:
            return 0.0

        return min(
            score / total_strength,
            1.0
        )

    # ==========================================================
    # PHASE 2 — DISCOVERY
    # ==========================================================

    @classmethod
    def _select_discovery_question(
        cls,
        remaining: List[CompactQuestion],
        user_vector: List[float],
        candidates: List[VectorCharacterProfile]
    ) -> CompactQuestion:

        # If there are no candidates, fall back to random
        # selection rather than trying to perform character
        # discrimination.
        if not candidates:

            return random.choice(
                remaining
            )

        scored = []

        for question in remaining:

            # --------------------------------------------------
            # How differently could the possible answers affect
            # the current character rankings?
            # --------------------------------------------------

            discrimination = (
                cls._character_discrimination(
                    question=question,
                    user_vector=user_vector,
                    candidates=candidates
                )
            )

            # --------------------------------------------------
            # Prefer traits where the user currently has weak
            # evidence.
            # --------------------------------------------------

            coverage = cls._trait_coverage_score(
                question=question,
                user_vector=user_vector
            )

            # --------------------------------------------------
            # Prefer questions with genuinely different options.
            # --------------------------------------------------

            diversity = cls._option_diversity(
                question
            )

            score = (
                discrimination * 0.45
                + coverage * 0.35
                + diversity * 0.20
                + random.uniform(
                    0.0,
                    cls.RANDOM_WEIGHT
                )
            )

            scored.append(
                (
                    score,
                    question
                )
            )

        if not scored:
            return random.choice(
                remaining
            )

        scored.sort(
            key=lambda item: item[0],
            reverse=True
        )

        top_count = min(
            4,
            len(scored)
        )

        return random.choice(
            scored[:top_count]
        )[1]

    # ==========================================================
    # PHASE 3 — REFINEMENT
    # ==========================================================

    @classmethod
    def _select_refinement_question(
        cls,
        remaining: List[CompactQuestion],
        user_vector: List[float],
        candidates: List[VectorCharacterProfile]
    ) -> CompactQuestion:

        if not candidates:

            return random.choice(
                remaining
            )

        # ------------------------------------------------------
        # Rank the current candidates.
        # ------------------------------------------------------

        current_ranking = (
            RankingEngine.rank_characters(
                user_vector=user_vector,
                candidates=candidates
            )
        )

        # ------------------------------------------------------
        # Don't only consider the top 2-3 characters.
        #
        # A character sitting at #8 may become #1 after the
        # next answer.
        # ------------------------------------------------------

        leading_names = {
            item["name"]
            for item in current_ranking[
                :cls.REFINEMENT_CANDIDATES
            ]
        }

        leading_candidates = [
            candidate
            for candidate in candidates
            if candidate.name in leading_names
        ]

        if len(leading_candidates) < 2:

            leading_candidates = candidates

        scored = []

        for question in remaining:

            # --------------------------------------------------
            # Character discrimination
            # --------------------------------------------------

            discrimination = (
                cls._character_discrimination(
                    question=question,
                    user_vector=user_vector,
                    candidates=leading_candidates
                )
            )

            # --------------------------------------------------
            # Trait coverage
            # --------------------------------------------------

            coverage = cls._trait_coverage_score(
                question=question,
                user_vector=user_vector
            )

            # --------------------------------------------------
            # Option diversity
            # --------------------------------------------------

            diversity = cls._option_diversity(
                question
            )

            # --------------------------------------------------
            # Uncertainty
            #
            # Questions targeting traits with weak evidence
            # receive extra weight.
            # --------------------------------------------------

            uncertainty = cls._question_uncertainty(
                question=question,
                user_vector=user_vector
            )

            score = (
                discrimination * 0.45
                + coverage * 0.25
                + uncertainty * 0.20
                + diversity * 0.10
                + random.uniform(
                    0.0,
                    cls.RANDOM_WEIGHT
                )
            )

            scored.append(
                (
                    score,
                    question
                )
            )

        if not scored:
            return random.choice(
                remaining
            )

        scored.sort(
            key=lambda item: item[0],
            reverse=True
        )

        top_count = min(
            3,
            len(scored)
        )

        return random.choice(
            scored[:top_count]
        )[1]

    # ==========================================================
    # CHARACTER DISCRIMINATION
    # ==========================================================

    @classmethod
    def _character_discrimination(
        cls,
        question: CompactQuestion,
        user_vector: List[float],
        candidates: List[VectorCharacterProfile]
    ) -> float:

        if (
            not question.options
            or len(candidates) < 2
        ):
            return 0.0

        simulated_rankings = []

        # ------------------------------------------------------
        # Pretend the user selected each possible answer.
        #
        # Then see how much the character ranking changes.
        # ------------------------------------------------------

        for option in question.options.values():

            option_vector = cls._option_vector(
                option
            )

            simulated_vector = cls._add_vectors(
                user_vector,
                option_vector
            )

            ranking = (
                RankingEngine.rank_characters(
                    user_vector=simulated_vector,
                    candidates=candidates
                )
            )

            if ranking:

                simulated_rankings.append(
                    ranking
                )

        if len(simulated_rankings) < 2:
            return 0.0

        # ------------------------------------------------------
        # Find every character that appears in the simulated
        # rankings.
        # ------------------------------------------------------

        all_names = {
            item["name"]
            for ranking in simulated_rankings
            for item in ranking
        }

        variations = []

        # ------------------------------------------------------
        # Measure how much each character's score changes
        # depending on the answer.
        # ------------------------------------------------------

        for name in all_names:

            scores = []

            for ranking in simulated_rankings:

                match = next(
                    (
                        item
                        for item in ranking
                        if item["name"] == name
                    ),
                    None
                )

                if match is not None:

                    scores.append(
                        match["score"]
                    )

            if len(scores) < 2:
                continue

            mean = (
                sum(scores)
                / len(scores)
            )

            variance = (
                sum(
                    (score - mean) ** 2
                    for score in scores
                )
                / len(scores)
            )

            variations.append(
                math.sqrt(
                    variance
                )
            )

        if not variations:
            return 0.0

        average_variation = (
            sum(variations)
            / len(variations)
        )

        # Scores are out of roughly 0-100.
        #
        # Divide to normalize the result to approximately 0-1.
        return min(
            average_variation / 20.0,
            1.0
        )

    # ==========================================================
    # TRAIT COVERAGE
    # ==========================================================

    @classmethod
    def _trait_coverage_score(
        cls,
        question: CompactQuestion,
        user_vector: List[float]
    ) -> float:

        question_vector = (
            cls._question_vector(
                question
            )
        )

        if not question_vector:
            return 0.0

        if not user_vector:
            return 1.0

        score = 0.0
        total_weight = 0.0

        for index, strength in enumerate(
            question_vector
        ):

            if index >= len(user_vector):
                break

            strength = min(
                abs(strength),
                cls.MAX_TRAIT_WEIGHT
            )

            evidence = abs(
                user_vector[index]
            )

            # --------------------------------------------------
            # Diminishing returns.
            #
            # The first evidence for a trait is valuable.
            # Repeated evidence becomes less useful.
            # --------------------------------------------------

            uncertainty = 1.0 / (
                1.0 + evidence
            )

            score += (
                strength
                * uncertainty
            )

            total_weight += strength

        if total_weight <= 0:
            return 0.0

        return min(
            score / total_weight,
            1.0
        )

    # ==========================================================
    # QUESTION UNCERTAINTY
    # ==========================================================

    @classmethod
    def _question_uncertainty(
        cls,
        question: CompactQuestion,
        user_vector: List[float]
    ) -> float:

        question_vector = (
            cls._question_vector(
                question
            )
        )

        if not question_vector:
            return 0.0

        if not user_vector:
            return 1.0

        uncertainty = 0.0
        total_weight = 0.0

        for index, strength in enumerate(
            question_vector
        ):

            if index >= len(user_vector):
                break

            strength = abs(
                strength
            )

            if strength <= 0:
                continue

            evidence = abs(
                user_vector[index]
            )

            # Strong existing evidence means lower uncertainty.
            trait_uncertainty = 1.0 / (
                1.0 + evidence
            )

            uncertainty += (
                strength
                * trait_uncertainty
            )

            total_weight += strength

        if total_weight <= 0:
            return 0.0

        return min(
            uncertainty / total_weight,
            1.0
        )

    # ==========================================================
    # QUESTION VECTOR
    # ==========================================================

    @classmethod
    def _question_vector(
        cls,
        question: CompactQuestion
    ) -> List[float]:

        vectors = [
            cls._option_vector(
                option
            )
            for option in question.options.values()
        ]

        if not vectors:
            return []

        length = min(
            len(vector)
            for vector in vectors
        )

        if length <= 0:
            return []

        # ------------------------------------------------------
        # Average absolute evidence across all options.
        #
        # This tells us which personality dimensions a question
        # as a whole is testing.
        # ------------------------------------------------------

        return [
            sum(
                abs(vector[i])
                for vector in vectors
            )
            / len(vectors)
            for i in range(length)
        ]

    # ==========================================================
    # OPTION VECTOR
    # ==========================================================

    @staticmethod
    def _option_vector(
        option
    ) -> List[float]:

        NUM_TRAITS = 12

        vector = [
            0.0
        ] * NUM_TRAITS

        if option is None:
            return vector

        # ------------------------------------------------------
        # NEW FORMAT
        #
        # evidence={
        #     Behavior.CREATIVE: 0.8,
        #     Behavior.CURIOUS: 0.4
        # }
        #
        # ------------------------------------------------------

        evidence = getattr(
            option,
            "evidence",
            None
        )

        if evidence:

            for behavior, strength in evidence.items():

                profile = (
                    BEHAVIOR_PROFILES.get(
                        behavior
                    )
                )

                if profile is None:
                    continue

                try:

                    strength = float(
                        strength
                    )

                except (
                    TypeError,
                    ValueError
                ):

                    continue

                strength = max(
                    -1.0,
                    min(
                        1.0,
                        strength
                    )
                )

                for i in range(
                    min(
                        NUM_TRAITS,
                        len(profile)
                    )
                ):

                    vector[i] += (
                        profile[i]
                        * strength
                    )

            return vector

        # ------------------------------------------------------
        # OLD FORMAT
        #
        # behaviors=[...]
        #
        # Keep this for compatibility with existing questions.
        # ------------------------------------------------------

        behaviors = getattr(
            option,
            "behaviors",
            None
        )

        if not behaviors:
            return vector

        valid_behaviors = 0

        for behavior in behaviors:

            profile = (
                BEHAVIOR_PROFILES.get(
                    behavior
                )
            )

            if profile is None:
                continue

            valid_behaviors += 1

            for i in range(
                min(
                    NUM_TRAITS,
                    len(profile)
                )
            ):

                vector[i] += (
                    profile[i]
                    * 0.50
                )

        if valid_behaviors == 0:
            return vector

        # ------------------------------------------------------
        # Average old-format behaviors.
        #
        # This prevents an option with 3 behaviors from being
        # automatically 3x stronger than an option with 1.
        # ------------------------------------------------------

        return [
            value / valid_behaviors
            for value in vector
        ]

    # ==========================================================
    # OPTION DIVERSITY
    # ==========================================================

    @classmethod
    def _option_diversity(
        cls,
        question: CompactQuestion
    ) -> float:

        vectors = [
            cls._option_vector(
                option
            )
            for option in question.options.values()
        ]

        if len(vectors) < 2:
            return 0.0

        total_distance = 0.0
        comparisons = 0

        for i in range(
            len(vectors)
        ):

            for j in range(
                i + 1,
                len(vectors)
            ):

                total_distance += (
                    cls._vector_distance(
                        vectors[i],
                        vectors[j]
                    )
                )

                comparisons += 1

        if comparisons == 0:
            return 0.0

        average_distance = (
            total_distance
            / comparisons
        )

        # 12 dimensions × roughly 1 max difference.
        #
        # Normalize the distance to approximately 0-1.
        return min(
            average_distance / 8.0,
            1.0
        )

    # ==========================================================
    # VECTOR DISTANCE
    # ==========================================================

    @staticmethod
    def _vector_distance(
        a: List[float],
        b: List[float]
    ) -> float:

        if not a or not b:
            return 0.0

        length = min(
            len(a),
            len(b)
        )

        return sum(
            abs(
                a[i] - b[i]
            )
            for i in range(length)
        )

    # ==========================================================
    # VECTOR ADDITION
    # ==========================================================

    @staticmethod
    def _add_vectors(
        a: List[float],
        b: List[float]
    ) -> List[float]:

        length = min(
            len(a),
            len(b)
        )

        result = list(a)

        if len(result) < len(b):

            result.extend(
                [0.0] * (
                    len(b)
                    - len(result)
                )
            )

        for i in range(length):

            result[i] += b[i]

        return result