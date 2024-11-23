from typing import List

from pydantic import BaseModel

from model.stats_model.choice_count_response import ChoiceCountResponse


class ChoiceCountByQuestionResponse(BaseModel):
    title: str
    choices: List[ChoiceCountResponse]



