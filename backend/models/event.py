from sqlalchemy import Column, Integer, String, ForeignKey
from database.db import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    location = Column(String)
    date = Column(String)
    organizer_id = Column(Integer, ForeignKey("users.id"))