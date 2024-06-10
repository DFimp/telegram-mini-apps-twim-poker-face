from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from server.src.game.models.TableUsers import TableUsers


async def get_users_on_the_table(table_id: int, session: AsyncSession):
    """Получить всех пользователей за столом"""

    try:
        query = select(TableUsers).filter_by(table_id=table_id)
        result = await session.execute(query)

        return result.scalars().all()
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail=str(SQLAlchemyError))


async def join_user_to_the_table(user_id: int, table_id: int, session: AsyncSession):
    """Присоединения пользователя за стол"""

    try:
        table_user = TableUsers(
            user_id=user_id,
            table_id=table_id,
            on_the_table=True,
            card_first_id=None,
            card_second_id=None,
        )

        session.add(table_user)
        await session.commit()

    except SQLAlchemyError:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(SQLAlchemyError))

    except Exception:
        await session.rollback()
        raise HTTPException(status_code=500, detail="Error")


async def disconnection_user_from_table(
    user_id: int, table_id: int, session: AsyncSession
):
    """Отсоединение пользователя от стола"""

    try:
        result = await get_user_on_table_by_id(user_id, table_id, session)

        await session.delete(result)
        await session.commit()

    except SQLAlchemyError:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(SQLAlchemyError))

    except NoResultFound:
        raise HTTPException(status_code=404, detail="User not found")


async def get_user_on_table_by_id(
    user_id: int, table_id: int, session: AsyncSession, load_cards: bool = False
):
    """Получить пользователя по id за столом"""

    try:
        query = select(TableUsers).filter_by(user_id=user_id, table_id=table_id)
        if load_cards:
            query = query.options(
                selectinload(TableUsers.card_first),
                selectinload(TableUsers.card_second),
            )

        result = await session.execute(query)

    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail=str(SQLAlchemyError))

    except NoResultFound:
        raise HTTPException(status_code=404, detail="User not found")
