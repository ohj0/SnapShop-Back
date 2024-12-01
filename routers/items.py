from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Item, Category
from schemas import ItemCreate, Item
from database import get_db

router = APIRouter(
    prefix="/items",
    tags=["items"],
)

@router.post("/", response_model=Item)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    # Ensure the category exists before adding an item
    db_category = db.query(Category).filter(Category.id == item.category_id).first()
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    db_item = Item(name=item.name, price=item.price, category_id=item.category_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/", response_model=list[Item])
def get_items(db: Session = Depends(get_db)):
    return db.query(Item).all()

@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
