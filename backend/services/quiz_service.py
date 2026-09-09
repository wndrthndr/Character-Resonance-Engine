from typing import Dict, List

from engine.behavior_engine import BehaviorEngine
from engine.question_selector import QuestionSelector
from engine.quiz_engine import QuizEngine
from engine.ranking_engine import RankingEngine
from services.question_service import QuestionService
from data.characters import CHARACTER_REGISTRY

from models import (
    QuizSession,
    SubmitRequest,
    QuizResultResponse,
    MatchResult,
    UserResponse,
    NUM_TRAITS,
)

# ==========================================================
# Constants
# ==========================================================

MIN_QUESTIONS = 8
MAX_QUESTIONS = 10
EARLY_STOP_GAP = 10

# ==========================================================
# Active Sessions
# ==========================================================

ACTIVE_SESSIONS: Dict[str, QuizSession] = {}


class QuizService:

    # ======================================================
    # START QUIZ
    # ======================================================
    @staticmethod
    def start_quiz(franchise: str) -> QuizSession:

        franchise = franchise.lower()

        questions = QuestionService.generate_quiz(franchise)

        session = QuizSession(
            franchise=franchise,
            user_vector=[0.0] * NUM_TRAITS,
            available_questions=questions,
        )

        # Initial vector is empty, so selector can
        # choose from the available questions.
        candidates = QuizService._get_candidates(franchise)

        session.current_question = QuestionSelector.select_next(
            user_vector=session.user_vector,
            answered_questions=session.answered_questions,
            question_pool=session.available_questions,
            candidates=candidates,
        )

        ACTIVE_SESSIONS[session.session_id] = session

        return session

    # ======================================================
    # SUBMIT ONE ANSWER
    # ======================================================
    @staticmethod
    def submit_answer(session_id: str, response: UserResponse) -> QuizSession:

        session = ACTIVE_SESSIONS.get(session_id)

        if session is None:
            raise ValueError("Session not found.")

        question = session.current_question

        if question is None:
            raise ValueError("No active question.")

        option = question.options.get(response.selected_option)

        if option is None:
            raise ValueError("Invalid option.")

        # ==================================================
        # UPDATE RAW VECTOR
        # ==================================================

        session.user_vector = BehaviorEngine.update_vector(
            current_vector=session.user_vector,
            behaviors=option.behaviors,
        )

        # ==================================================
        # STORE ANSWER
        # ==================================================

        session.responses.append(response)
        session.answered_questions.append(question.id)

        # ==================================================
        # NORMALIZED VECTOR FOR ANALYSIS
        # ==================================================

        normalized_vector = BehaviorEngine.normalize(session.user_vector)

        # ==================================================
        # GET CANDIDATES
        # ==================================================

        candidates = QuizService._get_candidates(session.franchise)

        # ==================================================
        # RANKING (computed once, reused below)
        #
        # The previous version called RankingEngine.rank_characters
        # up to three times per submit_answer call on the exact
        # same (normalized_vector, candidates) inputs -- once for
        # session.matches, once for the early-termination gap
        # check, and once for the debug print. Now it's computed
        # once and reused everywhere.
        # ==================================================

        ranking = (
            RankingEngine.rank_characters(normalized_vector, candidates)
            if candidates
            else []
        )

        session.matches = ranking

        # ==================================================
        # CURRENT PREDICTION
        # ==================================================

        session.predicted_character = QuizEngine.predict_character(
            franchise=session.franchise,
            user_vector=normalized_vector,
        )

        session.confidence = QuizEngine.confidence(
            franchise=session.franchise,
            user_vector=normalized_vector,
        )

        questions_answered = len(session.answered_questions)

        # ==================================================
        # STOP CONDITIONS
        # ==================================================

        # --------------------------------------------------
        # EARLY TERMINATION
        # --------------------------------------------------

        if questions_answered >= MIN_QUESTIONS and len(ranking) > 1:

            top = ranking[0]["score"]
            second = ranking[1]["score"]

            gap = top - second

            # Keep the threshold conservative.
            if gap >= EARLY_STOP_GAP:

                session.completed = True
                session.current_question = None

                QuizService._debug(session, normalized_vector, candidates, ranking)

                return session

        # --------------------------------------------------
        # MAX QUESTIONS
        # --------------------------------------------------

        if questions_answered >= MAX_QUESTIONS:

            session.completed = True
            session.current_question = None

            QuizService._debug(session, normalized_vector, candidates, ranking)

            return session

        # ==================================================
        # CHOOSE NEXT QUESTION
        # ==================================================

        session.current_question = QuestionSelector.select_next(
            user_vector=session.user_vector,
            answered_questions=session.answered_questions,
            question_pool=session.available_questions,
            candidates=candidates,
        )

        # --------------------------------------------------
        # QUESTION POOL EXHAUSTED
        # --------------------------------------------------

        if session.current_question is None:

            session.completed = True

            QuizService._debug(session, normalized_vector, candidates, ranking)

            return session

        # ==================================================
        # DEBUG
        # ==================================================

        QuizService._debug(session, normalized_vector, candidates, ranking)

        return session

    # ======================================================
    # CANDIDATE LOOKUP
    #
    # Handles the lower/upper case key mismatch that used to
    # only be handled inside submit_answer. start_quiz now
    # uses the same lookup, so the very first question is
    # selected against the same candidate pool as every
    # question after it (previously, if a franchise's
    # characters were registered under an upper-case key,
    # start_quiz would get an empty candidate list while
    # submit_answer would correctly find them).
    # ======================================================

    @staticmethod
    def _get_candidates(franchise: str) -> List[dict]:

        return (
            CHARACTER_REGISTRY.get(franchise)
            or CHARACTER_REGISTRY.get(franchise.upper())
            or []
        )

    # ======================================================
    # DEBUG
    # ======================================================

    @staticmethod
    def _debug(
        session: QuizSession,
        normalized_vector,
        candidates,
        ranking,
    ) -> None:

        print("RAW VECTOR:", session.user_vector)
        print("NORMALIZED VECTOR:", normalized_vector)
        print("QUESTIONS ANSWERED:", len(session.answered_questions))
        print("CANDIDATES:", len(candidates))

        if ranking:
            print(
                "TOP 5:",
                [(item["name"], item["score"]) for item in ranking[:5]],
            )

    # ======================================================
    # FINISH QUIZ
    # ======================================================

    @staticmethod
    def finish_quiz(session_id: str):

        session = ACTIVE_SESSIONS.get(session_id)

        if session is None:
            raise ValueError("Session not found.")

        normalized_vector = BehaviorEngine.normalize(session.user_vector)

        result = QuizEngine.evaluate_vector(
            franchise=session.franchise,
            user_vector=normalized_vector,
        )

        session.completed = True

        return result

    # ======================================================
    # GET SESSION
    # ======================================================

    @staticmethod
    def get_session(session_id: str) -> QuizSession | None:

        return ACTIVE_SESSIONS.get(session_id)

    # ======================================================
    # OLD API SUPPORT
    # ======================================================

    @staticmethod
    def evaluate(payload: SubmitRequest) -> QuizResultResponse:

        questions = QuestionService.generate_quiz(payload.franchise)

        result = QuizEngine.evaluate_quiz(
            franchise=payload.franchise,
            responses=payload.responses,
            questions=questions,
        )

        matches = [
            MatchResult(
                name=item["name"],
                tagline=item["tagline"],
                desc=item["description"],
                score=item["score"],
            )
            for item in result["matches"]
        ]

        dominant = "Unknown"

        if result["user_vector"]:
            idx = result["user_vector"].index(max(result["user_vector"]))
            dominant = str(idx)

        return QuizResultResponse(
            matches=matches,
            user_fingerprint=result["user_vector"],
            dominant_trait=dominant,
        )