import app.cruds.quiz as quiz_crud
import app.schemas.quiz as quiz_schema
from app.db import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get("/quiz", response_model=quiz_schema.GetQuizResponse)
async def get_quiz(db: AsyncSession = Depends(get_db)):
    return await quiz_crud.get_quiz(db)


@router.get("/quiz/reset/")
async def reset_used_quiz(db: AsyncSession = Depends(get_db)):
    return await quiz_crud.reset_used_quiz(db)
