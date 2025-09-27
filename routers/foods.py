from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import Food
from app.database import get_db

router = APIRouter(prefix="/foods", tags=["foods"])

@router.get("/search")
def search_foods(query: str = Query(..., min_length=1), db: Session = Depends(get_db)):
    results = (
        db.query(
            Food.name.label("name"),
            func.avg(Food.calories).label("calories"),
            func.avg(Food.protein).label("protein"),
            func.avg(Food.carbs).label("carbs"),
            func.avg(Food.fat).label("fat"),
            func.count(Food.id).label("variants")
        )
        .filter(Food.name.ilike(f"%{query}%"))
        .group_by(Food.name)
        .order_by(Food.name.asc())
        .all()
    )

    return [
        {
            "name": r.name,
            "calories": round(r.calories, 2) if r.calories else None,
            "protein": round(r.protein, 2) if r.protein else None,
            "carbs": round(r.carbs, 2) if r.carbs else None,
            "fat": round(r.fat, 2) if r.fat else None,
            "variants": r.variants
        }
        for r in results
    ]

@router.get("/detail")
def get_food_detail(name: str = Query(..., min_length=1), db: Session = Depends(get_db)):
    result = (
        db.query(
            func.avg(Food.calories).label("calories"),
            func.avg(Food.carbs).label("carbs"),
            func.avg(Food.protein).label("protein"),
            func.avg(Food.fat).label("fat"),
            func.avg(Food.sugars).label("sugars"),
            func.avg(Food.fiber).label("fiber"),
            func.avg(Food.sodium).label("sodium"),
            func.avg(Food.cholesterol).label("cholesterol"),
            func.avg(Food.saturated_fat).label("saturated_fat"),
            func.avg(Food.trans_fat).label("trans_fat"),
            func.count(Food.id).label("variants")
        )
        .filter(Food.name == name)
        .first()
    )

    if not result:
        return {"error": "해당 자료를 찾을 수 없습니다."}

    return {
        "name": name,
        "calories": round(result.calories, 2),
        "carbs": round(result.carbs, 2),
        "protein": round(result.protein, 2),
        "fat": round(result.fat, 2),
        "sugars": round(result.sugars, 2),
        "fiber": round(result.fiber, 2),
        "sodium": round(result.sodium, 2),
        "cholesterol": round(result.cholesterol, 2),
        "saturated_fat": round(result.saturated_fat, 2),
        "trans_fat": round(result.trans_fat, 2),
        "variants": result.variants
    }

@router.get("/autocomplete")
def autocomplete(
    query: str = Query(..., min_length=1),
    limit: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db),
):
    rows = (
        db.query(Food.id, Food.name)
        .filter(Food.name.ilike(f"%{query}%"))
        .distinct(Food.name)
        .order_by(Food.name.asc())
        .limit(limit)
        .all()
    )
    return [{"id": r.id, "name": r.name} for r in rows]
