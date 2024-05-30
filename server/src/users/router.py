from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from server.src.database import get_async_session
from server.src.users.models import User
from server.src.users.schemas import UserCreate

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserCreate)
async def create_user_in_db(
    user: UserCreate, session: AsyncSession = Depends(get_async_session)
):
    """Создание и добавление пользователя в бд"""
    new_user = User(
        first_name=user.first_name,
        username=user.username,
        telegram_id=user.telegram_id,
    )
    session.add(new_user)
    await session.commit()

    return {"status": "200", "user": new_user}
