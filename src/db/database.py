from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

import os
from dotenv import load_dotenv

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
)

async_session = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=Session,
)


Base = declarative_base()


async def get_db():
    async with async_session() as session:
        yield session
