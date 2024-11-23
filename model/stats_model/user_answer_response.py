from pydantic import BaseModel


class UserAnswerResponse(BaseModel):
    title: str
    choice: str

