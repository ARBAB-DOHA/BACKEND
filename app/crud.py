# In your crud.py file
from typing import Optional
from sqlalchemy.orm import Session
from . import models  # Import your existing SQLAlchemy models
from .schemas import BusinessCreate, Comment, CommentCreate, EventCreate

from app.models import Business, User, Post, Event,Comment
from datetime import datetime
from app.schemas import UserDashboard, CommentCreate



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
    notifications = ["New post in community ", "Event starting soon",]

    # Ensure that dashboard is always populated
    dashboard_data = UserDashboard(
        recent_posts=recent_posts or [],  # Use an empty list if recent_posts is None
        upcoming_events=upcoming_events or [],  # Use an empty list if upcoming_events is None
        notifications=notifications or [],)  # Use an empty list if notifications is None

    return {"user": user, "dashboard": dashboard_data}

def create_comment(
    db: Session, comment: CommentCreate, user_id: int, post_id: Optional[int] = None, event_id: Optional[int] = None, parent_comment_id: Optional[int] = None
):
    # Set created_at to the current timestamp
    

    db_comment = Comment(
        content=comment.content,
        user_id=user_id,
        post_id=post_id,
        event_id=event_id,
        parent_comment_id=parent_comment_id,

    )

    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)

    return db_comment

def get_comments_by_post_id(db: Session, post_id: int):
    return db.query(Comment).filter(Comment.post_id == post_id).all()

def get_comments_by_event_id(db: Session, event_id: int):
    return db.query(Comment).filter(Comment.event_id == event_id).all()

def get_comments_by_user_id(db: Session, user_id: int):
    return db.query(Comment).filter(Comment.user_id == user_id).all()

def reply_to_comment(db: Session, comment: CommentCreate, user_id: int, parent_comment_id: int):
    return create_comment(db, comment, user_id, parent_comment_id=parent_comment_id)



def create_business(db: Session, business: BusinessCreate):
    db_business = Business(**business.dict())
    db.add(db_business)
    db.commit()
    db.refresh(db_business)
    return db_business

def get_businesses(db: Session):
    return db.query(Business).all()

def get_business_by_id(db: Session, business_id: int):
    return db.query(Business).filter(Business.id == business_id).first()

def update_business_approval_status(db: Session, business_id: int, approval_status: str):
    db_business = db.query(Business).filter(Business.id == business_id).first()
    db_business.approval_status = approval_status
    db.commit()
    db.refresh(db_business)
    return db_business