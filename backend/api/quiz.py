from fastapi import APIRouter, HTTPException

from services.quiz_service import QuizService

from models import (
    SubmitRequest,
    QuizResultResponse,
    StartQuizRequest,
    AnswerRequest,
    NextQuestionResponse
)

router = APIRouter(
    prefix="/api/quiz",
    tags=["Quiz"]
)

# ==========================================================
# OLD API (BACKWARDS COMPATIBLE)
# ==========================================================

@router.post(
    "/submit",
    response_model=QuizResultResponse
)
def submit_quiz(payload: SubmitRequest):

    try:

        return QuizService.evaluate(payload)

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ==========================================================
# START ADAPTIVE QUIZ
# ==========================================================

@router.post(
    "/start",
    response_model=NextQuestionResponse
)
def start_quiz(payload: StartQuizRequest):

    try:

        session = QuizService.start_quiz(
            payload.franchise
        )

        return NextQuestionResponse(

            session_id=session.session_id,

            completed=False,

            question=session.current_question,

            confidence=0.0,

            predicted_character=None

        )

    except Exception as e:
        import traceback

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ==========================================================
# SUBMIT ONE ANSWER
# ==========================================================

@router.post(
    "/answer",
    response_model=NextQuestionResponse
)
def submit_answer(payload: AnswerRequest):

    try:

        session = QuizService.submit_answer(

            payload.session_id,

            payload.response

        )

        return NextQuestionResponse(
            session_id=session.session_id,
            completed=session.completed,
            question=session.current_question,
            confidence=session.confidence,
            predicted_character=session.predicted_character,
            matches=session.matches
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ==========================================================
# FINISH QUIZ
# ==========================================================

@router.post("/finish/{session_id}")
def finish_quiz(session_id: str):

    try:

        return QuizService.finish_quiz(session_id)

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ==========================================================
# GET SESSION
# ==========================================================

@router.get("/session/{session_id}")
def get_session(session_id: str):

    session = QuizService.get_session(session_id)

    if session is None:

        raise HTTPException(

            status_code=404,

            detail="Session not found."

        )

    return session