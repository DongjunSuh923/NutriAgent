import psycopg2
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_connection():
    return psycopg2.connect(
        host="localhost",
        dbname="nutri_db",
        user="postgres",
        password="1234",
        port=5432
    )

@app.get("/search")
async def search(query: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, name, calories, protein, carbs, fat 
        FROM foods
        WHERE name LIKE %s
    """, ('%' + query + '%',))

    rows = cur.fetchall()
    cur.close()
    conn.close()

    results = []
    for row in rows:
        results.append({
            "id": row[0],
            "name": row[1],
            "calories": row[2],
            "protein": row[3],
            "carbs": row[4],
            "fat": row[5],
        })

    return results