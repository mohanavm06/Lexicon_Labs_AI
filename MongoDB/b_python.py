from datetime import datetime
from pprint import pprint
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMs=3000)
db = client["webshop"]

# 1
for product in db.products.find({"category": "Accessories"}):
    print(product.get("name", "Unknown"))

# 2
for customer in db.customers.find({"city": "Göteborg"}):
    print(customer["first_name"], customer["last_name"])

# 3
for product in db.products.find():
    print(f"{product['name']} ({product['price']} kr)")

# 4
no_of_customers = db.customers.count_documents({"city": "Uppsala"})
print(no_of_customers)

# 5
product = db.products.find_one({"name": "Sandals"})
print(product["stock"])

# 6
for customer in db.customers.find({"newsletter": True}):
    print(customer["first_name"])

# 7
result = db.customers.insert_one({
    "first_name": "Harry",
    "last_name": "Potter",
    "email": "harry@example.com",
    "city": "Stockholm",
    "joined": datetime(2024, 3, 14),
    "newsletter": True
})

customer = db.customers.find_one({"email": "harry@example.com"})
print(result.inserted_id)
pprint(customer)

# 8
db.products.insert_many([
    {
        "_id": 13,
        "name": "Wool Scarf",
        "category": "Accessories",
        "price": 299,
        "stock": 35,
        "tags": ["winter", "wool"],
        "details": {"color": "grey", "material": "wool"}
    },
    {
        "_id": 14,
        "name": "Hiking Boots",
        "category": "Shoes",
        "price": 1599,
        "stock": 9,
        "tags": ["outdoor", "waterproof"],
        "details": {"color": "brown", "material": "leather"},
        "sizes": [38, 39, 40, 41, 42, 43]
    }
])

no_of_products = db.products.count_documents({})
print(no_of_products)

# 9
for customer in db.customers.find():
    city = customer.get("city") or "unknown"
    print(f"{customer['first_name']} {customer['last_name']} ({city})")

# 10
for order in db.orders.find():
    print(f"Order {order['_id']}: {len(order['items'])} items")