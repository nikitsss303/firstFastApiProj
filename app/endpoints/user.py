

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.config.database import SessionLocal
from app.controllers.users import UserController 
from app.models.users import User
import app.schemas.users as user_schemas 



router = APIRouter()
user_controller = UserController()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/')
async def greetings():
    return {'Hello':'World'}


@router.get('/users')
async def get_users(
    db: Session = Depends(get_db),
    response: Response = None
):
    result = user_controller.get_users(db=db)
    if not result:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': "Users not found", "status_code": response}
    return result


@router.get('/users/id', response_model=user_schemas.UserReadSchema)
async def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db)
):
    result = user_controller.get_user_by_id(db=db, user_id=user_id)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "message":"User was not found",
                "status_code":status.HTTP_404_NOT_FOUND
            }
        )
    return result


@router.get('/users/name/{user_name}')
async def get_users_by_name(
    user_name: str,
    db: Session = Depends(get_db)
):
    result = user_controller.get_user_by_name(db=db, user_name=user_name)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "message":"User was not found",
                "status_code":status.HTTP_404_NOT_FOUND
            }
        )
    return result


@router.post('/users/create/{user_name}', response_model=user_schemas.UserCreateSchema)
async def create_users(
    user: user_schemas.UserCreateSchema,
    user_name: str,
    db: Session = Depends(get_db)
):
    user.name = user_name
    result = user_controller.create_user(db=db, user=user)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "message":"User already exists",
                "status_code":status.HTTP_400_BAD_REQUEST,
            },
        )

    print(f'endpoint: {result.__dict__}')
    return result


@router.put('/users/change', response_model=user_schemas.UserUpdateSchema)
async def update_users_by_id(
    user_id: int,
    user_name: str,
    user: user_schemas.UserUpdateSchema,
    db: Session = Depends(get_db)
):
    user.name = user_name
    result = user_controller.update_user(db=db, user_id=user_id, user=user)

    if result:
        update_user = user_controller.get_user_by_id(db=db, user_id=user_id)

    return update_user


@router.delete('/users/delete/{user_id}')
async def delete_users_by_id(
    user_id: int,
    db: Session = Depends(get_db)
):
    result = user_controller.delete_user(db=db, user_id=user_id)

    if result:
        return {"Delete":"User was deleted successfully"}