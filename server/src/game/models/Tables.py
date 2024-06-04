import datetime

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship

from .Handings import Handings
from .TableTypes import TableTypes
from .Speeds import Speeds
from ...users.models import Users

Base = declarative_base()


class Tables(Base):
    __tablename__ = "tables"

    id: Mapped[int] = mapped_column(primary_key=True)
    table_types: Mapped[int] = mapped_column(
        ForeignKey(TableTypes.id, ondelete="CASCADE")
    )
    is_free: Mapped[bool]
    speed_id: Mapped[int] = mapped_column(ForeignKey(Speeds.id, ondelete="CASCADE"))
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )

    users_on_table: Mapped[list["Users"]] = relationship(
        back_populates="tables_with_user", secondary="table_users"
    )
    speed: Mapped["Speeds"] = relationship(back_populates="table")
    handings: Mapped[list["Handings"]] = relationship(back_populates="table")
