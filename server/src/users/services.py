from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException

from .models import User
from .schemas import UserCreate


async def get_user_by_telegram_id(telegram_id: int, session: AsyncSession):
    """Получение пользователя по telegram_id"""
    try:
        result = await session.execute(select(User).filter_by(telegram_id=telegram_id))
        return result.scalars().first()
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail=str(SQLAlchemyError))


async def create_user(user: UserCreate, session: AsyncSession):
    """Создание и добавление пользователя в БД"""

    try:
        new_user = User(
            first_name=user.first_name,
            username=user.username,
            telegram_id=user.telegram_id,
        )

        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)

        return new_user
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail=str(SQLAlchemyError))
    except Exception:
        await session.rollback()
        raise HTTPException(status_code=500, detail={"status": "error"})
