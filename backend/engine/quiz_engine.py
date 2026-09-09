from typing import Dict, List

from data.characters import CHARACTER_REGISTRY

from models import (
    CompactQuestion,
    UserResponse,
    VectorCharacterProfile,
    
)
from models.predict import PredictedCharacter
from engine.behavior_engine import BehaviorEngine
from engine.ranking_engine import RankingEngine


class QuizEngine:
    """
    High-level quiz orchestrator.

    Responsibilities
    ----------------
    1. Build the user's personality vector.
    2. Rank all characters.
    3. Return the final result.

    Supports BOTH:

    - Classic quiz
    - Adaptive quiz
    """

    # ==========================================================
    # CLASSIC QUIZ
    # ==========================================================

    @classmethod
    def evaluate_quiz(
        cls,
        franchise: str,
        responses: List[UserResponse],
        questions: List[CompactQuestion]
    ) -> Dict:

        user_vector = BehaviorEngine.build_user_vector(
            responses=responses,
            questions=questions
        )

        return cls.evaluate_vector(
            franchise=franchise,
            user_vector=user_vector
        )

    # ==========================================================
    # ADAPTIVE QUIZ
    # ==========================================================

    @classmethod
    def evaluate_vector(
        cls,
        franchise: str,
        user_vector: List[float]
    ) -> Dict:
          

        # ✅ ADD THESE PRINTS HERE
        print("FRANCHISE RECEIVED:", franchise)
        print("REGISTRY KEYS:", CHARACTER_REGISTRY.keys())
        print("ATLA COUNT:", len(CHARACTER_REGISTRY.get("atla", [])))

        candidates: List[VectorCharacterProfile] = (
            CHARACTER_REGISTRY.get(franchise, [])
        )

        print("CANDIDATES FOUND:", len(candidates))  # 🔥 ALSO ADD THIS

        if not candidates:
            raise ValueError(
                f"No characters found for franchise '{franchise}'."
            )

        ranking = RankingEngine.rank_characters(
            user_vector=user_vector,
            candidates=candidates
        )

        best_match = ranking[0] if ranking else None

        return {

            "user_vector": user_vector,

            "matches": ranking,

            "best_match": best_match

        }

    # ==========================================================
    # CONFIDENCE
    # ==========================================================

    @classmethod
    def confidence(
        cls,
        user_vector: List[float],
        franchise: str
    ) -> float:
        """
        Returns the confidence score (0-100)
        of the current best character.
        """

        result = cls.evaluate_vector(
            franchise,
            user_vector
        )

        if result["best_match"] is None:
            return 0.0

        return result["best_match"]["score"]

    # ==========================================================
    # PREDICT CHARACTER
    # ==========================================================

    @classmethod
    def predict_character(
        cls,
        franchise: str,
        user_vector: List[float]
    ) -> str | None:
        """
        Returns only the best matching character.
        """

        result = cls.evaluate_vector(
            franchise,
            user_vector
        )

        if result["best_match"] is None:
            return None

        best = result["best_match"]

        return PredictedCharacter(
            name=best["name"],
            color=best["character"].geometry["color"],
            image=best["image"]
        )