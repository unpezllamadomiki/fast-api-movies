from asyncio import current_task

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, async_scoped_session, async_sessionmaker
from sqlalchemy.orm import registry, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = async_scoped_session(
    async_sessionmaker(engine, expre_on_commit=False), scopefunc=current_task
)

metadata = MetaData()
mapper_registry = registry()

Base = declarative_base()

async def get_db() -> async_scoped_session:
    yield SessionLocal
    await SessionLocal.commit()