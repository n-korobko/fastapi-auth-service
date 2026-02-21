from datetime import date
from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    surname: Mapped[str] = mapped_column(String(255), nullable=False)

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )

    date_of_birth: Mapped[date] = mapped_column(Date, nullable=False)

    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)