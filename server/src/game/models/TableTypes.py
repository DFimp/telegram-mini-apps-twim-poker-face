from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from server.src.database import Base


class TableTypes(Base):
    __tablename__ = "table_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    buy_in_low: Mapped[int] = mapped_column(nullable=True)
    buy_in_high: Mapped[int] = mapped_column(nullable=True)
    blind: Mapped[bool]

    table = relationship("Tables", back_populates="table_type")

