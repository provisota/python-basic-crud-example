from fastapi import APIRouter, Depends, HTTPException
from typing import List

from app.schemas.user_schema import UserCreate, User as UserSchema
from app.services.user_service import UserService
from app.db.session import get_db

router = APIRouter(prefix='/users', tags=['users'])

@router.post('/', response_model=UserSchema)
def create_user(user: UserCreate, db=Depends(get_db)):
    return UserService(db).create_user(user)

@router.get('/', response_model=List[UserSchema])
def list_users(db=Depends(get_db)):
    return UserService(db).get_users()

@router.get('/{user_id}', response_model=UserSchema)
def get_user(user_id: int, db=Depends(get_db)):
    user = UserService(db).get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user

@router.put('/{user_id}', response_model=UserSchema)
def update_user(user_id: int, user: UserCreate, db=Depends(get_db)):
    return UserService(db).update_user(user_id, user)

@router.delete('/{user_id}')
def delete_user(user_id: int, db=Depends(get_db)):
    UserService(db).delete_user(user_id)
    return {'ok': True}
