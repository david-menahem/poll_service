from typing import List

from fastapi import HTTPException, APIRouter
from starlette import status

from model.stats_model.choice_count_by_question_response import ChoiceCountByQuestionResponse
from model.stats_model.user_answer_response import UserAnswerResponse
from service import stats_service, question_service

router = APIRouter(
    prefix="/stats",
    tags=["stats"]
)


@router.get(path="/choices_selected_count_by_question/{question_id}", response_model=ChoiceCountByQuestionResponse, status_code=status.HTTP_200_OK)
async def get_choices_selected_count_by_question_id(question_id: int) -> ChoiceCountByQuestionResponse:
    try:
        question = await question_service.get_by_id(question_id)
        return await stats_service.get_choices_selected_count_by_question(question)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(path="/user_count_by_question/{question_id}", response_model=str, status_code=status.HTTP_200_OK)
async def get_user_count_by_question_id(question_id: int) -> str:
    try:
        return await stats_service.get_user_count_by_question_id(question_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(path="/user_answers/{user_id}", response_model=List[UserAnswerResponse], status_code=status.HTTP_200_OK)
async def get_user_answers_by_user_id(user_id: int) -> List[UserAnswerResponse]:
    try:
        return await stats_service.get_user_answers_by_user_id(user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(path="/user_answer_count/{user_id}", response_model=str, status_code=status.HTTP_200_OK)
async def get_user_answer_count_by_user_id(user_id: int) -> str:
    try:
        return await stats_service.get_answer_count_by_user_id(user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(path="/all_questions_and_choices_selected", response_model=List[ChoiceCountByQuestionResponse], status_code=status.HTTP_200_OK)
async def get_all_questions_and_choices_selected_count():
    try:
        return await stats_service.get_all_questions_and_choices_selected_count()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

