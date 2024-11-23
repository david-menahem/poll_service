from typing import List

from api.internalAPI import user_service
from model.question import Question
from model.stats_model.choice_count_by_question_response import ChoiceCountByQuestionResponse
from model.stats_model.choice_count_response import ChoiceCountResponse
from model.stats_model.user_answer_response import UserAnswerResponse
from repository import stats
from service import question_service, choice_service


async def get_choices_selected_count_by_question_id(question_id: int) -> ChoiceCountByQuestionResponse:
    question = await question_service.get_by_id(question_id)
    choice_count = await get_choices_selected_count_by_question(question)
    return ChoiceCountByQuestionResponse(title=question.title, choices=choice_count)


async def get_user_count_by_question_id(question_id: int) -> str:
    await question_service.get_by_id(question_id)
    user_count = await stats.get_user_count_by_question_id(question_id)
    return f"The number of users that answered this question is: {user_count}"


async def get_user_answers_by_user_id(user_id: int) -> List[UserAnswerResponse]:
    await user_service.get_by_id(user_id)
    return await stats.get_user_answers_by_user_id(user_id)


async def get_answer_count_by_user_id(user_id: int) -> str:
    await user_service.get_by_id(user_id)
    answers_count = await stats.get_answer_count_by_user_id(user_id)
    return f"User with id: {user_id} has answered {answers_count} questions"


async def get_all_questions_and_choices_selected_count() -> List[ChoiceCountByQuestionResponse]:
    choice_count_by_question_response = []
    questions = await question_service.get_all()
    for question in questions:
        choice_count_by_question_response.append(await get_choices_selected_count_by_question(question))
    return choice_count_by_question_response


async def get_choices_selected_count_by_question(question: Question) -> ChoiceCountByQuestionResponse:
    choice_count_by_question = []
    choices = await choice_service.get_by_question_id(question.id)
    for choice in choices:
        choice_count = await stats.get_choice_selected_count(choice.id)
        choice = choice.choice
        choice_count_by_question.append(ChoiceCountResponse(choice=choice, choice_count=choice_count))
    return ChoiceCountByQuestionResponse(title=question.title, choices=choice_count_by_question)

