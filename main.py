import logging
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from database import get_db  # Import your database session utility
from models import Item  # Import your SQLAlchemy models
from routers.categories import router as categories_router  # Correct import for categories.py inside the router folder
from fastapi import Query
from models import Category



app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Allow CORS for all domains (for Android to make requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with specific URLs like "http://localhost:3000"
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Mount the 'static' folder to serve static files (images) from the 'static' directory
app.mount("/static", StaticFiles(directory="static"), name="static")


# Include the categories router
app.include_router(categories_router, prefix="/api")


# Home route with search form
@app.get("/", response_class=HTMLResponse)
def get_items(db: Session = Depends(get_db)):
    # Retrieve all items from the database
    items = db.query(Item).all()

    # Generate HTML content for displaying items with images
    items_html = ""
    for item in items:
        # Assuming 'item.image_url' contains the image filename
        image_path = f"/static/{item.image_url}"
        
        # Log the image path for debugging purposes
        logging.debug(f"Image Path: {image_path}")

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
        # Fetch the category by name
        category_obj = db.query(Category).filter(Category.name.ilike(category)).first()

        
        # If the category doesn't exist, return a message
        if not category_obj:
            return {"message": f"No category found with the name '{category}'."}
        
        # Fetch the items for the category
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

    
# Search route
@app.get("/search/{query}")
def search_items(query: str, db: Session = Depends(get_db)):
    # Clean up query string
    query = query.strip()

    # Query the database based on the search query
    items = db.query(Item).filter(Item.name.ilike(f"%{query}%")).all()

    # Prepare the response data in a JSON-friendly format
    if items:
        search_results = [
            {
                "name": item.name,
                "price": item.price,
                "image_url": f"/static/{item.image_url}"  # Assumes 'image_url' is a file name
            }
            for item in items
        ]
        return {"items": search_results}
    else:
        return {"message": "No items found"}
