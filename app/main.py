from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import foods
from app.database import engine, Base
from app import models

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def health_check():
    return {"status": "healthy"}

app.include_router(foods.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
