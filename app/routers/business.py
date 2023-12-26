from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models import BusinessApprovalStatus

from ..database import get_db
from ..crud import create_business, get_businesses, get_business_by_id, update_business_approval_status
from ..schemas import BusinessCreate, Business

router = APIRouter(tags=['Business'])

@router.post("/business/register")
async def register_business(business: BusinessCreate, db: Session = Depends(get_db)):
    return create_business(db, business)

@router.get("/businesses", response_model=list[Business])
async def get_business_list(db: Session = Depends(get_db)):
    return get_businesses(db)

@router.put("/business/{business_id}/approve")
async def approve_business(business_id: int, db: Session = Depends(get_db)):
    business = get_business_by_id(db, business_id)
    if not business:
        raise HTTPException(status_code=404, detail="Business not found")
    return update_business_approval_status(db, business_id, BusinessApprovalStatus.approved)
