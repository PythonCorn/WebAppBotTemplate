from datetime import datetime
from decimal import Decimal
from typing import Optional, Any, Dict

from sqlalchemy import Integer, BigInteger, String, DECIMAL, DateTime, func, Boolean
from sqlalchemy.orm import Mapped, mapped_column, validates

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True, index=True)
    username: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    low_username: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    balance: Mapped[Decimal] = mapped_column(DECIMAL(precision=10, scale=2), default=Decimal("0.00"))
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    @validates
    def validate_username(self, key, value: Optional[str]) -> str:
        if value and isinstance(value, str):
            self.low_username = value.lower()
            return value
        self.low_username = str(self.telegram_id)
        return str(self.telegram_id)

    def __repr__(self):
        return f"<User(id={self.id}, telegram_id={self.telegram_id})>"

    def dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "telegram_id": self.telegram_id,
            "username": self.username,
            "low_username": self.low_username,
            "balance": self.balance,
            "created_at": self.created_at
        }