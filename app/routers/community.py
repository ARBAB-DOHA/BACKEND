from fastapi import status, HTTPException,Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db


router = APIRouter(
    prefix="/community",
    tags=['community']
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.CommunityOut)
def create_community(community: schemas.CommunityCreate, db: Session = Depends(get_db)):
    
    hashed_password = utils.hash(community.password)
    community_dict = community.dict()
    community_dict["password"] = hashed_password
    
    new_community = models.Community(**community_dict)
    db.add(new_community)
    db.commit()
    db.refresh(new_community)
    
    return new_community