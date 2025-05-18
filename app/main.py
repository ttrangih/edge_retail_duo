from fastapi import FastAPI
from app.api import product

app = FastAPI(title="Edge Retail Duo")

# Đăng ký router
app.include_router(product.router, prefix="/product")

