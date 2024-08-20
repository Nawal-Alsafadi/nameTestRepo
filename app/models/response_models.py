from pydantic import BaseModel

class NameResponse(BaseModel):
    message: str