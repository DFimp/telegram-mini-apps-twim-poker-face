from sqlalchemy.orm import declarative_base, Mapped, mapped_column

Base = declarative_base()


class TableTypes(Base):
    __tablename__ = "table_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    buy_in_low: Mapped[int] = mapped_column(nullable=False)
    buy_in_high: Mapped[int] = mapped_column(nullable=False)
    blind: Mapped[bool]
