from typing import List

from model.stats_model.user_answer_response import UserAnswerResponse
from repository.database import database

QUESTION_TABLE = "question"
OPTION_TABLE = "choice"
ANSWER_TABLE = "answer"


async def get_choice_selected_count(choice_id: int) -> int:
    query = f"""
    SELECT COUNT(choice_id) FROM {ANSWER_TABLE}
    WHERE choice_id=:choice_id
    GROUP BY choice_id
    """
    value = {"choice_id": choice_id}
    count = await database.fetch_one(query, value)
    if count:
        return count[0]
    else:
        return 0


async def get_user_count_by_question_id(question_id: int) -> int:
    query = f"""SELECT COUNT(question_id) AS user_count FROM {ANSWER_TABLE} 
    WHERE question_id=:question_id
    GROUP BY question_id
    """
    value = {"question_id": question_id}
    user_count = await database.fetch_one(query, value)
    if user_count:
        return user_count[0]
    else:
        return 0


async def get_user_answers_by_user_id(user_id: int) -> List[UserAnswerResponse]:
    query = f"""
    SELECT question.title, choices.choice FROM
    {ANSWER_TABLE} AS answer JOIN {QUESTION_TABLE} AS question JOIN {OPTION_TABLE} AS choices 
    ON answer.question_id=question.id AND answer.choice_id=choices.id
    WHERE answer.user_id=:user_id
    """
    value = {"user_id": user_id}
    results = await database.fetch_all(query, value)
    return [UserAnswerResponse(**result) for result in results]


async def get_answer_count_by_user_id(user_id: int) -> int:
    query = f"""SELECT COUNT(user_id) FROM {ANSWER_TABLE} 
    WHERE user_id=:user_id
    GROUP BY user_id
    """
    value = {"user_id": user_id}
    answer_count = await database.fetch_one(query, value)
    if answer_count:
        return answer_count[0]
    else:
        return 0

