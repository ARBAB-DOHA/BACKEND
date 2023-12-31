from enum import Enum
from pydantic import BaseModel, EmailStr, validator
from datetime import datetime
from typing import Optional
from typing import List

from pydantic.types import conint


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass










class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


class CommunityCreate(BaseModel):
    community_name: str
    admin_email: EmailStr
    password: str
    
    
class CommunityOut(BaseModel):
    id : int
    admin_email: EmailStr
    created_at : datetime
    class Config:
        from_attributes = True
        
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)

class EventCreate(BaseModel):
    title: str
    description: str
    date_time: datetime
    
class EventOut(BaseModel):
    id: int
    title: str
    description: str
    date_time: datetime
    community: CommunityOut

    class Config:
        from_attributes = True  





    
class CommunityOut(BaseModel):
    id : int
    admin_email: EmailStr
    created_at : datetime
    class Config:
        from_attributes = True
    


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int


    class Config:
        from_attributes = True
        


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        from_attributes = True




class UserDashboard(BaseModel):
    recent_posts: List[Post] = []
    upcoming_events: List[EventOut] = []
    notifications: List[str] = []


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    dashboard: UserDashboard
    reset_token: Optional[str]  
    reset_token_expiry: Optional[datetime] 

    class Config:
        from_orm = True


class CommentBase(BaseModel):
    content: str

class CommentCreate(BaseModel):
    content: str

class Comment(CommentBase):
    id: int
    user_id: int
    post_id: Optional[int] = None
    event_id: Optional[int] = None
    parent_comment_id: Optional[int] = None

    class Config:
        from_attributes = True

class CommentWithReplies(Comment):
    replies: List[Comment] = []
    
    
    
    
class Holiday(BaseModel):
    name: str
    date: datetime
    @validator("date", pre=True, always=True)
    def parse_date(cls, value):
        # Add custom logic to parse the date string into a datetime object
        try:
            return datetime.strptime(value, "%m/%d/%Y")
        except ValueError as e:
            raise ValueError("Invalid date format") from e
        
        
        
        
class BusinessApprovalStatusEnum(str, Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"

class BusinessBase(BaseModel):
    name: str
    services: str
    community_id: int

class BusinessCreate(BusinessBase):
    pass

class Business(BusinessBase):
    id: int
    approval_status: BusinessApprovalStatusEnum

    class Config:
        from_attributes = True