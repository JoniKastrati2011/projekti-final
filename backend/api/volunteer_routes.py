from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import SessionLocal
from models.volunteer import Volunteer

router = APIRouter(prefix="/volunteer")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/join")
def join_event(user_id: int, event_id: int, db: Session = Depends(get_db)):
    record = Volunteer(user_id=user_id, event_id=event_id)
    db.add(record)
    db.commit()
    return {"message": "Successfully joined event"}