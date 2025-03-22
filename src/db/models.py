from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .database import Base



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    tg_id = Column(String, index=True)

    @staticmethod
    async def get_all(session: AsyncSession):
        async with session as db:
            result = await db.execute(select(User))
            return result.scalars().all()

class Wallets(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True, index=True)
    wallet = Column(String, unique=True, index=True)
    winrate = Column(Float, nullable=True)
    rockets = Column(String, nullable=True)
    profit_trades = Column(Integer, nullable=True)
    good_profit = Column(Integer, nullable=True)
    average_trade_duration = Column(Integer, nullable=True)


