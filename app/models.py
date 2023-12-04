from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table,Text,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
import sqlalchemy as sa

from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")
    comments = relationship("Comment", back_populates="post")


class UserCommunityAssociation(Base):
    __tablename__ = "user_community_association"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    community_id = Column(Integer, ForeignKey("community.id"), primary_key=True)




class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    join_requests = relationship("JoinRequest", back_populates="users")
    communities = relationship("Community", secondary="user_community_association", back_populates="members")
    comments = relationship("Comment", back_populates="user")



class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey(
        "posts.id", ondelete="CASCADE"), primary_key=True)
    



    
  
class Community(Base):
    __tablename__ = "community"
    id = Column(Integer, primary_key=True, nullable=False)
    community_name = Column(String, nullable=False)
    admin_email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    join_requests = relationship("JoinRequest", back_populates="community")
    event = relationship("Event", back_populates="community")
    members = relationship("User", secondary="user_community_association", back_populates="communities")


class JoinRequest(Base):
    __tablename__ = "join_requests"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    community_id = Column(Integer, ForeignKey("community.id"))

    users = relationship("User", back_populates="join_requests")
    community = relationship("Community", back_populates="join_requests")
    
class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    date_time = Column(DateTime, nullable=False)
    community_id = Column(Integer, ForeignKey("community.id", ondelete="CASCADE"), nullable=False)

    # Define a relationship with the Community model
    community = relationship("Community", back_populates="event")
    comments = relationship("Comment", back_populates="event")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True,nullable=True)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"))
    event_id = Column(Integer, ForeignKey("event.id"))
    parent_comment_id = Column(Integer, ForeignKey("comments.id"))

    user = relationship("User")
    post = relationship("Post")
    event = relationship("Event")
    parent_comment = relationship("Comment", back_populates="replies", remote_side=[id])
    replies = relationship("Comment", remote_side=[id])