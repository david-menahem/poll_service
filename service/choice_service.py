from typing import List

from model.choice import Choice
from repository import choice_repository
from service import question_service


async def get_by_question_id(question_id: int) -> List[Choice]:
    await question_service.get_by_id(question_id)
    return await choice_repository.get_by_question_id(question_id)


async def create(choice: Choice):
    await choice_repository.create(choice)


async def delete(choice_id: int):
    await choice_repository.delete(choice_id)

