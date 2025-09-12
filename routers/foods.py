from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.models_orm import Food
from app.database import get_db

router = APIRouter()

@router.get("/search")
def search_foods(q: str = Query(..., min_length=1), db: Session = Depends(get_db)):
    results = db.query(Food).filter(Food.name.ilike(f"%{q}%")).all()
    return results