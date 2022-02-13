from pydantic import BaseModel


class PresentBase(BaseModel):
    name: str


class GetCategoriesResponse(PresentBase):
    count: int


class ChoosePresentResponse(PresentBase):
    image_path: str

    class Config:
        orm_mode = True
