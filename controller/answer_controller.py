from typing import List

from fastapi import APIRouter, HTTPException
from starlette import status

from model.answer_request import AnswerRequest
from service import answer_service

router = APIRouter(
    prefix="/answer",
    tags=["answer"]
)


@router.post(path="/{user_id}", response_model=List[str], status_code=status.HTTP_201_CREATED)
async def submit_survey(user_id: int, answers: List[AnswerRequest]) -> List[str]:
    try:
        return await answer_service.submit_survey(user_id, answers)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put(path="/{user_id}", response_model=str, status_code=status.HTTP_200_OK)
async def update(user_id: int, answer_request: AnswerRequest) -> str:
    try:
        return await answer_service.update(user_id, answer_request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete(path="/delete_by_user_id/{user_id}", status_code=status.HTTP_200_OK)
async def delete_by_user_id(user_id: int):
    try:
        await answer_service.delete_by_user_id(user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))