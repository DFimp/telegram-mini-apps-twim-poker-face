from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship

from server.src.game.models.UsersCards import UsersCards

Base = declarative_base()


class Cards(Base):
    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(primary_key=True)
    rank: Mapped[str] = mapped_column(nullable=False)
    suit: Mapped[str] = mapped_column(nullable=False)
    img_url: Mapped[str] = mapped_column(nullable=False)

    card_1_users_cards: Mapped["UsersCards"] = relationship(
        "UsersCards", back_populates="card_1", foreign_keys="[UsersCards.card_1_id]"
    )
    card_2_users_cards: Mapped["UsersCards"] = relationship(
        "UsersCards", back_populates="card_2", foreign_keys="[UsersCards.card_2_id]"
    )
