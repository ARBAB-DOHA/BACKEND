from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db
from app import crud


router = APIRouter(
    prefix="/users",
    tags=['Users']
)

# /users/
# /users


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # hash the password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    user_data = crud.get_user_data(new_user.id, db)

    # Construct UserOut with the correct dashboard field
    user_out = schemas.UserOut(
        id=new_user.id,
        email=new_user.email,
        created_at=new_user.created_at,
        dashboard=user_data.get("dashboard", schemas.UserDashboard()),  # Use a default UserDashboard if not available
        reset_token=new_user.reset_token,
        reset_token_expiry=new_user.reset_token_expiry,
    )

    return user_out



@router.get('/{id}', response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db), ):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")
    user_data = crud.get_user_data(id, db)
    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")
    
   
    

  

    return user,user_data
