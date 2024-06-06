from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from server.src.database import Base


class Stages(Base):
    __tablename__ = "stages"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=True)

    handing = relationship(
        "Handings", secondary="stages_handings", back_populates="stage"
    )
