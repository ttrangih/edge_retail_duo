from sqlalchemy.orm import Session
from app.data.db import SessionLocal
from app.models.models import Product
from fastapi import HTTPException

# 🔁 Sử dụng database thay vì đọc file JSON

def find_product(product_id: str):
    db: Session = SessionLocal()
    product = (
        db.query(Product)
        .filter(Product.id.ilike(product_id))
        .first()
    )
    db.close()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


def get_product_status(product_id: str):
    product = find_product(product_id)
    return {"product_id": product.id, "status": product.status}


def get_shelf_location(product_id: str):
    product = find_product(product_id)
    return {
        "product_id": product.id,
        "location": {
            "aisle_id": product.aisle_id,
            "shelf_id": product.shelf_id,
            "location": {"x": product.x, "y": product.y},
            "shelf_position": product.shelf_position
        }
    }


def get_product_info(product_id: str):
    product = find_product(product_id)
    return {
        "product_id": product.id,
        "name": product.name,
        "status": product.status,
        "shelf_location": {
            "aisle_id": product.aisle_id,
            "shelf_id": product.shelf_id,
            "location": {"x": product.x, "y": product.y},
            "shelf_position": product.shelf_position
        }
    }


def get_products_by_category(category_id: str):
    db: Session = SessionLocal()
    products = (
        db.query(Product)
        .filter(Product.category_id.ilike(category_id))
        .all()
    )
    db.close()

    if not products:
        raise HTTPException(status_code=404, detail="Category not found")

    return {
        "category": category_id,
        "products": [
            {
                "product_id": p.id,
                "name": p.name,
                "status": p.status,
                "shelf_location": {
                    "aisle_id": p.aisle_id,
                    "shelf_id": p.shelf_id,
                    "location": {"x": p.x, "y": p.y},
                    "shelf_position": p.shelf_position
                }
            }
            for p in products
        ]
    }


def find_products_with_status_and_location(keyword: str):
    db: Session = SessionLocal()
    products = (
        db.query(Product)
        .filter(Product.name.ilike(f"%{keyword}%"))
        .all()
    )
    db.close()

    if not products:
        raise HTTPException(status_code=404, detail="No products match your keyword")

    return [
        {
            "product_id": p.id,
            "name": p.name,
            "status": p.status,
            "shelf_location": {
                "aisle_id": p.aisle_id,
                "shelf_id": p.shelf_id,
                "location": {"x": p.x, "y": p.y},
                "shelf_position": p.shelf_position
            }
        }
        for p in products
    ]
