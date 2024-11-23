from typing import List, Optional

from model.choice import Choice
from repository.database import database

TABLE = "choice"


async def get_by_question_id(question_id: int) -> List[Choice]:
    query = f"SELECT * FROM {TABLE} WHERE question_id=:question_id"
    value = {"question_id": question_id}
    results = await database.fetch_all(query, value)
    return [Choice(**result) for result in results]


async def create(choice: Choice):
    query = f"""
    INSERT INTO {TABLE}
    (question_id, choice)
    VALUES (:question_id, :choice)
    """
    values = {"question_id": choice.question_id, "choice": choice.choice}
    await database.execute(query, values)


async def update(choice: Choice):
    query = f"""
    UPDATE {TABLE} SET
    choice=:choice
    WHERE id=:choice_id AND question_id=:question_id
    """
    values = {"choice": choice.choice, "choice_id": choice.id, "question_id": choice.question_id}
    await database.execute(query, values)


async def delete(choice_id: int):
    query = f"DELETE FROM {TABLE} WHERE id=:choice_id"
    value = {"choice_id": choice_id}
    await database.execute(query, value)

