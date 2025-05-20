from app.data.db import engine, Base
from app.models.models import Product

Base.metadata.create_all(bind=engine)

