from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

from .Tables import Tables
from ...users.models import Users

Base = declarative_base()


class Handings(Base):
    __tablename__ = "Handings"

    id: Mapped[int] = mapped_column(primary_key=True)
    winner_user_id: Mapped[int] = mapped_column(ForeignKey(Users.id, ondelete="CASCADE"))
    table_id: Mapped[int] = mapped_column(ForeignKey(Tables.id, ondelete="CASCADE"))