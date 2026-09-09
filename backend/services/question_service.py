
import random

from data.questions import QUESTION_POOL


class QuestionService:

    # ==========================================================
    # GET ALL QUESTIONS
    # ==========================================================

    @staticmethod
    def get_all():
        return QUESTION_POOL

    # ==========================================================
    # GLOBAL QUESTIONS
    # ==========================================================

    @staticmethod
    def get_global():

        return [
            q
            for q in QUESTION_POOL
            if q.scope == "GLOBAL"
        ]

    # ==========================================================
    # FRANCHISE QUESTIONS
    # ==========================================================

    @staticmethod
    def get_franchise(franchise: str):

        return [
            q
            for q in QUESTION_POOL
            if q.scope == "FRANCHISE"
            and q.franchise == franchise
        ]

    # ==========================================================
    # GENERATE QUIZ
    # ==========================================================

    @staticmethod
    def generate_quiz(
        franchise: str,
        global_questions: int = 10,
        franchise_questions: int = 10
    ):
        """
        Build the question pool used by the adaptive selector.

        IMPORTANT:
            This does NOT mean the user will answer 20 questions.

            The quiz still has its own MAX_QUESTIONS limit.

            We intentionally give QuestionSelector a larger pool
            so it has enough choices to:

                Q1-Q4 -> explore different traits
                Q5-Q6 -> discover useful distinctions
                Q7+   -> refine the result

        Previously:
            5 global + 5 franchise = 10 available questions

        Now:
            10 global + 10 franchise = up to 20 available questions
        """

        franchise = franchise.lower()

        globals_pool = QuestionService.get_global()

        franchise_pool = QuestionService.get_franchise(
            franchise
        )

        selected = []

        # ======================================================
        # GLOBAL QUESTIONS
        # ======================================================

        global_count = min(
            global_questions,
            len(globals_pool)
        )

        if global_count > 0:

            selected.extend(
                random.sample(
                    globals_pool,
                    global_count
                )
            )

        # ======================================================
        # FRANCHISE QUESTIONS
        # ======================================================

        franchise_count = min(
            franchise_questions,
            len(franchise_pool)
        )

        if franchise_count > 0:

            selected.extend(
                random.sample(
                    franchise_pool,
                    franchise_count
                )
            )

        # ======================================================
        # FINAL SHUFFLE
        # ======================================================

        random.shuffle(
            selected
        )

        return selected
