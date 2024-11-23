from typing import Optional

from pydantic import BaseModel


class Choice(BaseModel):
    id: Optional[int] = None
    question_id: int
    choice: str



