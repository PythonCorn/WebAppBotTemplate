from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.database.repos.user import UserRepo
from app.webapp.schemas import WebAppAuthRequest
from app.webapp.schemas import WebAppInitDataResponse, UserSchema
from app.core.security import telegram_auth

webapp_router = APIRouter(prefix="", tags=["API"])

@webapp_router.post("/auth", response_model=UserSchema)
async def auth(payload: WebAppAuthRequest, session: AsyncSession = Depends(get_db)):
    user_data = telegram_auth(payload.initData)
    data_response = WebAppInitDataResponse.model_validate(user_data)
    user: UserSchema = data_response.user
    user_repo = UserRepo(session)
    user_in_base = await user_repo.get_user_by_telegram_id(user.id)
    print(user_in_base)
    print(user_in_base.dict())
    return user