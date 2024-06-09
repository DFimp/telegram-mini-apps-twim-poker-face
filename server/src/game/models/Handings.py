from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from server.src.database import Base

from .Stages import Stages
from .StagesHandings import StagesHandings

class Handings(Base):
    __tablename__ = "handings"

    id: Mapped[int] = mapped_column(primary_key=True)
    winner_user_id: Mapped[int] = mapped_column(
        ForeignKey("users.telegram_id", ondelete="CASCADE")
    )
    table_id: Mapped[int] = mapped_column(ForeignKey("tables.id", ondelete="CASCADE"))

    winner_user = relationship("Users", back_populates="handing")
    table = relationship("Tables", back_populates="handing")
    stage = relationship(
        "Stages", back_populates="handing", secondary="stages_handings"
    )