from fastapi import FastAPI

from app.routers import present, quiz

app = FastAPI()
app.include_router(quiz.router)
app.include_router(present.router)
