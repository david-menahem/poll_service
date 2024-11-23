from typing import List, Optional

from model.question import Question
from repository.database import database

TABLE = "question"


async def get_all() -> List[Question]:
    query = f"SELECT * FROM {TABLE}"
    results = await database.fetch_all(query)
    questions = [Question(**result) for result in results]
    return questions


async def get_by_id(question_id: int) -> Optional[Question]:
    query = f"SELECT * FROM {TABLE} WHERE id=:question_id"
    value = {"question_id": question_id}
    result = await database.fetch_one(query, value)
    if result:
        return Question(**result)
    else:
        return None


async def get_by_title(title: str) -> Optional[Question]:
    query = f"SELECT * FROM {TABLE} WHERE title=:title"
    value = {"title": title}
    result = await database.fetch_one(query, value)
    if result:
        return Question(**result)
    else:
        return None


async def create(question: Question) -> Question:
    query = f"""
    INSERT INTO {TABLE}
    (title)
    VALUES (:title)
    """
    value = {"title": question.title}
    async with database.transaction():
        await database.execute(query, value)
        last_insert_id = await database.fetch_one("SELECT LAST_INSERT_ID()")
    return await get_by_id(last_insert_id[0])


async def update(question: Question) -> Question:
    query = f"""
    UPDATE {TABLE} SET
    title=:title
    WHERE id=:question_id
    """
    values = {"title": question.title, "question_id": question.id}
    await database.execute(query, values)
    return await get_by_id(question.id)


async def delete(question_id: int):
    query = f"DELETE FROM {TABLE} WHERE id=:question_id"
    value = {"question_id": question_id}
    await database.execute(query, value)
