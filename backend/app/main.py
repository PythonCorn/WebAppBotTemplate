from fastapi import FastAPI, APIRouter

from app.bot.api import webhook_bot
from app.core.lifespan import lifespan
from app.domains.payments.api import payments_router
from app.webapp.api import webapp_router

app = FastAPI(lifespan=lifespan)

api_router = APIRouter(prefix="/api", tags=["api"])
api_router.include_router(webapp_router)

webhook_router = APIRouter(prefix="/webhook", tags=["webhook"])
webhook_router.include_router(webhook_bot)
webhook_router.include_router(payments_router)

app.include_router(webhook_router)
app.include_router(api_router)