import app.cruds.quiz as quiz_crud
from app.db import get_db_session
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get("/quiz")
async def get_quiz(db: AsyncSession = Depends(get_db_session)):
    return await quiz_crud.get_quiz(db)
