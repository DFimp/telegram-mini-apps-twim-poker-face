import random

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from random import shuffle

from sqlalchemy.orm import selectinload

from server.src.database import get_async_session
from server.src.game.models.Cards import Cards
from server.src.game.models.TableUsers import TableUsers

from server.src.game.services.services import get_shuffled_deck
from server.src.users.models import Users

router = APIRouter(prefix="/card_actions", tags=["Card"])


@router.get("/")
async def start_handing(
    table_id: int, session: AsyncSession = Depends(get_async_session)
):
    """Раздача для стола table_id"""

    shuffle_deck = await get_shuffled_deck(session)

    # stmt = (select(TableUsers).filter_by(table_id=table_id))
    stmt = select(TableUsers).filter(TableUsers.table_id == table_id)
    result = await session.execute(stmt)
    table_users = result.scalars().all()

    print("TABLE", table_users)
    print(len(table_users))

    if len(table_users) > 1:
        for user in table_users:
            first_card = shuffle_deck.pop(0)
            second_card = shuffle_deck.pop(0)

            user.card_first_id = first_card.id
            user.card_second_id = second_card.id

        await session.commit()

        print("Карты успешно назначены пользователям.")
        print(len(table_users))
    else:
        print("Нет пользователей для назначения карт.")

        print("Меньше 2 пользователей")


@router.get("/get_cards_user/")
async def start_handing(
    user_id: int, session: AsyncSession = Depends(get_async_session)
):
    query = (
        select(TableUsers)
        .filter_by(user_id=user_id)
        .options(
            selectinload(TableUsers.card_first),
            selectinload(TableUsers.card_second)
        )
    )

    result = await session.execute(query)
    users = result.scalars().all()

    for user in users:
        return user.card_first, user.card_second


