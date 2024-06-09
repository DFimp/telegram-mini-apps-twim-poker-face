from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from server.src.database import get_async_session

from server.src.game.services.services_cards import get_shuffled_deck
from server.src.game.services.services_table_users import get_users_on_the_table, get_user_on_table_by_id

router = APIRouter(prefix="/card_actions", tags=["Card"])


@router.patch("/")
async def start_handing(
    table_id: int, session: AsyncSession = Depends(get_async_session)
):
    """Раздача карт пользователям на столе"""

    try:
        shuffle_deck = await get_shuffled_deck(session)
        table_users = await get_users_on_the_table(table_id, session)

        if len(table_users) < 1:
            raise HTTPException(
                status_code=500,
                detail={"status": "error", "details": "less than two users at a table"},
            )

        for user in table_users:
            first_card, second_card = shuffle_deck.pop(0), shuffle_deck.pop(0)
            user.card_first_id, user.card_second_id = first_card.id, second_card.id
        await session.commit()

    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail=str(SQLAlchemyError))

    except Exception:
        raise HTTPException(
            status_code=500, detail={
                "status": "error",
                "details": "unknown error"
            })


@router.get("/get_cards_user/")
async def get_cards_user(
    user_id: int, table_id: int, session: AsyncSession = Depends(get_async_session)
):
    """Получить карты пользователя за столом"""

    user = await get_user_on_table_by_id(user_id, table_id, session, True)

    return user[0].card_first, user[0].card_second
