from sqlalchemy import Column, String, Float
from app.data.db import Base

class Product(Base):
    __tablename__ = "product"

    id = Column(String, primary_key=True)
    name = Column(String)
    status = Column(String)
    aisle_id = Column(String)
    shelf_id = Column(String)
    x = Column(Float)
    y = Column(Float)
    shelf_position = Column(String)
    category_id = Column(String)