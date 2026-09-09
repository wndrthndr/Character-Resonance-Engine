from typing import List, Optional
from uuid import uuid4

from pydantic import BaseModel, Field

from models.question import CompactQuestion
from models.response import UserResponse


class QuizSession(BaseModel):
    """
    Represents one active quiz session.
    """

    session_id: str = Field(
        default_factory=lambda: str(uuid4())
    )

    franchise: str

    # Raw accumulated personality vector.
    # This should NOT be normalized after every answer.
    user_vector: List[float]

    # Questions already answered
    answered_questions: List[str] = Field(
        default_factory=list
    )

    # Entire quiz pool available
    available_questions: List[CompactQuestion]

    # Responses given so far
    responses: List[UserResponse] = Field(
        default_factory=list
    )

    # Current question shown to user
    current_question: Optional[CompactQuestion] = None

    # Finished?
    completed: bool = False

    # Confidence of current best match
    confidence: float = 0.0

    # Best character so far
    predicted_character: Optional[dict] = None
    matches: List[dict] = Field(default_factory=list)