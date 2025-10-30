from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from ..config.database import Base



class User(Base):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    def __repr__(self) -> str:
        return f"{self.name} with id = {self.id}"