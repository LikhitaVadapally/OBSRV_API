from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#DATABASE_URL = "postgresql+asyncpg://obsrv_user:obsrv123@db:5432/obsrv"
DATABASE_URL = "postgresql+asyncpg://obsrv_user:obsrv123@db:5432/obsrv_db"
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()