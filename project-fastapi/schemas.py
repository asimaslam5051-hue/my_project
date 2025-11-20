from pydantic import BaseModel
from typing import List, Optional

# Article inside UserDisplay
class Article(BaseModel):
    title: str
    content: str
    published: bool

    model_config = {
        "from_attributes": True
    }

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    id: int
    username: str
    email: str
    items: List[Article] = []

    model_config = {
        "from_attributes": True
    }

# User inside ArticleDisplay
class User(BaseModel):
    id: int
    username: str

    model_config = {
        "from_attributes": True
    }

class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int

class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: Optional[User]  # link back to user

    model_config = {
        "from_attributes": True
    }