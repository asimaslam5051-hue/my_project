from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from router.auth.oauth2 import oauth2_schema
from db.database import get_db
from schemas import ArticleBase, ArticleDisplay
from db import db_article
from schemas import ArticleBase, ArticleDisplay, UserBase
from router.auth.oauth2 import oauth2_schema, get_current_user






router = APIRouter(
    prefix="/article",
    tags=["article"]
)


# Create an article
@router.post("/", response_model=ArticleDisplay, status_code=status.HTTP_201_CREATED)
def create_article(request: ArticleBase, db: Session = Depends(get_db),token:str=Depends(oauth2_schema)):
    created_article = db_article.create_article(db, request)
    if not created_article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Failed to create article"
        )
    return created_article


# Get a specific article
@router.get("/{id}") # response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
 

    return {
        "data": db_article.get_article(db,id),
        "current_user": current_user
    }