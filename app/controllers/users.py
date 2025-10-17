from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from app.models.users import User

import app.lib.databases.users as user_db
import app.schemas.users as schemas_user



class UserController:
    def get_users(
            self, 
            db: Session
            ):
        users = user_db.get_users(db=db)
        return self._take_JSON_response(users=users)
    
    def get_user_by_id(
            self, 
            db: Session,
            user_id: int
            ):
        user = user_db.get_user_by_id(db=db, user_id=user_id)
        return self._take_JSON_response(user)
    
    def get_user_by_name(
            self,
            db: Session,
            user_name: str
            ):
        users = user_db.get_user_by_name(db=db, user_name=user_name)
        return self._take_JSON_response(users)
    
    def create_user(
            self,
            db: Session,
            user: schemas_user.UserCreateSchema
            ):
        created_user = user_db.create_user(db=db, user=user)
        
        if not created_user:
            return False

        return self._take_JSON_response(created_user)
    
    def update_user(
            self,
            db: Session,
            user_id: int,
            user: schemas_user.UserUpdateSchema
            ):
        searching_user = user_db.get_user_by_id(db=db, user_id=user_id)
        if not searching_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "message":"User was not found",
                    "status_code":status.HTTP_404_NOT_FOUND
                }
            )
        
        is_update_user = user_db.update_user(db=db, user_id=user_id, user=user)
        return is_update_user
    
    def delete_user(
            self,
            db: Session,
            user_id: int
            ):
        searching_user = user_db.get_user_by_id(db=db, user_id=user_id)
        if not searching_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "message":"User was not found",
                    "status_code":status.HTTP_404_NOT_FOUND
                }
            )

        is_delete_user = user_db.delete_user(db=db, user_id=user_id)
        return is_delete_user


    @staticmethod
    def _take_JSON_response(users):
        if not users:
            return []
        
        if isinstance(users, list):
            return [schemas_user.UserReadSchema.model_validate(user) for user in users]
        
        return schemas_user.UserReadSchema.model_validate(users)
