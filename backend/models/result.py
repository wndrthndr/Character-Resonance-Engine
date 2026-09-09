from typing import List

from pydantic import BaseModel


class MatchResult(BaseModel):

    name: str

    tagline: str

    desc: str

    score: float


class QuizResultResponse(BaseModel):

    matches: List[MatchResult]

    user_fingerprint: List[float]

    dominant_trait: str