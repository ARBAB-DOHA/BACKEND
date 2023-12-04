
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import crud, models, schemas
from ..database import get_db
from ..oauth2 import get_current_user

router = APIRouter(  prefix="/comments",
    tags=['comments'])

@router.post("/posts/{post_id}/comments/", response_model=schemas.Comment)
def create_post_comment(
    post_id: int, comment: schemas.CommentCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)
):
    return crud.create_comment(db, comment, user_id=current_user.id, post_id=post_id)

@router.post("/events/{event_id}/comments/", response_model=schemas.Comment)
def create_event_comment(
    event_id: int, comment: schemas.CommentCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)
):
    return crud.create_comment(db, comment, user_id=current_user.id, event_id=event_id)

@router.get("/posts/{post_id}/comments/", response_model=List[schemas.Comment])
def get_post_comments(post_id: int, db: Session = Depends(get_db)):
    return crud.get_comments_by_post_id(db, post_id)

@router.get("/events/{event_id}/comments/", response_model=List[schemas.Comment])
def get_event_comments(event_id: int, db: Session = Depends(get_db)):
    return crud.get_comments_by_event_id(db, event_id)

@router.post("/comments/{comment_id}/reply/", response_model=schemas.Comment)
def reply_to_comment(
    comment_id: int, reply: schemas.CommentCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)
):
    user_id = current_user.id

    # Create the parent comment (reply) using crud.create_comment
    parent_comment = crud.create_comment(db, reply, user_id=user_id, parent_comment_id=comment_id)

    if not parent_comment:
        raise HTTPException(status_code=404, detail="Parent comment not found")

    # Now, you can perform additional operations if needed or simply return the parent comment
    return parent_comment
