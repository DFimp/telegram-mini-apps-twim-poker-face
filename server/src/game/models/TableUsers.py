from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from server.src.users.models import Users
from .Tables import Tables


Base = declarative_base()


class TableUsers(Base):
    __tablename__ = "table_users"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(Users.id, ondelete="CASCADE"))
    table_id: Mapped[int] = mapped_column(ForeignKey(Tables.id, ondelete="CASCADE"))
    on_the_table: Mapped[bool]
