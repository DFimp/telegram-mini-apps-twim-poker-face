from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from .Handings import Handings
from .Cards import Cards
from .TableUsers import TableUsers

Base = declarative_base()


class UsersCards(Base):
    __tablename__ = "users_cards"

    id: Mapped[int] = mapped_column(primary_key=True)
    table_user_id: Mapped[int] = mapped_column(ForeignKey(TableUsers.id, ondelete="CASCADE"))
    handing_id: Mapped[int] = mapped_column(ForeignKey(Handings.id, ondelete="CASCADE"))
    card_1_id: Mapped[int] = mapped_column(ForeignKey(Cards.id, ondelete="CASCADE"))
    card_2_id: Mapped[int] = mapped_column(ForeignKey(Cards.id, ondelete="CASCADE"))
