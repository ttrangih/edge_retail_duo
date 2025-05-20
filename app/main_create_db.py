from app.data.db import Base, engine
from app.models.product import Product  # Hoặc models.models nếu đặt model ở đó

# Tạo các bảng từ model
Base.metadata.create_all(bind=engine)

