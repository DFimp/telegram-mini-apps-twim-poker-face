from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException

from .models import Users
from .schemas import UserCreate


async def get_user_by_telegram_id(telegram_id: int, session: AsyncSession):
    """Получение пользователя по id"""

    try:
        result = await session.execute(select(Users).filter_by(telegram_id=telegram_id))
        return result.scalars().first()
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail=str(SQLAlchemyError))


async def create_user(user: UserCreate, session: AsyncSession):
    """Создание и добавление пользователя в БД"""

    try:
        new_user = Users(
            telegram_id=user.telegram_id,
            first_name=user.first_name,
            last_name=user.last_name,
            username=user.username,
        )

        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)

        return new_user
    except SQLAlchemyError:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(SQLAlchemyError))
    except Exception:
        await session.rollback()
        raise HTTPException(status_code=500, detail={"status": "error"})
