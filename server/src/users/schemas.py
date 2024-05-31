# schemas.py
from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    first_name: str
    username: str
    telegram_id: int
