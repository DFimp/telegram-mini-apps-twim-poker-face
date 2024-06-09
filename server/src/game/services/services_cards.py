import random
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from server.src.game.models.Cards import Cards


async def get_shuffled_deck(session: AsyncSession):
    """Создание перемешанной колоды"""

    try:
        query = await session.execute(select(Cards))
        result = query.scalars().all()

        deck = [card for card in result]
        random.shuffle(deck)

        return deck
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail=str(SQLAlchemyError))
