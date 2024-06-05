from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from server.src.database import Base


class StagesHandings(Base):
    __tablename__ = "stages_handings"

    id: Mapped[int] = mapped_column(primary_key=True)
    stage_id: Mapped[int] = mapped_column(ForeignKey("stages.id", ondelete="CASCADE"))
    handing_id: Mapped[int] = mapped_column(
        ForeignKey("handings.id", ondelete="CASCADE")
    )

    action_user = relationship("UserActions", back_populates="stage_handing")
