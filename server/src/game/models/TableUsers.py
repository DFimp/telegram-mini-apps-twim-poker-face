from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from server.src.database import Base

from .Tables import Tables
from .Cards import Cards

class TableUsers(Base):
    __tablename__ = "table_users"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    table_id: Mapped[int] = mapped_column(ForeignKey("tables.id", ondelete="CASCADE"))
    on_the_table: Mapped[bool]
    card_first_id: Mapped[int] = mapped_column(ForeignKey("cards.id"), nullable=True)
    card_second_id: Mapped[int] = mapped_column(ForeignKey("cards.id"), nullable=True)

    card_first = relationship(
        "Cards", back_populates="first_card_user", foreign_keys=[card_first_id]
    )
    card_second = relationship(
        "Cards", back_populates="second_card_user", foreign_keys=[card_second_id]
    )

