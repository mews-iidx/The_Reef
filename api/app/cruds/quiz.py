import app.models.quiz as quiz_model
from sqlalchemy import exists, select, update
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession


async def get_quiz(db: AsyncSession) -> quiz_model.Quiz:
    result: Result = await db.execute(
        select(quiz_model.Quiz.id, quiz_model.Quiz.question, quiz_model.Quiz.image_url)
        .filter(quiz_model.Quiz.is_used == 0)
        .order_by(quiz_model.Quiz.id)
    )
    quiz = result.first()
    if quiz is None:
        return {
            "quiz_id": "",
            "question": "",
            "image_url": "",
            "is_enable": False,
        }

    quiz_id = quiz.id

    await update_used_quiz(db, quiz_id)

    result: Result = await db.execute(
        exists().where(quiz_model.Quiz.is_used == 0).select()
    )

    return {
        "quiz_id": quiz.id,
        "question": quiz.question,
        "image_url": quiz.image_url,
        "is_enable": True,
    }


async def update_used_quiz(db: AsyncSession, quiz_id: int):
    await db.execute(
        update(quiz_model.Quiz).where(quiz_model.Quiz.id == quiz_id).values(is_used=1)
    )
    await db.commit()


async def reset_used_quiz(db: AsyncSession):
    await db.execute(update(quiz_model.Quiz).values(is_used=0))
    await db.commit()
