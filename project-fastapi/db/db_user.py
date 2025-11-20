from sqlalchemy.orm import Session
from schemas import UserBase
from models import User
from db.hash import Hash
from fastapi import HTTPException, status


def create_user(db: Session, request: UserBase):
    new_user = User(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt_password(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_user(db: Session):
    return db.query(User).all()


def get_user(db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found"
        )

    return user


def get_user_by_username(db: Session, username: str):
    user = db.query(User).filter(User.username == username).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with username '{username}' not found"
        )
    return user


def update_user(db: Session, id: int, request: UserBase):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found"
        )

    # Update fields
    user.username = request.username
    user.email = request.email
    user.password = Hash.bcrypt_password(request.password)

    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found"
        )

    db.delete(user)
    db.commit()
    return {"detail": "User deleted successfully"}
