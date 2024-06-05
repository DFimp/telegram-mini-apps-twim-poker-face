from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from server.src.database import Base


class TypeOfActions(Base):
    __tablename__ = "type_of_actions"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)

    action_user = relationship("UserActions", back_populates="type")
