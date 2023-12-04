# In your crud.py file
from sqlalchemy.orm import Session
from . import models  # Import your existing SQLAlchemy models
from .schemas import EventCreate

from app.models import User, Post, Event
from datetime import datetime
from app.schemas import UserDashboard

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

# your_project/app/crud/user.py



def get_user_data(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        return None

    recent_posts = db.query(Post).filter(Post.owner_id == user_id).limit(5).all()
    upcoming_events = db.query(Event).filter(Event.community_id.in_([c.id for c in user.communities])).filter(Event.date_time > datetime.utcnow()).limit(5).all()
    notifications = ["New post in community ", "Event starting soon",]  # Fetch or generate notifications

    return {"user": user, "dashboard": UserDashboard(recent_posts=recent_posts, upcoming_events=upcoming_events, notifications=notifications)}
