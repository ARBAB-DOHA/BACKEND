# In your main application file
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from .. import crud  # Import your existing CRUD functions
from ..database import get_db
from ..schemas import EventCreate

router = APIRouter(
    prefix="/event",
    tags=['Event'])

@router.post("/events/", response_model=EventCreate)
def create_event(event: EventCreate, community_id: int, db: Session = Depends(get_db)):
    return crud.create_event(db, event, community_id)

@router.get("/events/{event_id}")
def read_event(event_id: int, db: Session = Depends(get_db)):
    return crud.get_event(db, event_id)

@router.get("/events/")
def read_events(community_id: int, db: Session = Depends(get_db)):
    return crud.get_events(db, community_id)
