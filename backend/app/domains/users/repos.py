from asyncio.log import logger
from typing import Optional

from sqlalchemy import select

from app.database import User
from app.database.base_repository import BaseRepo


class UserRepo(BaseRepo):
    async def get_user_by_telegram_id(self, telegram_id: int) -> Optional[User]:
        stmt = select(User).where(User.telegram_id == telegram_id)
        user = await self.session.scalar(stmt)
        if user:
            logger.info(f"Found user with telegram_id={telegram_id}")
        return user

    async def get_user_by_id(self, user_id: int) -> Optional[User]:
        stmt = select(User).where(User.id == user_id)
        user = await self.session.scalar(stmt)
        if user:
            logger.info(f"Found user with telegram_id={user_id}")
        return user

    async def get_user_by_username(self, username: str) -> Optional[User]:
        if isinstance(username, str):
            stmt = select(User).where(User.low_username == username.lower())
            return await self.session.scalar(stmt)
        return None

    async def add_new_user(self, telegram_id: int, username: str) -> User:
        user = await self.get_user_by_telegram_id(telegram_id)
        if user:
            return user
        user = User(telegram_id=telegram_id, username=username)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
