from pydantic import BaseModel


class ChoiceCountResponse(BaseModel):
    choice: str
    choice_count: int

