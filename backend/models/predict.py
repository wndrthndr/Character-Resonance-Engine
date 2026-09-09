from pydantic import BaseModel

class PredictedCharacter(BaseModel):
    
    name: str
    color: str
    image: str
    