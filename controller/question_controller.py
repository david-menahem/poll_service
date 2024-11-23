from typing import List

from fastapi import APIRouter, HTTPException
from starlette import status

from model.question_request import QuestionRequest
from model.question_response import QuestionResponse
from service import question_service

router = APIRouter(
    prefix="/question",
    tags=["question"]
)


@router.get(path="/survey", response_model=List[QuestionResponse], status_code=status.HTTP_200_OK)
async def get_survey() -> List[QuestionResponse]:
    try:
        return await question_service.get_survey()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(path="/{question_id}", response_model=QuestionResponse, status_code=status.HTTP_200_OK)
async def get_by_id(question_id: int) -> QuestionResponse:
    try:
        return await question_service.get_question_and_choices_by_question_id(question_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post(path="/", response_model=QuestionResponse, status_code=status.HTTP_201_CREATED)
async def create(question_request: QuestionRequest) -> QuestionResponse:
    try:
        return await question_service.create(question_request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put(path="/{question_id}", response_model=QuestionResponse, status_code=status.HTTP_200_OK)
async def update(question_id: int, question_request: QuestionRequest) -> QuestionResponse:
    try:
        return await question_service.update(question_id, question_request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete(path="/{question_id}", status_code=status.HTTP_200_OK)
async def delete(question_id: int):
    try:
        return await question_service.delete(question_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
