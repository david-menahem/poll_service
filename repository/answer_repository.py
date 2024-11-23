from typing import Optional

from model.answer import Answer
from repository.database import database

TABLE = "answer"


async def get_by_question_id_and_user_id(question_id: int, user_id: int) -> Optional[Answer]:
    query = f"SELECT * FROM {TABLE} WHERE question_id=:question_id AND user_id=:user_id"
    values = {"question_id": question_id, "user_id": user_id}
    result = await database.fetch_one(query, values)
    if result:
        return Answer(**result)
    else:
        return None


async def create(answer: Answer):
    query = f"""INSERT INTO {TABLE}
    (question_id, user_id, choice_id)
    VALUES (:question_id, :user_id, :choice_id)
    """
    values = {"question_id": answer.question_id, "user_id": answer.user_id, "choice_id": answer.choice_id}
    await database.execute(query, values)


async def update(answer: Answer):
    query = f"""
    UPDATE {TABLE} SET
    choice_id=:choice_id
    WHERE question_id=:question_id AND user_id=:user_id
    """
    values = {"question_id": answer.question_id,
              "user_id": answer.user_id, "choice_id": answer.choice_id}
    await database.execute(query, values)


async def delete_by_user_id(user_id: int):
    query = f"DELETE FROM {TABLE} WHERE user_id=:user_id"
    value = {"user_id": user_id}
    await database.execute(query, value)


async def delete_by_question_id(question_id: int):
    query = f"DELETE FROM {TABLE} WHERE question_id=:question_id"
    value = {"question_id": question_id}
    await database.execute(query, value)

