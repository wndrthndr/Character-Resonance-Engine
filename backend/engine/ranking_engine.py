import math
from typing import List

from models import VectorCharacterProfile


class RankingEngine:
    """
    Character personality ranking engine.

    Philosophy
    ----------
    A character should win because the user's PERSONALITY SHAPE
    resembles that character, not simply because many trait values
    happen to be high.

    The ranking therefore uses:

        1. Distinctive character traits
        2. User/character trait agreement
        3. Contradiction penalties
        4. Overall cosine similarity as a small supporting signal

    This prevents broadly "high trait" characters from dominating
    every quiz.
    """

    # ==========================================================
    # CONFIGURATION
    #
    # SIGNATURE_WEIGHT + STRONG_MATCH_WEIGHT + PROFILE_WEIGHT +
    # COSINE_WEIGHT MUST sum to 1.0. These are the only positive
    # contributors to the score, so if they sum to more than 1.0
    # the final min(1.0, raw_score) clamp starts firing on
    # ordinary good matches -- not just genuinely perfect ones --
    # and unrelated characters start tying at 100.0 (this was
    # happening before: the old weights summed to 1.20).
    # ==========================================================

    SIGNATURE_WEIGHT = 0.55
    STRONG_MATCH_WEIGHT = 0.20
    PROFILE_WEIGHT = 0.15
    COSINE_WEIGHT = 0.10

    # Contradictions are a separate, subtractive term -- not part
    # of the budget above. contradiction_penalty() returns a value
    # already normalized to roughly [0, 1], so this weight can be
    # tuned independently without needing a second "fudge factor"
    # multiplier elsewhere (the old code applied CONTRADICTION_WEIGHT
    # inside contradiction_penalty() and then multiplied the result
    # by an unrelated 0.035 in rank_characters(), which made even a
    # maximal contradiction worth only ~6 points out of 100).
    CONTRADICTION_WEIGHT = 0.35

    # ==========================================================
    # NORMALIZE
    #
    # Not currently used internally by rank_characters() -- the
    # vector passed in is expected to already be normalized
    # upstream (e.g. by BehaviorEngine.normalize). Kept as a
    # public utility in case other callers rely on it.
    # ==========================================================

    @staticmethod
    def normalize(vector: List[float]) -> List[float]:

        if not vector:
            return []

        maximum = max(vector)

        if maximum <= 0:
            return [0.0] * len(vector)

        return [
            value / maximum
            for value in vector
        ]

    # ==========================================================
    # COSINE
    # ==========================================================

    @staticmethod
    def cosine_similarity(
        user_vector: List[float],
        character_vector: List[float]
    ) -> float:

        if (
            not user_vector
            or not character_vector
            or len(user_vector) != len(character_vector)
        ):
            return 0.0

        dot = sum(
            u * c
            for u, c in zip(
                user_vector,
                character_vector
            )
        )

        user_mag = math.sqrt(
            sum(u * u for u in user_vector)
        )

        character_mag = math.sqrt(
            sum(c * c for c in character_vector)
        )

        if user_mag == 0 or character_mag == 0:
            return 0.0

        return dot / (
            user_mag * character_mag
        )

    # ==========================================================
    # CHARACTER SIGNATURE
    # ==========================================================

    @staticmethod
    def signature_similarity(
        user_vector: List[float],
        character_vector: List[float]
    ) -> float:

        """
        Measures similarity on traits that actually distinguish
        the character.

        Example:

            Character trait = 0.95
            User trait      = 0.90

        -> very strong match.

            Character trait = 0.95
            User trait      = 0.20

        -> very poor match.

        Traits around 0.5 are deliberately given little influence
        because they don't tell us much about the character.
        """

        if (
            not user_vector
            or not character_vector
            or len(user_vector) != len(character_vector)
        ):
            return 0.0

        total = 0.0
        weight_total = 0.0

        for user, character in zip(
            user_vector,
            character_vector
        ):

            # --------------------------------------------------
            # Character distinctiveness
            # --------------------------------------------------

            distinctiveness = abs(
                character - 0.5
            ) * 2.0

            # Ignore almost-neutral character traits.
            if distinctiveness < 0.15:
                weight = 0.15

            elif distinctiveness < 0.35:
                weight = 0.35

            elif distinctiveness < 0.60:
                weight = 0.75

            elif distinctiveness < 0.80:
                weight = 1.25

            else:
                weight = 2.00

            # --------------------------------------------------
            # Agreement
            # --------------------------------------------------

            distance = abs(
                user - character
            )

            similarity = 1.0 - distance

            similarity = max(
                0.0,
                min(1.0, similarity)
            )

            # NOTE: previously each of these was also multiplied
            # by a DISTINCTIVE_WEIGHT constant. Since that constant
            # was applied identically to both `total` and
            # `weight_total`, it canceled out of the final
            # total / weight_total division and had zero effect
            # on the result -- it's removed here rather than kept
            # as dead configuration.

            total += similarity * weight
            weight_total += weight

        if weight_total == 0:
            return 0.0

        return total / weight_total

    # ==========================================================
    # PROFILE SHAPE
    # ==========================================================

    @staticmethod
    def profile_similarity(
        user_vector: List[float],
        character_vector: List[float]
    ) -> float:

        """
        Secondary signal.

        Compares the complete personality shape but gives
        substantially less influence than signature traits.
        """

        if (
            not user_vector
            or not character_vector
            or len(user_vector) != len(character_vector)
        ):
            return 0.0

        total = 0.0
        weight_total = 0.0

        for user, character in zip(
            user_vector,
            character_vector
        ):

            distance = abs(
                user - character
            )

            similarity = 1.0 - distance

            similarity = max(
                0.0,
                min(1.0, similarity)
            )

            total += similarity
            weight_total += 1.0

        if weight_total == 0:
            return 0.0

        return total / weight_total

    # ==========================================================
    # CONTRADICTION PENALTY
    # ==========================================================

    @staticmethod
    def contradiction_penalty(
        user_vector: List[float],
        character_vector: List[float]
    ) -> float:

        """
        Strongly penalizes obvious personality contradictions.

        Example:

            Character strongly rebellious = 0.95
            User strongly disciplined  = 0.90

        should hurt the character's score.

        Likewise:

            Character strongly empathetic = 0.95
            User empathy = 0.10

        should also hurt.

        Returns a value normalized to roughly [0, 1] -- the
        average per-trait contradiction severity -- so it can be
        combined with the other (also [0, 1]) similarity signals
        using a single top-level weight (CONTRADICTION_WEIGHT) in
        rank_characters(), instead of needing a second unrelated
        scaling constant applied by the caller.
        """

        if (
            not user_vector
            or not character_vector
            or len(user_vector) != len(character_vector)
        ):
            return 0.0

        penalty = 0.0

        for user, character in zip(
            user_vector,
            character_vector
        ):

            difference = abs(
                user - character
            )

            # Only meaningful contradictions matter.
            if difference < 0.35:
                continue

            # Character strongly possesses trait
            # while user strongly lacks it.
            if character >= 0.75 and user <= 0.35:

                severity = (
                    character - user
                )

                penalty += severity

            # Character strongly lacks trait
            # while user strongly possesses it.
            elif character <= 0.25 and user >= 0.75:

                severity = (
                    user - character
                )

                penalty += severity

        return penalty / len(user_vector)

    # ==========================================================
    # STRONG MATCH BONUS
    # ==========================================================

    @staticmethod
    def strong_match_bonus(
        user_vector: List[float],
        character_vector: List[float]
    ) -> float:

        """
        Rewards situations where BOTH:

            character strongly has a trait
            AND
            user strongly has that trait.

        This is more useful than rewarding generic similarity.
        """

        if (
            not user_vector
            or not character_vector
            or len(user_vector) != len(character_vector)
        ):
            return 0.0

        total = 0.0
        weight_total = 0.0

        for user, character in zip(
            user_vector,
            character_vector
        ):

            character_strength = abs(
                character - 0.5
            ) * 2.0

            user_strength = abs(
                user - 0.5
            ) * 2.0

            # Both need to be distinctive.
            if (
                character_strength < 0.45
                or user_strength < 0.30
            ):
                continue

            agreement = 1.0 - abs(
                user - character
            )

            agreement = max(
                0.0,
                min(1.0, agreement)
            )

            weight = (
                character_strength
                * user_strength
            )

            total += (
                agreement * weight
            )

            weight_total += weight

        if weight_total == 0:
            return 0.0

        return total / weight_total

    # ==========================================================
    # FINAL RANKING
    # ==========================================================

    @classmethod
    def rank_characters(
        cls,
        user_vector: List[float],
        candidates: List[VectorCharacterProfile]
    ) -> List[dict]:

        if not user_vector or not candidates:
            return []

        comparison_vector = user_vector

        ranked = []

        for character in candidates:

            character_vector = (
                character.trait_vector
            )

            if len(comparison_vector) != len(
                character_vector
            ):
                continue

            # --------------------------------------------------
            # 1. Character signature
            # --------------------------------------------------

            signature = cls.signature_similarity(
                comparison_vector,
                character_vector
            )

            # --------------------------------------------------
            # 2. Strong matching traits
            # --------------------------------------------------

            strong_match = cls.strong_match_bonus(
                comparison_vector,
                character_vector
            )

            # --------------------------------------------------
            # 3. Overall profile
            # --------------------------------------------------

            profile = cls.profile_similarity(
                comparison_vector,
                character_vector
            )

            # --------------------------------------------------
            # 4. Overall direction
            # --------------------------------------------------

            cosine = cls.cosine_similarity(
                comparison_vector,
                character_vector
            )

            # --------------------------------------------------
            # 5. Contradictions
            # --------------------------------------------------

            contradiction = cls.contradiction_penalty(
                comparison_vector,
                character_vector
            )

            # --------------------------------------------------
            # FINAL SCORE
            #
            # The four positive terms are weighted to sum to
            # 1.0 (see the class-level comment on the weight
            # constants), so a perfect match tops out at exactly
            # 1.0 instead of overshooting and getting clamped.
            # Contradictions are then subtracted as an
            # independent penalty on the same [0, 1] scale.
            # --------------------------------------------------

            raw_score = (

                signature
                * cls.SIGNATURE_WEIGHT

                +

                strong_match
                * cls.STRONG_MATCH_WEIGHT

                +

                profile
                * cls.PROFILE_WEIGHT

                +

                cosine
                * cls.COSINE_WEIGHT
            )

            raw_score -= (
                contradiction * cls.CONTRADICTION_WEIGHT
            )

            raw_score = max(
                0.0,
                min(1.0, raw_score)
            )

            ranked.append({
                "name": character.name,
                "tagline": character.tagline,
                "description": character.desc,
                "image": character.image,
                "score": round(
                    raw_score * 100,
                    2
                ),
                "character": character,
                "signals": cls.explain_match(
                    comparison_vector,
                    character_vector
                )
            })

        # ------------------------------------------------------
        # SORT
        # ------------------------------------------------------

        ranked.sort(
            key=lambda item: item["score"],
            reverse=True
        )

        return ranked
    @staticmethod
    def explain_match(  
        user_vector: List[float],
        character_vector: List[float]
    ) -> List[dict]:

        trait_names = [
            "ACTION",
            "ANALYTICAL",
            "EMPATHETIC",
            "JUSTICE_DRIVEN",
            "AMBITIOUS",
            "CREATIVE",
            "LOYAL",
            "DISCIPLINED",
            "HUMOROUS",
            "CURIOUS",
            "PRAGMATIC",
            "REBELLIOUS",
        ]

        signals = []

        length = min(
            len(user_vector),
            len(character_vector),
            len(trait_names)
        )

        for i in range(length):
            user_value = user_vector[i]
            character_value = character_vector[i]

            # How closely the user's trait matches
            # this character's trait.
            match = 1.0 - abs(
                user_value - character_value
            )

            match = max(
                0.0,
                min(1.0, match)
            )

            # Only consider traits that are meaningful
            # for the character.
            if character_value < 0.50:
                continue

            signals.append({
                "trait": trait_names[i],
                "strength": round(match, 3),
                "character_strength": round(
                    character_value,
                    3
                ),
                "user_strength": round(
                    user_value,
                    3
                ),
            })

        # Strongest matching traits first
        signals.sort(
            key=lambda item: item["strength"],
            reverse=True
        )

        return signals[:4]