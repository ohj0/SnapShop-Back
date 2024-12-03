from pydantic import BaseModel
from typing import List

class ItemBase(BaseModel):
    name: str
    price: float
    image_url: str

    class Config:
        orm_mode = True

class CategoryWithItems(BaseModel):
    id: int
    name: str
    items: List[ItemBase]

    class Config:
        orm_mode = True
