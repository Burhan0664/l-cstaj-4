import datetime
from typing import List, Optional
from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text,ForeignKey
from sqlalchemy.engine import Engine
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer,primary_key=True,nullable=True,autoincremenet=True)
    title = Column(String,nullable=True)
    content = Column(String,nullable=True)
    published = Column(Boolean, server_default='TRUE')
    users = relationship("User",back_populates = "post")
    
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, nullable = True,autoincrement=True)
    name = Column(String(225),nullable = True)
    surname = Column(String, nullable = True)
    published = Column(Boolean, server_default='TRUE')
    post_id = Column(Integer,ForeignKey=("posts.id"))
    post = relationship("Post",back_populates = "users")




    def dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "published": self.published
        }