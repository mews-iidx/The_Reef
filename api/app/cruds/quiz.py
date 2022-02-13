import app.models.quiz as quiz_model
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession


async def get_quiz(db: AsyncSession):
    result: Result = await db.execute(
        select(quiz_model.Quiz)
        .filter(quiz_model.Quiz.is_used == 0)
        .order_by(quiz_model.Quiz.id)
    )

    quiz = result.first().Quiz
    response_quiz = quiz
    quiz.is_used = 1

    db.add(quiz)
    await db.commit()
    await db.refresh(quiz)

    return response_quiz
