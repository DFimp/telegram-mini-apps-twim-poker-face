from sqlalchemy.orm import Mapped, mapped_column, relationship
from server.src.database import Base


class Cards(Base):
    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(primary_key=True)
    rank: Mapped[str] = mapped_column(nullable=True)
    suit: Mapped[str] = mapped_column(nullable=True)
    img_url: Mapped[str] = mapped_column(nullable=False)

    first_card_user = relationship(
        "TableUsers",
        back_populates="card_first",
        foreign_keys="[TableUsers.card_first_id]",
    )
    second_card_user = relationship(
        "TableUsers",
        back_populates="card_second",
        foreign_keys="[TableUsers.card_second_id]",
    )

