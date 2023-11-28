from fastapi import status, HTTPException,Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db
from ..models import Community, JoinRequest
from ..models import User


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

@router.post("/send_join_request/{community_id}")
def send_join_request(community_id: int, user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    community = db.query(models.Community).filter(Community.id == community_id).first()
    if community is None:
        raise HTTPException(status_code=404, detail="Community not found")

    join_request = JoinRequest(user_id=user_id, community_id=community_id)
    db.add(join_request)
    db.commit()

    return {"message": "Join request sent successfully"}

@router.get("/join_requests/{community_id}")
def get_join_requests(community_id: int, db: Session = Depends(get_db)):
    community = db.query(Community).filter(Community.id == community_id).first()
    if community is None:
        raise HTTPException(status_code=404, detail="Community not found")

   
    join_requests = db.query(JoinRequest).filter(JoinRequest.community_id == community_id).all()

    return join_requests

@router.post("/approve_join_request/{join_request_id}")
def approve_join_request(join_request_id: int, db: Session = Depends(get_db)):
    join_request = db.query(JoinRequest).filter(JoinRequest.id == join_request_id).first()
    if join_request is None:
        raise HTTPException(status_code=404, detail="Join request not found")

    

    db.delete(join_request)
    db.commit()

    return {"message": "Join request approved"}

@router.post("/reject_join_request/{join_request_id}")
def reject_join_request(join_request_id: int, db: Session = Depends(get_db)):
    join_request = db.query(JoinRequest).filter(JoinRequest.id == join_request_id).first()
    if join_request is None:
        raise HTTPException(status_code=404, detail="Join request not found")

    

    db.delete(join_request)
    db.commit()

    return {"message": "Join request rejected"}


