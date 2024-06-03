from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from .Stages import Stages
from .Handings import Handings

Base = declarative_base()


class StagesHandings(Base):
    __tablename__ = "stages_handings"

    id: Mapped[int] = mapped_column(primary_key=True)
    stage_id: Mapped[int] = mapped_column(ForeignKey(Stages.id, ondelete="CASCADE"))
    handing_id: Mapped[int] = mapped_column(ForeignKey(Handings.id, ondelete="CASCADE"))