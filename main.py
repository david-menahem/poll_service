from fastapi import FastAPI

from controller.question_controller import router as question_router
from controller.answer_controller import router as answer_router
from controller.stats_controller import router as stats_router
from repository.database import database

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shut_down():
    await database.disconnect()


app.include_router(question_router)
app.include_router(answer_router)
app.include_router(stats_router)

