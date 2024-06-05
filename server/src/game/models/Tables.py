import datetime

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from server.src.database import Base


class Tables(Base):
    __tablename__ = "tables"

    id: Mapped[int] = mapped_column(primary_key=True)
    table_types: Mapped[int] = mapped_column(
        ForeignKey("table_types.id", ondelete="CASCADE")
    )
    is_free: Mapped[bool]
    speed_id: Mapped[int] = mapped_column(ForeignKey("speeds.id", ondelete="CASCADE"))
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )

    users_on_table = relationship(
        "Users", back_populates="tables_with_user", secondary="table_users"
    )
    speed = relationship("Speeds", back_populates="table")
    handing = relationship("Handings", back_populates="table")
    table_type = relationship("TableTypes", back_populates="table_types")
