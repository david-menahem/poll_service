from typing import Optional

from pydantic import BaseModel


class Answer(BaseModel):
    id: Optional[int] = None
    question_id: int
    user_id: int
    choice_id: int

