from pydantic import BaseModel


class StartQuizRequest(BaseModel):

    franchise: str