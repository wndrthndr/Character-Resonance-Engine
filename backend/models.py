from enum import Enum
from typing import Dict, List, Literal, Optional

from pydantic import BaseModel


# =====================================================
# DECISION BEHAVIORS
# =====================================================

class Behavior(str, Enum):
    EMPATHETIC = "EMPATHETIC"
    SUPPORTIVE = "SUPPORTIVE"

    STRATEGIC = "STRATEGIC"
    ANALYTICAL = "ANALYTICAL"

    AGGRESSIVE = "AGGRESSIVE"
    COURAGEOUS = "COURAGEOUS"

    HUMOROUS = "HUMOROUS"

    DIPLOMATIC = "DIPLOMATIC"

    SELFLESS = "SELFLESS"

    AMBITIOUS = "AMBITIOUS"

    PRAGMATIC = "PRAGMATIC"

    INNOVATIVE = "INNOVATIVE"

    DISCIPLINED = "DISCIPLINED"

    REBELLIOUS = "REBELLIOUS"

    ADAPTABLE = "ADAPTABLE"



# =====================================================
# CHARACTER
# =====================================================

class VectorCharacterProfile(BaseModel):

    name: str

    tagline: str

    desc: str

    image: Optional[str] = None

    geometry: Dict

    # Still keep vectors
    trait_vector: List[float]

    # NEW
    behaviors: List[Behavior] = []

    stats: Dict[str, int] = {}



# =====================================================
# QUESTION
# =====================================================

class CompactOption(BaseModel):

    text: str

    # Instead of weights
    behaviors: List[Behavior]



class CompactQuestion(BaseModel):

    id: str

    scope: Literal["GLOBAL", "FRANCHISE"]

    franchise: str

    question: str

    options: Dict[Literal["A", "B", "C", "D"], CompactOption]



# =====================================================
# USER
# =====================================================

class UserResponse(BaseModel):

    question_id: str

    selected_option: Literal["A", "B", "C", "D"]



class SubmitRequest(BaseModel):

    franchise: str

    responses: List[UserResponse]



# =====================================================
# RESULT
# =====================================================

class MatchResult(BaseModel):

    name: str

    tagline: str

    desc: str

    score: float



class QuizResultResponse(BaseModel):

    matches: List[MatchResult]

    user_fingerprint: List[float]

    dominant_trait: str