import logging
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from database import get_db  
from models import Item  
from routers.categories import router as categories_router  
from fastapi import Query
from models import Category



app = FastAPI()




app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


app.mount("/static", StaticFiles(directory="static"), name="static")



app.include_router(categories_router, prefix="/api")



@app.get("/", response_class=HTMLResponse)
def get_items(db: Session = Depends(get_db)):
    
    items = db.query(Item).all()

    
    items_html = ""
    for item in items:
      
        image_path = f"/static/{item.image_url}"
        
       

        items_html += f"""
        <div>
            <h3>{item.name} - ${item.price}</h3>
            <img src="{image_path}" alt="{item.name}" width="200">
        </div>
        """

    return f"""
    <html>
        <head>
            <title>Items Page</title>
        </head>
        <body>
            <h1>Items for Sale</h1>
            <form method="get" action="/search">
                <input type="text" name="query" placeholder="Search for items" required>
                <button type="submit">Search</button>
            </form>
            <div>{items_html}</div>
        </body>
    </html>
    """

@app.get("/api/items/{category}")
def get_items_by_category(category: str, db: Session = Depends(get_db)):
    try:
        
        category_obj = db.query(Category).filter(Category.name.ilike(category)).first()

        
       
        if not category_obj:
            return {"message": f"No category found with the name '{category}'."}
        
       
        items = db.query(Item).filter(Item.category_id == category_obj.id).all()
        
        if items:
            return {
                "items": [
                    {"name": item.name, "price": item.price, "image_url": f"/static/{item.image_url}"}
                    for item in items
                ]
            }
        else:
            return {"message": f"No items found in category '{category}'."}
    except Exception as e:
        logging.error(f"Error occurred while fetching items for category '{category}': {e}")
        return {"message": "An error occurred while fetching the items."}

    

@app.get("/search/{query}")
def search_items(query: str, db: Session = Depends(get_db)):
    
    query = query.strip()

    
    items = db.query(Item).filter(Item.name.ilike(f"%{query}%")).all()

   
    if items:
        search_results = [
            {
                "name": item.name,
                "price": item.price,
                "image_url": f"/static/{item.image_url}"  
            }
            for item in items
        ]
        return {"items": search_results}
    else:
        return {"message": "No items found"}
