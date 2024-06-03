from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from .Handings import Handings
from .Cards import Cards
from .TableUsers import TableUsers
from .TypeOfActions import TypeOfActions
from .StagesHandings import StagesHandings

Base = declarative_base()


class UserActions(Base):
    __tablename__ = "user_actions"

    id: Mapped[int] = mapped_column(primary_key=True)
    stage_handing_id: Mapped[int] = mapped_column(ForeignKey(StagesHandings.id, ondelete="CASCADE"))
    type_id: Mapped[int] = mapped_column(ForeignKey(TypeOfActions.id, ondelete="CASCADE"))
    amount: Mapped[int] = mapped_column(ForeignKey(Cards.id, ondelete="CASCADE"))
