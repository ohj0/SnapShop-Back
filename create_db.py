from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
from models import Category, Item

# Create the tables in the database
Base.metadata.create_all(bind=engine)

# Create a session and populate the database
def create_initial_data(db: Session):
    # Create categories
    sport_category = Category(name="Sport")
    shoes_category = Category(name="Shoes")
    cosmetics_category = Category(name="Cosmetics")
    fashion_category = Category(name="Fashion")
    electronics_category = Category(name="Electronics")

    db.add_all([sport_category, shoes_category, cosmetics_category, fashion_category, electronics_category])
    db.commit()

    # Create items with image URLs for each category
    sport_items = [
        Item(name="Soccer Ball", price=25, category_id=sport_category.id, image_url="images/soccer_ball.jpeg"),
        Item(name="Tennis Racket", price=50, category_id=sport_category.id, image_url="images/tennis_racket.jpg"),
        Item(name="Running Shoes", price=80, category_id=sport_category.id, image_url="images/running_shoes.jpg"),
        Item(name="Basketball", price=30, category_id=sport_category.id, image_url="images/basketball.jpg"),
        Item(name="Baseball Bat", price=45, category_id=sport_category.id, image_url="images/baseball_bat.jpg"),
        Item(name="Yoga Mat", price=20, category_id=sport_category.id, image_url="images/yoga_mat.jpg"),
        Item(name="Swimming Goggles", price=15, category_id=sport_category.id, image_url="images/swimming_goggles.jpg"),
        Item(name="Boxing Gloves", price=35, category_id=sport_category.id, image_url="images/boxing_gloves.jpg"),
        Item(name="Cricket Ball", price=10, category_id=sport_category.id, image_url="images/cricket_ball.jpg"),
        Item(name="Skipping Rope", price=12, category_id=sport_category.id, image_url="images/skipping_rope.jpg"),
    ]
    shoes_items = [
        Item(name="Leather Boots", price=120, category_id=shoes_category.id, image_url="images/leather_boots.jpg"),
        Item(name="Sneakers", price=60, category_id=shoes_category.id, image_url="images/sneakers.jpg"),
        Item(name="Sandals", price=40, category_id=shoes_category.id, image_url="images/sandals.jpg"),
        Item(name="High Heels", price=90, category_id=shoes_category.id, image_url="images/high_heels.jpg"),
        Item(name="Flip Flops", price=20, category_id=shoes_category.id, image_url="images/flip_flops.jpg"),
        Item(name="Ankle Boots", price=110, category_id=shoes_category.id, image_url="images/ankle_boots.jpg"),
        Item(name="Running Trainers", price=85, category_id=shoes_category.id, image_url="images/running_trainers.jpg"),
        Item(name="Loafers", price=70, category_id=shoes_category.id, image_url="images/loafers.jpg"),
        Item(name="Slippers", price=25, category_id=shoes_category.id, image_url="images/slippers.jpg"),
        Item(name="Clogs", price=50, category_id=shoes_category.id, image_url="images/clogs.jpg"),
    ]
    cosmetics_items = [
        Item(name="Lipstick", price=15, category_id=cosmetics_category.id, image_url="images/lipstick.jpg"),
        Item(name="Face Cream", price=30, category_id=cosmetics_category.id, image_url="images/face_cream.jpg"),
        Item(name="Shampoo", price=10, category_id=cosmetics_category.id, image_url="images/shampoo.jpg"),
        Item(name="Eyeliner", price=12, category_id=cosmetics_category.id, image_url="images/eyeliner.jpg"),
        Item(name="Mascara", price=20, category_id=cosmetics_category.id, image_url="images/mascara.jpg"),
        Item(name="Foundation", price=35, category_id=cosmetics_category.id, image_url="images/foundation.jpg"),
        Item(name="Blush", price=18, category_id=cosmetics_category.id, image_url="images/blush.jpg"),
        Item(name="Nail Polish", price=8, category_id=cosmetics_category.id, image_url="images/nail_polish.jpg"),
        Item(name="Perfume", price=60, category_id=cosmetics_category.id, image_url="images/perfume.jpg"),
        Item(name="Makeup Remover", price=14, category_id=cosmetics_category.id, image_url="images/makeup_remover.jpg"),
    ]
    fashion_items = [
        Item(name="Jeans", price=40, category_id=fashion_category.id, image_url="images/jeans.jpg"),
        Item(name="T-Shirt", price=20, category_id=fashion_category.id, image_url="images/tshirt.jpg"),
        Item(name="Jacket", price=100, category_id=fashion_category.id, image_url="images/jacket.jpg"),
        Item(name="Sweater", price=50, category_id=fashion_category.id, image_url="images/sweater.jpg"),
        Item(name="Skirt", price=35, category_id=fashion_category.id, image_url="images/skirt.jpg"),
        Item(name="Dress", price=70, category_id=fashion_category.id, image_url="images/dress.jpg"),
        Item(name="Blazer", price=90, category_id=fashion_category.id, image_url="images/blazer.jpg"),
        Item(name="Shirt", price=30, category_id=fashion_category.id, image_url="images/shirt.jpg"),
        Item(name="Trousers", price=45, category_id=fashion_category.id, image_url="images/trousers.jpg"),
        Item(name="Belt", price=15, category_id=fashion_category.id, image_url="images/belt.jpg"),
    ]
    electronics_items = [
        Item(name="Smartphone", price=500, category_id=electronics_category.id, image_url="images/smartphone.jpg"),
        Item(name="Laptop", price=1000, category_id=electronics_category.id, image_url="images/laptop.jpg"),
        Item(name="Headphones", price=80, category_id=electronics_category.id, image_url="images/headphones.jpg"),
        Item(name="Smartwatch", price=150, category_id=electronics_category.id, image_url="images/smartwatch.jpg"),
        Item(name="Camera", price=400, category_id=electronics_category.id, image_url="images/camera.jpg"),
        Item(name="Tablet", price=300, category_id=electronics_category.id, image_url="images/tablet.jpg"),
        Item(name="Gaming Console", price=600, category_id=electronics_category.id, image_url="images/gaming_console.jpg"),
        Item(name="Bluetooth Speaker", price=50, category_id=electronics_category.id, image_url="images/bluetooth_speaker.jpg"),
        Item(name="External Hard Drive", price=120, category_id=electronics_category.id, image_url="images/external_hard_drive.jpg"),
        Item(name="Monitor", price=200, category_id=electronics_category.id, image_url="images/monitor.jpg"),
    ]

    db.add_all(sport_items + shoes_items + cosmetics_items + fashion_items + electronics_items)
    db.commit()

    print("Initial categories and items with images created!")



# Create a session and populate the database
def main():
    db = SessionLocal()
    try:
        create_initial_data(db)
    finally:
        db.close()

if __name__ == "__main__":
    main()
