from typing import List

import app.cruds.present as present_crud
import app.schemas.present as present_schema
from app.db import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get("/genre", response_model=List[present_schema.GetCategoriesResponse])
async def get_categories(db: AsyncSession = Depends(get_db)):
    return await present_crud.get_categories(db)


@router.get("/result/{genre_name}", response_model=present_schema.ChoosePresentResponse)
async def choose_present(genre_name, db: AsyncSession = Depends(get_db)):
    return await present_crud.choose_present(db, genre_name=genre_name)


@router.get("/present/reset")
async def reset_used_present(db: AsyncSession = Depends(get_db)):
    return await present_crud.reset_used_present(db)
