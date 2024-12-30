import random
from models import db, Product

categories = ['Electronics', 'Clothing', 'Home & Garden', 'Sports & Outdoors', 'Books', 'Toys & Games']
adjectives = ['Amazing', 'Fantastic', 'Incredible', 'Awesome', 'Superb', 'Excellent', 'Great', 'Premium', 'Deluxe']
nouns = ['Gadget', 'Widget', 'Device', 'Tool', 'Accessory', 'Item', 'Product', 'Solution', 'Innovation']

def generate_product():
    name = f"{random.choice(adjectives)} {random.choice(nouns)}"
    description = f"This {name.lower()} is perfect for all your needs. High-quality and durable."
    price = round(random.uniform(9.99, 999.99), 2)
    category = random.choice(categories)
    
    return Product(name=name, description=description, price=price, category=category)

def populate_database(app):
    with app.app_context():
        for _ in range(100):
            product = generate_product()
            db.session.add(product)
        db.session.commit()
        print("Database populated with 100 mock products.")
