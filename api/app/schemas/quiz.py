from typing import Optional

from pydantic import BaseModel


class GetQuizResponse(BaseModel):
    quiz_id: int
    question: str
    image_url: Optional[str]
    is_enable: bool

    class Config:
        orm_mode = True


class GetAnswerRequest(BaseModel):
    quiz_id: int


class GetAnswerResponse(BaseModel):
    quiz_id: int
    answer: str
