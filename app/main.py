from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import foods
from app.database import engine, Base
from app import models
import logging

logger = logging.getLogger(__name__)

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    try:
        # Create tables on startup
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Failed to create database tables: {e}")
        # App will still start, but DB operations may fail

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
