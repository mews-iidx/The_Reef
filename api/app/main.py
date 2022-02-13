from fastapi import FastAPI

from app.routers import present, quiz

app = FastAPI()
app.include_router(quiz.router)
app.include_router(present.router)


@app.get("/hello")
async def hello():
    return {"message": "hello world!"}
