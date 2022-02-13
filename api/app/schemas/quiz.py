from typing import Optional

from pydantic import BaseModel


class GetQuizResponse(BaseModel):
    quiz: str
    image_url: Optional[str]
