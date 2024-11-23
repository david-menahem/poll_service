from typing import List

from pydantic import BaseModel


class AnswerRequest(BaseModel):
    title: str
    choice: str



    


