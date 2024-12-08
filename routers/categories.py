from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)


categories = []
category_id_counter = 1

@router.post("/")
def create_category(name: str):
    global category_id_counter
    new_category = {"id": category_id_counter, "name": name}
    categories.append(new_category)
    category_id_counter += 1
    return new_category

@router.get("/")
def get_categories():
    return categories

@router.get("/{category_id}")
def get_category(category_id: int):
    for category in categories:
        if category["id"] == category_id:
            return category
    raise HTTPException(status_code=404, detail="Category not found")
