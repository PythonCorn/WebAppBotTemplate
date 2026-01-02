from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from app.core.settings import settings

async_engine = create_async_engine(
    url=settings.async_db_url,
    pool_size=10,
    max_overflow=2,
)

async_session_maker = async_sessionmaker(bind=async_engine, expire_on_commit=False, class_=AsyncSession)

async def get_db():
    async with async_session_maker() as session:
        yield session