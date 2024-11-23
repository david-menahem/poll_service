from typing import List, Optional

from model.choice import Choice
from model.question import Question
from model.question_request import QuestionRequest
from model.question_response import QuestionResponse
from repository import question_repository
from service import choice_service, answer_service


async def get_all() -> List[Question]:
    return await question_repository.get_all()


async def get_survey() -> List[QuestionResponse]:
    questions = await question_repository.get_all()
    questions_response = []
    for question in questions:
        choices = await choice_service.get_by_question_id(question.id)
        choices = [choice.choice for choice in choices]
        question_response = QuestionResponse(id=question.id, title=question.title, choices=choices)
        questions_response.append(question_response)

    return questions_response


async def get_by_id(question_id) -> Question:
    question = await question_repository.get_by_id(question_id)
    if question:
        return question
    else:
        raise Exception(f"Question with id {question_id} does not exists")


async def get_by_title(title: str) -> Optional[Question]:
    question = await question_repository.get_by_title(title)
    if question:
        return question
    else:
        return None


async def get_question_and_choices_by_question_id(question_id: int) -> QuestionResponse:
    question = await get_by_id(question_id)
    choices = await choice_service.get_by_question_id(question_id)
    choices = [choice.choice for choice in choices]
    return QuestionResponse(id=question.id, title=question.title, choices=choices)


async def create(question_request: QuestionRequest) -> QuestionResponse:
    question = Question(title=question_request.title)
    question = await question_repository.create(question)

    first_choice = Choice(question_id=question.id, choice=question_request.first_choice)
    second_choice = Choice(question_id=question.id, choice=question_request.second_choice)
    third_choice = Choice(question_id=question.id, choice=question_request.third_choice)
    forth_choice = Choice(question_id=question.id, choice=question_request.forth_choice)

    await choice_service.create(first_choice)
    await choice_service.create(second_choice)
    await choice_service.create(third_choice)
    await choice_service.create(forth_choice)
    choices = [first_choice.choice, second_choice.choice, third_choice.choice, forth_choice.choice]

    return QuestionResponse(id=question.id, title=question.title, choices=choices)


async def update(question_id, question_request: QuestionRequest) -> QuestionResponse:
    await get_by_id(question_id)
    await delete(question_id)
    question = await question_repository.create(Question(title=question_request.title))

    first_choice = Choice(question_id=question.id, choice=question_request.first_choice)
    second_choice = Choice(question_id=question.id, choice=question_request.second_choice)
    third_choice = Choice(question_id=question.id, choice=question_request.third_choice)
    forth_choice = Choice(question_id=question.id, choice=question_request.forth_choice)

    await choice_service.create(first_choice)
    await choice_service.create(second_choice)
    await choice_service.create(third_choice)
    await choice_service.create(forth_choice)
    choices = [first_choice.choice, second_choice.choice, third_choice.choice, forth_choice.choice]

    return QuestionResponse(id=question.id, title=question.title, choices=choices)


async def delete(question_id):
    await get_by_id(question_id)
    await answer_service.delete_by_question_id(question_id)
    choices = await choice_service.get_by_question_id(question_id)
    [await choice_service.delete(choice.id) for choice in choices]
    await question_repository.delete(question_id)

