from typing import List, Literal

from pydantic import BaseModel


class UserResponse(BaseModel):

    question_id: str

    selected_option: Literal[
        "A",
        "B",
        "C",
        "D"
    ]


class SubmitRequest(BaseModel):

    franchise: str

    responses: List[UserResponse]