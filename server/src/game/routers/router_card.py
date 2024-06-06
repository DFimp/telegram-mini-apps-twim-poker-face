import random

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from random import shuffle

from server.src.database import get_async_session
from server.src.game.models.Cards import Cards


router = APIRouter(prefix="/card_actions", tags=["Card"])


@router.get("/")
async def get_shuffled_deck(session: AsyncSession = Depends(get_async_session)):
    """Создание перемешанной колоды"""

    query = await session.execute(select(Cards))
    result = query.scalars().all()

    deck = [card for card in result]
    random.shuffle(deck)

    return deck
