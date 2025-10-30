from pydantic import BaseModel


class UserReadSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class UserCreateSchema(BaseModel):
    name: str

    


class UserUpdateSchema(BaseModel):
    id: int
    name: str


