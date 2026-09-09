from pydantic import BaseModel

from models.response import UserResponse


class AnswerRequest(BaseModel):

    session_id: str

    response: UserResponse
    