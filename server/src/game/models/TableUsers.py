from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from server.src.users.models import Users
from .Cards import Cards
from .Tables import Tables


Base = declarative_base()


class TableUsers(Base):
    __tablename__ = "table_users"

    user_id: Mapped[int] = mapped_column(
        ForeignKey(Users.id, ondelete="CASCADE"), primary_key=True
    )
    table_id: Mapped[int] = mapped_column(
        ForeignKey(Tables.id, ondelete="CASCADE"), primary_key=True
    )
    on_the_table: Mapped[bool]
    card_1_id: Mapped[int] = mapped_column(ForeignKey(Cards.id), nullable=True)
    card_2_id: Mapped[int] = mapped_column(ForeignKey(Cards.id), nullable=True)

    card_1: Mapped["Cards"] = relationship(foreign_keys=[card_1_id])
    card_2: Mapped["Cards"] = relationship(foreign_keys=[card_2_id])
