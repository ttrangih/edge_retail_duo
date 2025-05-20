from fastapi import APIRouter, HTTPException
from app.services.product_service import get_product_status, get_shelf_location, get_product_info, get_products_by_category
from typing import Dict

router = APIRouter()

@router.get("/status")
def api_get_product_status(product_id: str) -> Dict:
    return get_product_status(product_id)

@router.get("/location")
def api_get_shelf_location(product_id: str) -> Dict:
    return get_shelf_location(product_id)

@router.get("/info")
def api_get_product_info(product_id: str) -> Dict:
    return get_product_info(product_id)

@router.get("/category")
def get_product_category(category_id: str):
    return get_products_by_category(category_id)

@router.get("/search")
def search_by_keyword(name: str):
    from app.services.product_service import find_products_with_status_and_location
    return find_products_with_status_and_location(name)

from fastapi import Depends
from sqlalchemy.orm import Session
from app.data.db import SessionLocal
from app.models.product import Product
from app.models.schemas import ProductSchema

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProductSchema)
def create_product(product: ProductSchema, db: Session = Depends(get_db)):
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get("/", response_model=list[ProductSchema])
def read_all_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.get("/{product_id}", response_model=ProductSchema)
def read_product(product_id: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=ProductSchema)
def update_product(product_id: str, updated: ProductSchema, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in updated.dict().items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)
    return product

@router.delete("/{product_id}")
def delete_product(product_id: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"message": f"Product {product_id} deleted successfully"}
