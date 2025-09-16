from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Food(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    weight = Column(Float)
    calories = Column(Float)
    carbs = Column(Float)
    protein = Column(Float)
    fat = Column(Float)
    sodium = Column(Float)