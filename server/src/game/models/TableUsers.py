from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from server.src.database import Base


class TableUsers(Base):
    __tablename__ = "table_users"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), primary_key=True
    )
    table_id: Mapped[int] = mapped_column(
        ForeignKey("tables.id", ondelete="CASCADE"), primary_key=True
    )
    on_the_table: Mapped[bool]
    card_1_id: Mapped[int] = mapped_column(ForeignKey("cards.id"), nullable=True)
    card_2_id: Mapped[int] = mapped_column(ForeignKey("cards.id"), nullable=True)

    card_1 = relationship("Cards", foreign_keys=[card_1_id])
    card_2 = relationship("Cards", foreign_keys=[card_2_id])
