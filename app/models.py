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
    sugars = Column(Float, nullable=True)
    fiber = Column(Float, nullable=True)
    cholesterol = Column(Float, nullable=True)
    saturated_fat = Column(Float, nullable=True)
    trans_fat = Column(Float, nullable=True)