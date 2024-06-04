from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from .Stages import Stages
from .Handings import Handings

Base = declarative_base()


class StagesHandings(Base):
    __tablename__ = "stages_handings"

    stage_id: Mapped[int] = mapped_column(ForeignKey('stages.id', ondelete="CASCADE"), primary_key=True)
    handing_id: Mapped[int] = mapped_column(ForeignKey('handings.id', ondelete="CASCADE"), primary_key=True)
