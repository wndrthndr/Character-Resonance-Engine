from typing import Optional,List

from pydantic import BaseModel

from models.question import CompactQuestion
from models.predict import PredictedCharacter

class NextQuestionResponse(BaseModel):
    session_id: str
    completed: bool
    question: Optional [CompactQuestion]
    confidence: float
    predicted_character: Optional[PredictedCharacter] = None
    matches: List[dict] = []