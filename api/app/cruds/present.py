import random

import app.models.present as present_model
from sqlalchemy import func, select, update
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession


async def get_categories(db: AsyncSession):
    result: Result = await db.execute(
        select(
            present_model.PresentCategory.name,
            func.count(present_model.PresentCategory.name),
        )
        .join(
            present_model.Present,
            present_model.Present.present_category_id
            == present_model.PresentCategory.id,
        )
        .filter(present_model.Present.is_used == 0)
        .group_by(present_model.PresentCategory.name)
    )

    return result.all()


async def choose_present(db: AsyncSession, genre_name):
    result: Result = await db.execute(
        select(present_model.Present)
        .join(
            present_model.PresentCategory,
            present_model.Present.present_category_id
            == present_model.PresentCategory.id,
        )
        .filter(present_model.PresentCategory.name == genre_name)
        .filter(present_model.Present.is_used == 0)
    )

    result = random.choice(result.all())
    present = result[0]

    result[0].is_used = 1

    db.add(result[0])
    await db.commit()
    await db.refresh(result[0])

    return present


async def reset_used_present(db: AsyncSession):
    await db.execute(update(present_model.Present).values(is_used=0))
    await db.commit()
