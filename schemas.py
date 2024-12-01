from pydantic import BaseModel
from typing import Optional, List

# Category Schemas
class CategoryBase(BaseModel):
    name: str  # Shared field for both creation and response

class CategoryCreate(CategoryBase):
    pass  # Inherits all fields from CategoryBase for creation

class Category(CategoryBase):
    id: int  # ID is included in the response
    items: List["Item"] = []  # Include related items as a list (optional)

    class Config:
        orm_mode = True  # Enable ORM compatibility with SQLAlchemy

# Item Schemas
class ItemBase(BaseModel):
    name: str  # Shared field for both creation and response
    price: int  # Shared field
    image_url: str = None  # Optional field for the image URL

class ItemCreate(ItemBase):
    category_id: int  # Required field for linking to a category

class Item(ItemBase):
    id: int  # ID is included in the response
    category_id: int  # Include the category ID for reference

    class Config:
        orm_mode = True  # Enable ORM compatibility with SQLAlchemy
