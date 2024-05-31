from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from server.src.database import get_async_session
from server.src.users.schemas import UserCreate

from server.src.users.services import get_user_by_telegram_id, create_user

router = APIRouter(prefix="/user_create", tags=["Users"])


@router.post("/")
async def register_or_login_user(
    user: UserCreate, session: AsyncSession = Depends(get_async_session)
):
    """Регистрация или авторизация пользователя"""

    existing_user = await get_user_by_telegram_id(user.telegram_id, session)

    if existing_user:
        return {
            "status": 200,
            "data": existing_user,
            "detail": "success auth",
        }

    new_user = await create_user(user, session)
    return {
        "status": 200,
        "data": new_user,
        "detail": "success registered",
    }
