from typing import List

from pydantic import BaseModel

from models.behavior import Behavior


class CompactOption(BaseModel):
    text: str
    behaviors: List[Behavior]