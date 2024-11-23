from pydantic import BaseModel


class AnswerResponse(BaseModel):
    title: str
    choice: str

