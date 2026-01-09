from sqlalchemy.ext.asyncio import AsyncSession

from app.domains.users.repos import UserRepo
from app.domains.payments.available_currencies import FIAT, Fiat


class UpdateBalance:
    def __init__(self, session: AsyncSession):
        self.user_repo = UserRepo(session)
        self.fiat: Fiat = FIAT
