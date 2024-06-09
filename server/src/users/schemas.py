# schemas.py
from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    telegram_id: int
    first_name: str
    last_name: str
    username: str
