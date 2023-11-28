# In your crud.py file
from sqlalchemy.orm import Session
from . import models  # Import your existing SQLAlchemy models
from .schemas import EventCreate

def create_event(db: Session, event: EventCreate, community_id: int):
    db_event = models.Event(**event.dict(), community_id=community_id)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def get_event(db: Session, event_id: int):
    return db.query(models.Event).filter(models.Event.id == event_id).first()

def get_events(db: Session, community_id: int):
    return db.query(models.Event).filter(models.Event.community_id == community_id).all()
