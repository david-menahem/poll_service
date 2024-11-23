from typing import List, Optional

from api.internalAPI import user_service
from model.answer import Answer
from model.answer_request import AnswerRequest
from repository import answer_repository
from service import choice_service, question_service


async def submit_survey(user_id: int, answers: List[AnswerRequest]) -> List[str]:
    user = await user_service.get_by_id(user_id)
    if user.is_registered:
        response = []
        for answer_request in answers:
            response.append(await process_answer(user_id, answer_request, False))
        response.append("Thank you for answering the survey")
        return response
    else:
        raise Exception(f"Sorry, user with id: {user_id} has not activated his account")


async def create(answer: Answer):
    await answer_repository.create(answer)


async def update(user_id: int, answer_request: AnswerRequest) -> str:
    user = await user_service.get_by_id(user_id)
    if user.is_registered:
        return await process_answer(user_id, answer_request, True)
    else:
        raise Exception(f"Sorry, user with id: {user_id} has not activated his account")


async def process_answer(user_id, answer_request: AnswerRequest, update_flag: bool) -> str:
    question = await question_service.get_by_title(answer_request.title)
    if question:
        choices = await choice_service.get_by_question_id(question.id)
        choice_id = 0
        for choice in choices:
            if answer_request.choice == choice.choice:
                choice_id = choice.id
                break

        if choice_id > 0:
            is_answered = await answer_repository.get_by_question_id_and_user_id(question.id, user_id)
            answer = Answer(question_id=question.id, user_id=user_id, choice_id=choice_id)
            if update_flag:
                if is_answered:
                    await answer_repository.update(answer)
                    response = f"Answer for: {question.title} has been updated"
                else:
                    response = f"User with id: {user_id} has not answered this question before - Nothing to update"
            else:
                if not is_answered:
                    await answer_repository.create(answer)
                    response = f"Question: {question.title} has been submitted"
                else:
                    response = f"You have already answered the question: {answer_request.title}"
        else:
            response = f"Choice: {answer_request.choice} does not exist"
    else:
        response = f"Question: {answer_request.title} does not exist"

    return response


async def delete_by_question_id(question_id: int):
    await answer_repository.delete_by_question_id(question_id)


async def delete_by_user_id(user_id: int):
    await user_service.get_by_id(user_id)
    await answer_repository.delete_by_user_id(user_id)

