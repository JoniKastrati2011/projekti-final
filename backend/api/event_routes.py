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

@router.post("/create")
def create_event(title: str, location: str, date: str, organizer_id: int, db: Session = Depends(get_db)):
    event = Event(
        title=title,
        location=location,
        date=date,
        organizer_id=organizer_id
    )
    db.add(event)
    db.commit()
    return {"message": "Event created"}

@router.get("/")
def list_events(db: Session = Depends(get_db)):
    return db.query(Event).all()