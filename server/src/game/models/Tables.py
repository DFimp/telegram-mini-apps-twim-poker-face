import datetime

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from .TableTypes import TableTypes
from .Speeds import Speeds


Base = declarative_base()


class Tables(Base):
    __tablename__ = "tables"

    id: Mapped[int] = mapped_column(primary_key=True)
    table_types: Mapped[int] = mapped_column(ForeignKey(TableTypes.id, ondelete="CASCADE"))
    is_free: Mapped[bool]
    speed: Mapped[int] = mapped_column(ForeignKey(Speeds.id, ondelete="CASCADE"))
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
