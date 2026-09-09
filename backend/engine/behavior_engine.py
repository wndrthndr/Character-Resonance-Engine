from typing import Dict, List, Union

from config import NUM_TAGS
from models import (
    CompactQuestion,
    UserResponse,
)

from data.behavior_profiles import BEHAVIOR_PROFILES


class BehaviorEngine:
    """
    Converts quiz answers into accumulated personality evidence.

    Architecture:

        Answer
          ↓
        weighted behavior evidence
          ↓
        accumulated trait vector
          ↓
        average evidence
          ↓
        ranking / adaptive selection

    IMPORTANT
    ----------
    The engine does NOT normalize the vector while accumulating
    evidence.

    Each answer contributes evidence only once.

    New question format can use:

        evidence={
            Behavior.CREATIVE: 0.8,
            Behavior.CURIOUS: 0.4,
        }

    The old format is still supported:

        behaviors=[
            Behavior.CREATIVE,
            Behavior.CURIOUS
        ]

    This allows us to migrate questions gradually.
    """

    # ==========================================================
    # BUILD COMPLETE VECTOR
    # ==========================================================

    @classmethod
    def build_user_vector(
        cls,
        responses: List[UserResponse],
        questions: List[CompactQuestion]
    ) -> List[float]:

        user_vector = [0.0] * NUM_TAGS

        question_map = {
            question.id: question
            for question in questions
        }

        for response in responses:

            question = question_map.get(
                response.question_id
            )

            if question is None:
                continue

            option = question.options.get(
                response.selected_option
            )

            if option is None:
                continue

            cls.apply_option(
                user_vector,
                option
            )

        return user_vector

    # ==========================================================
    # INCREMENTAL UPDATE
    # ==========================================================

    @classmethod
    def update_vector(
        cls,
        current_vector: List[float],
        behaviors=None,
        evidence: Dict = None,
        option=None
    ) -> List[float]:

        # ------------------------------------------------------
        # Make sure vector always has exactly NUM_TAGS values.
        # ------------------------------------------------------

        updated_vector = list(
            current_vector[:NUM_TAGS]
        )

        if len(updated_vector) < NUM_TAGS:

            updated_vector.extend(
                [0.0] * (
                    NUM_TAGS - len(updated_vector)
                )
            )

        # ------------------------------------------------------
        # Preferred path:
        #
        # Pass the complete option.
        # ------------------------------------------------------

        if option is not None:

            cls.apply_option(
                updated_vector,
                option
            )

            return updated_vector

        # ------------------------------------------------------
        # New weighted evidence format.
        # ------------------------------------------------------

        if evidence:

            cls._apply_weighted_evidence(
                updated_vector,
                evidence
            )

            return updated_vector

        # ------------------------------------------------------
        # Backwards-compatible old format.
        # ------------------------------------------------------

        if behaviors:

            cls._apply_behaviors(
                updated_vector,
                behaviors
            )

        return updated_vector

    # ==========================================================
    # APPLY OPTION
    # ==========================================================

    @classmethod
    def apply_option(
        cls,
        vector: List[float],
        option
    ) -> None:

        if option is None:
            return

        # ------------------------------------------------------
        # Preferred format:
        #
        # option.evidence
        # ------------------------------------------------------

        evidence = getattr(
            option,
            "evidence",
            None
        )

        if evidence:

            cls._apply_weighted_evidence(
                vector,
                evidence
            )

            return

        # ------------------------------------------------------
        # Existing format:
        #
        # option.behaviors
        #
        # This remains supported so existing questions don't
        # immediately break.
        # ------------------------------------------------------

        behaviors = getattr(
            option,
            "behaviors",
            None
        )

        if behaviors:

            cls._apply_behaviors(
                vector,
                behaviors
            )

    # ==========================================================
    # APPLY WEIGHTED EVIDENCE
    # ==========================================================

    @classmethod
    def _apply_weighted_evidence(
        cls,
        vector: List[float],
        evidence: Dict
    ) -> None:

        if not evidence:
            return

        for behavior, strength in evidence.items():

            try:
                strength = float(strength)
            except (
                TypeError,
                ValueError
            ):
                continue

            # --------------------------------------------------
            # Prevent malformed question data from exploding
            # the personality vector.
            #
            # Evidence is intentionally bounded.
            # --------------------------------------------------

            strength = max(
                -1.0,
                min(
                    1.0,
                    strength
                )
            )

            behavior_vector = (
                BEHAVIOR_PROFILES.get(
                    behavior
                )
            )

            if behavior_vector is None:
                continue

            for i in range(
                min(
                    NUM_TAGS,
                    len(behavior_vector)
                )
            ):

                vector[i] += (
                    behavior_vector[i]
                    * strength
                )

    # ==========================================================
    # APPLY OLD BEHAVIOR FORMAT
    # ==========================================================

    @classmethod
    def _apply_behaviors(
        cls,
        vector: List[float],
        behaviors
    ) -> None:

        if not behaviors:
            return

        # ------------------------------------------------------
        # Old behavior format treats every selected behavior
        # as moderate evidence rather than full-strength evidence.
        #
        # This is important.
        #
        # Previously:
        #
        #     behavior → 1.0 × entire profile
        #
        # Now:
        #
        #     behavior → 0.50 × profile
        #
        # This prevents one answer containing 3 behaviors from
        # overwhelming the entire quiz.
        # ------------------------------------------------------

        OLD_BEHAVIOR_STRENGTH = 0.50

        for behavior in behaviors:

            behavior_vector = (
                BEHAVIOR_PROFILES.get(
                    behavior
                )
            )

            if behavior_vector is None:
                continue

            for i in range(
                min(
                    NUM_TAGS,
                    len(behavior_vector)
                )
            ):

                vector[i] += (
                    behavior_vector[i]
                    * OLD_BEHAVIOR_STRENGTH
                )

    # ==========================================================
    # AVERAGE EVIDENCE
    # ==========================================================

    @staticmethod
    def average(
        vector: List[float],
        question_count: int
    ) -> List[float]:

        if not vector:

            return []

        if question_count <= 0:

            return [
                0.0
                for _ in vector
            ]

        return [
            round(
                value / question_count,
                4
            )
            for value in vector
        ]

    # ==========================================================
    # MAX NORMALIZATION
    # ==========================================================

    @staticmethod
    def normalize(
        vector: List[float]
    ) -> List[float]:

        """
        Legacy normalization.

        Do NOT use this as the primary representation of the
        user's personality.

        It is retained for compatibility with older code.
        """

        if not vector:
            return []

        maximum = max(vector)

        if maximum <= 0:

            return [
                0.0
                for _ in vector
            ]

        return [
            round(
                value / maximum,
                3
            )
            for value in vector
        ]

    # ==========================================================
    # L2 NORMALIZATION
    # ==========================================================

    @staticmethod
    def l2_normalize(
        vector: List[float]
    ) -> List[float]:

        """
        Normalizes the vector by its overall magnitude instead
        of forcing the largest trait to 1.0.

        This is much safer for personality comparison because
        several traits being high does not automatically force
        every other trait into an artificially compressed range.
        """

        if not vector:
            return []

        magnitude = sum(
            value * value
            for value in vector
        ) ** 0.5

        if magnitude <= 0:

            return [
                0.0
                for _ in vector
            ]

        return [
            round(
                value / magnitude,
                4
            )
            for value in vector
        ]

    # ==========================================================
    # AVERAGE + L2 NORMALIZE
    # ==========================================================

    @classmethod
    def normalized_average(
        cls,
        vector: List[float],
        question_count: int
    ) -> List[float]:

        averaged = cls.average(
            vector,
            question_count
        )

        return cls.l2_normalize(
            averaged
        )

    # ==========================================================
    # TRAIT STRENGTH
    # ==========================================================

    @staticmethod
    def trait_strengths(
        vector: List[float],
        question_count: int
    ) -> List[float]:

        """
        Returns average evidence without max normalization.

        This is the preferred representation for the adaptive
        question selector.
        """

        return BehaviorEngine.average(
            vector,
            question_count
        )