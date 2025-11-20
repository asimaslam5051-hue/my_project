from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    # One user can have many articles
    items = relationship("DbArticle", back_populates="user")


class DbArticle(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    published = Column(Boolean)
    
    user_id = Column(Integer, ForeignKey("users.id"))

    # Correct relationship:
    user = relationship("User", back_populates="items")
