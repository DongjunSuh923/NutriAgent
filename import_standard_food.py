import pandas as pd
from app.models import Food
from app.database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

df = pd.read_excel(
    "data/국가표준식품성분표_250426공개.xlsx",
    sheet_name="국가표준식품성분 Database 10.0",
    header=1,
    skiprows=[2]
)

df = df.rename(columns={
    "식품명": "name",
    "에너지": "calories",
    "단백질": "protein",
    "지방 ": "fat",
    "탄수화물": "carbs",
    "당류": "sugars",
    "총 \n식이섬유": "fiber",
    "나트륨": "sodium",
    "총 포화\n지방산": "saturated_fat",
    "총 트랜스\n지방산": "trans_fat"
})

df["weight"] = 100.0

df["cholesterol"] = 0.0

def to_float(val):
    try:
        return float(val)
    except (ValueError, TypeError):
        return 0.0

numeric_cols = [
    "calories", "protein", "fat", "carbs",
    "sugars", "fiber", "sodium",
    "saturated_fat", "trans_fat", "cholesterol", "weight"
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = df[col].apply(to_float)

df.fillna(0.0, inplace=True)

db = SessionLocal()
count = 0

for _, row in df.iterrows():
    try:
        if not isinstance(row["name"], str):
            continue

        food = Food(
            name=row["name"],
            weight=row["weight"],
            calories=row["calories"],
            carbs=row["carbs"],
            protein=row["protein"],
            fat=row["fat"],
            sodium=row["sodium"],
            sugars=row["sugars"],
            fiber=row["fiber"],
            cholesterol=row["cholesterol"],
            saturated_fat=row["saturated_fat"],
            trans_fat=row["trans_fat"]
        )
        db.add(food)
        count += 1
    except Exception as e:
        print("Error on row:", row.get("name", "Unknown"), e)

db.commit()
db.close()

print(f"{count}개의 데이터를 DB에 추가했습니다.")
