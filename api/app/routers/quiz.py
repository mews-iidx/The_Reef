from fastapi import APIRouter

router = APIRouter()


@router.get("/quiz")
async def start_quiz():
    pass


@router.get("/quiz/{quiz_id}")
async def get_quiz():
    pass
