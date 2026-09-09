from typing import Dict, Literal

from pydantic import BaseModel

from models.option import CompactOption


class CompactQuestion(BaseModel):

    id: str

    scope: Literal["GLOBAL", "FRANCHISE"]

    franchise: str

    question: str

    options: Dict[
        Literal["A", "B", "C", "D"],
        CompactOption
    ]