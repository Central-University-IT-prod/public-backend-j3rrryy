import pytest
from redis.asyncio import Redis

from config_data import Config
from database import User, get_postgres_sessionmaker
from external_services import convert_coordinates
from .setup import user


@pytest.mark.asyncio
async def test_redis_connection(config: Config):
    conn = Redis(host=config.redis.host, port=config.redis.port)
    assert await conn.ping() is True


@pytest.mark.asyncio
async def test_postgres_connection():
    async with get_postgres_sessionmaker()() as session:
        session.add(User(**user))
        await session.commit()
        db_user = await session.get(User, user["id"])
        assert db_user.id == user["id"]
        assert db_user.username == user["username"]
        await session.delete(db_user)
        await session.commit()


@pytest.mark.asyncio
async def test_convert_coordinates():
    country, city = await convert_coordinates(59.9386, 30.3141)
    assert country == "Россия"
    assert city == "Санкт-Петербург"
