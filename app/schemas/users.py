from pydantic import BaseModel, Field


class UserReadSchema(BaseModel):
    id: int
    name: str
    surname: str

    class Config:
        from_attributes = True


class UserCreateSchema(BaseModel):
    name: str = Field(min_length= 2, max_length=20, description='user name')
    surname: str = Field(min_length= 2, max_length=20, description='user surname')

    


class UserUpdateSchema(BaseModel):
    id: int
    name: str
    surname: str