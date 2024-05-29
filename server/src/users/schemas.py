from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str
    username: str
    telegram_id: int


class UserCreate(UserBase):
    pass
