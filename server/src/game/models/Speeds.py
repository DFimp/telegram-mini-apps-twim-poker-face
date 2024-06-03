from sqlalchemy.orm import declarative_base, Mapped, mapped_column

Base = declarative_base()


class Speeds(Base):
    __tablename__ = "speeds"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)