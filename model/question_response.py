from typing import List, Optional

from pydantic import BaseModel


class QuestionResponse(BaseModel):
    id: Optional[int] = None
    title: str
    choices: List[str]


