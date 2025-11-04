from sqlalchemy.orm import Session

import app.models.users as user_model
import app.schemas.users as schemas_user


def get_users(db: Session):
    return db.query(user_model.User).all()


def get_user_by_name(db: Session, user_name: str):
    return db.query(user_model.User).filter(user_model.User.name == user_name).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(user_model.User).filter(user_model.User.id == user_id).first()


def create_user(
        db: Session,
        user: schemas_user.UserCreateSchema
    ):
    
    db_user = user_model.User(name = user.name, surname = user.surname  )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user


def update_user(
        db: Session,
        user_id: int,
        user: schemas_user.UserUpdateSchema
    ):
    
    db.query(user_model.User).filter(user_model.User.id == user_id).update({
        user_model.User.name: user.name, 
        user_model.User.surname: user.surname
        })
    db.commit()
    return True


def delete_user(
        db: Session,
        user_id: int
    ):
    
    db.query(user_model.User).filter(user_model.User.id == user_id).delete()
    db.commit()
    return True