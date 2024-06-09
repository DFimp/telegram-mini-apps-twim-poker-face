from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from server.src.database import Base

from .TypeOfActions import TypeOfActions


class UserActions(Base):
    __tablename__ = "user_actions"

    id: Mapped[int] = mapped_column(primary_key=True)
    stage_handing_id: Mapped[int] = mapped_column(
        ForeignKey("stages_handings.id", ondelete="CASCADE")
    )
    type_id: Mapped[int] = mapped_column(
        ForeignKey("type_of_actions.id", ondelete="CASCADE")
    )
    amount: Mapped[float] = mapped_column(nullable=True)

    stage_handing = relationship("StagesHandings", back_populates="action_user")
    type = relationship("TypeOfActions", back_populates="action_user")

