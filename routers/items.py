from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Category
from schemas import CategoryWithItems
from database import get_db
from typing import List

router = APIRouter()

@router.get("/", response_model=List[CategoryWithItems])
def get_all_items(db: Session = Depends(get_db)):
    """
    Fetch all categories with their items from the database.
    """
    categories = db.query(Category).all()
    return categories
