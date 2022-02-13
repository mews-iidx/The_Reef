from typing import Optional

from pydantic import BaseModel


class GetQuizResponse(BaseModel):
    question: str
    image_url: Optional[str]
    is_continue: bool

    class Config:
        orm_mode = True
