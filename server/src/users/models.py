# import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from server.src.database import Base

from server.src.game.models import Tables
from server.src.game.models import Handings
from server.src.game.models import TableUsers

class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=True)
    username: Mapped[str] = mapped_column(nullable=False)
    telegram_id: Mapped[int] = mapped_column(nullable=False)
    # created_at: Mapped[datetime.datetime] = mapped_column(
    #     server_default=text("TIMEZONE('utc', now())")
    # )

    tables_with_user = relationship(
        "Tables", back_populates="users_on_table", secondary="table_users"
    )
    handing = relationship("Handings", back_populates="winner_user")
