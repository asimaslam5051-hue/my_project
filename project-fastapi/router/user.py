from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_db
from schemas import UserBase, UserDisplay
from router import user
from typing import List
from router.auth.oauth2 import oauth2_schema, get_current_user
router = APIRouter(
    prefix="/user",
    tags=["user"]
)

# Create a user
@router.post("/", response_model=UserDisplay, status_code=status.HTTP_201_CREATED)
def create_user(request: UserBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return user.create_user(db, request)

# Get all users
@router.get("/", response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return user.get_all_user(db)

# Get a single user
@router.get("/{id}", response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db)):
    user = user.get_user(db, id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

# Update a user
@router.put("/{id}", response_model=UserDisplay)
def update_user(id: int, request: UserBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    updated_user = user.update_user(db, id, request)
    if not updated_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return updated_user

# Delete a user
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db)):
    success = user.delete_user(db, id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return None
