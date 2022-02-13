import app.cruds.present as present_crud
from app.db import get_db_session
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get("/genre")
async def get_category(db: AsyncSession = Depends(get_db_session)):
    return await present_crud.get_category(db)


@router.get("/result/{genre_name}")
async def choose_present(genre_name, db: AsyncSession = Depends(get_db_session)):
    return await present_crud.choose_present(db, genre_name=genre_name)
