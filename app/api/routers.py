from fastapi import APIRouter, Depends, HTTPException
from typing import List

from app.schemas.user_schema import UserCreate, User as UserSchema
from app.schemas.order_schema import OrderCreate, Order as OrderSchema
from app.services.user_service import UserService
from app.services.order_service import OrderService
from app.db.session import get_db

router = APIRouter()
user_router = APIRouter(prefix='/users', tags=['users'])
order_router = APIRouter(prefix='/orders', tags=['orders'])


@user_router.post('/', response_model=UserSchema)
def create_user(user: UserCreate, db=Depends(get_db)):
    return UserService(db).create_user(user)


@user_router.get('/', response_model=List[UserSchema])
def list_users(db=Depends(get_db)):
    return UserService(db).get_users()


@user_router.get('/{user_id}', response_model=UserSchema)
def get_user(user_id: int, db=Depends(get_db)):
    user = UserService(db).get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user


@user_router.put('/{user_id}', response_model=UserSchema)
def update_user(user_id: int, user: UserCreate, db=Depends(get_db)):
    return UserService(db).update_user(user_id, user)


@user_router.delete('/{user_id}')
def delete_user(user_id: int, db=Depends(get_db)):
    UserService(db).delete_user(user_id)
    return {'ok': True}


@order_router.post('/', response_model=OrderSchema)
def create_order(order: OrderCreate, db=Depends(get_db)):
    return OrderService(db).create_order(order)


@order_router.get('/', response_model=List[OrderSchema])
def list_orders(db=Depends(get_db)):
    return OrderService(db).get_orders()


@order_router.get('/{order_id}', response_model=OrderSchema)
def get_order(order_id: int, db=Depends(get_db)):
    order = OrderService(db).get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail='Order not found')
    return order


@order_router.put('/{order_id}', response_model=OrderSchema)
def update_order(order_id: int, order: OrderCreate, db=Depends(get_db)):
    return OrderService(db).update_order(order_id, order)


@order_router.delete('/{order_id}')
def delete_order(order_id: int, db=Depends(get_db)):
    OrderService(db).delete_order(order_id)
    return {'ok': True}


router.include_router(user_router)
router.include_router(order_router)
