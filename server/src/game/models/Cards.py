from sqlalchemy.orm import declarative_base, Mapped, mapped_column

Base = declarative_base()


class Cards(Base):
    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(primary_key=True)
    rank: Mapped[str] = mapped_column(nullable=False)
    suit: Mapped[str] = mapped_column(nullable=False)
    img_url: Mapped[str] = mapped_column(nullable=False)
