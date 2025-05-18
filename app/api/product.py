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