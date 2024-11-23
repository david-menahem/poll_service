from typing import Optional

from pydantic import BaseModel


class QuestionRequest(BaseModel):
    title: str
    first_choice: str
    second_choice: str
    third_choice: str
    forth_choice: str

    
