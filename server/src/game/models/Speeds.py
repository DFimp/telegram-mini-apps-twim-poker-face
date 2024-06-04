from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship

from server.src.game.models.Tables import Tables

Base = declarative_base()


class Speeds(Base):
    __tablename__ = "speeds"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)

    table: Mapped["Tables"] = relationship(back_populates="speed")
