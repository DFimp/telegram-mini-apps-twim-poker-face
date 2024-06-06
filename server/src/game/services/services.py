import random
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from server.src.game.models.Cards import Cards


async def get_shuffled_deck(session: AsyncSession):
    """Создание перемешанной колоды"""

    query = await session.execute(select(Cards))
    result = query.scalars().all()

    deck = [card for card in result]
    random.shuffle(deck)

    return deck