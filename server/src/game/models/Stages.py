from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship

from server.src.game.models.StagesHandings import StagesHandings

Base = declarative_base()


class Stages(Base):
    __tablename__ = "stages"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)

    handings: Mapped[list["Handing"]] = relationship(
        "Handing", secondary="stages_handings", back_populates="stages"
    )
