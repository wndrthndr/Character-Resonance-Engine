# api/question.py

from fastapi import APIRouter, HTTPException, Query
from data.questions import QUESTION_POOL
import random

router = APIRouter(
    prefix="/api/questions",
    tags=["Questions"]
)


@router.get("/")
def get_questions(
    franchise: str = Query("all"),
    limit: int = Query(10, ge=1)
):



    if franchise == "all":
        global_qs = [q for q in QUESTION_POOL if q.scope == "GLOBAL"]
        random.shuffle(global_qs)
        return global_qs[:limit]

    global_qs = [q for q in QUESTION_POOL if q.scope == "GLOBAL"]
    franchise_qs = [q for q in QUESTION_POOL if q.franchise == franchise]

    if not franchise_qs:
        raise HTTPException(
            status_code=404,
            detail=f"No questions for franchise: {franchise}"
        )

    random.shuffle(global_qs)
    random.shuffle(franchise_qs)

    num_global = limit // 2
    num_franchise = limit - num_global

    selected = global_qs[:num_global] + franchise_qs[:num_franchise]
    random.shuffle(selected)

    return selected
@router.get("/global")
def get_global_questions():

    return [

        q

        for q in QUESTION_POOL

        if q.scope == "GLOBAL"
    ]


@router.get("/{franchise}")
def get_franchise_questions(franchise: str):

    questions = [

        q

        for q in QUESTION_POOL

        if q.franchise == franchise
    ]

    if not questions:

        raise HTTPException(
            status_code=404,
            detail="Franchise not found."
        )

    return questions