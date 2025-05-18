import json
from pathlib import Path
from fastapi import HTTPException

MOCK_FILE = Path("app/data/mock_data.json")

def load_mock_data():
    with open(MOCK_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def find_product(product_id: str):
    data = load_mock_data()
    for category in data.get("categories", []):
        for product in category.get("products", []):
            if product["id"].lower() == product_id.lower():
                return product
    raise HTTPException(status_code=404, detail="Product not found")


def get_product_status(product_id: str):
    product = find_product(product_id)
    return {"product_id": product["id"], "status": product["status"]}

def get_shelf_location(product_id: str):
    product = find_product(product_id)
    return {"product_id": product["id"], "location": product["shelf_location"]}

def get_product_info(product_id: str):
    product = find_product(product_id)
    return product

def get_products_by_category(category_id: str):
    data = load_mock_data()
    category = next(
    (cat for cat in data["categories"] if cat["id"].lower() == category_id.lower()),
    None
)
    
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return {
        "category": category["name"],
        "products": category["products"]
    }

def find_products_by_keyword(keyword: str):
    data = load_mock_data()
    matches = []

    for category in data.get("categories", []):
        for product in category.get("products", []):
            if keyword.lower() in product["name"].lower():
                matches.append(product)

    if not matches:
        raise HTTPException(status_code=404, detail="No products match your keyword")

    return matches

