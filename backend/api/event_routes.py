from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import SessionLocal
from models.event import Event

router = APIRouter(prefix="/events")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

