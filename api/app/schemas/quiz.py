from pydantic import BaseModel


class Quiz(BaseModel):
    id: int
    order_number: int
    question: str
    answer: str
