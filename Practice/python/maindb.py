# main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import User
from schemas import UserCreate, UserRead
from routers import users_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Management API")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(users_router.router, prefix="/users", tags=["users"])

@app.get("/")
def root():
    return {"message": "User Management API with FastAPI"}

# Run with: uvicorn main:app --reload
