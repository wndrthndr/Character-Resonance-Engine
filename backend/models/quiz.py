from typing import List

from pydantic import BaseModel

from models.question import CompactQuestion


class Quiz(BaseModel):

    franchise: str

    questions: List[CompactQuestion]