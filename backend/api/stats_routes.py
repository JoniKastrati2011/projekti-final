from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import SessionLocal
from models.event import Event
from models.volunteer import Volunteer

router = APIRouter(prefix="/stats")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_stats(db: Session = Depends(get_db)):
    return {
        "total_events": db.query(Event).count(),
        "total_volunteers": db.query(Volunteer).count()
    }