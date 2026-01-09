from datetime import datetime
from decimal import Decimal

from sqlalchemy import Integer, ForeignKey, DECIMAL, Enum, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.domains.payments.available_currencies import Currency
from app.domains.payments.pay_enums import BalanceActions, PaymentProviders


class BalanceHistory(Base):
    __tablename__ = "balance_history"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    amount: Mapped[Decimal] = mapped_column(DECIMAL(precision=10, scale=2))
    currency: Mapped[Currency] = mapped_column(Enum(Currency))
    action: Mapped[BalanceActions] = mapped_column(Enum(BalanceActions))
    provider: Mapped[PaymentProviders] = mapped_column(Enum(PaymentProviders))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )