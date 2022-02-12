from fastapi import FastAPI

from app.routers import quiz

app = FastAPI()
app.include_router(quiz.router)


@app.get("/hello")
async def hello():
    return {"message": "hello world!"}
