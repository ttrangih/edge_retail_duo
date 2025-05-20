from pydantic import BaseModel

class ProductSchema(BaseModel):
    id: str
    name: str
    status: str
    aisle_id: str
    shelf_id: str
    x: float
    y: float
    shelf_position: str
    category_id: str

    class Config:
        orm_mode = True
