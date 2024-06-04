import datetime

from sqlalchemy import text
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship

from server.src.game.models.Handings import Handings
from server.src.game.models.Tables import Tables

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=True)
    username: Mapped[str] = mapped_column(nullable=False)
    telegram_id: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )

    tables_with_user: Mapped[list["Tables"]] = relationship(
        back_populates="users_on_table", secondary="table_users"
    )
    handings: Mapped[list["Handings"]] = relationship(back_populates="winner_user")
