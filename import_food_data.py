import pandas as pd
from app.models import Food
from app.database import SessionLocal, engine, Base
import re

Base.metadata.create_all(bind=engine)

df = pd.read_excel("data/20250408_음식DB.xlsx")

df.rename(columns={
    '식품명': 'name',
    '영양성분함량기준량': 'weight',
    '에너지(kcal)': 'calories',
    '탄수화물(g)': 'carbs',
    '단백질(g)': 'protein',
    '지방(g)': 'fat',
    '나트륨(mg)': 'sodium',
    '당류(g)': 'sugars',
    '식이섬유(g)': 'fiber',
    '콜레스테롤(mg)': 'cholesterol',
    '포화지방산(g)': 'saturated_fat',
    '트랜스지방산(g)': 'trans_fat'
}, inplace=True)

def extract_numeric_weight(val):
    if pd.isna(val):
        return 0.0
    match = re.search(r'\d+(\.\d+)?', str(val))
    return float(match.group()) if match else 0.0

df['weight'] = df['weight'].apply(extract_numeric_weight)

df.fillna(0.0, inplace=True)

db = SessionLocal()

for _, row in df.iterrows():
    food = Food(
        name=row['name'],
        weight=row['weight'],
        calories=row['calories'],
        carbs=row['carbs'],
        protein=row['protein'],
        fat=row['fat'],
        sodium=row['sodium'],
        sugars=row['sugars'],
        fiber=row['fiber'],
        cholesterol=row['cholesterol'],
        saturated_fat=row['saturated_fat'],
        trans_fat=row['trans_fat']
    )
    db.add(food)

db.commit()
db.close()
