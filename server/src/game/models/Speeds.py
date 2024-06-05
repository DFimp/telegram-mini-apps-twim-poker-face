from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from server.src.database import Base


class Speeds(Base):
    __tablename__ = "speeds"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)

    table = relationship("Tables", back_populates="speed")
