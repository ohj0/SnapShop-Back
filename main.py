import logging
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy.orm import Session
from database import get_db  # Import your database session utility
from models import Item  # Import your SQLAlchemy models

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


# Search route
@app.get("/search")
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
        return JSONResponse(content={"items": search_results})
    else:
        return JSONResponse(content={"message": "No items found"})
