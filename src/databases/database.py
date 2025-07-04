import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.models.models import Base
engine = create_async_engine('sqlite+aiosqlite:///tasks.db')

new_session = async_sessionmaker(engine, expire_on_commit=False)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    logging.info(f"Tables deleted")

    await create_tables()
    logging.info(f"Tables created")
    yield