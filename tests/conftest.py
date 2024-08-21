from typing import Any, AsyncGenerator

import pytest
import pytest_asyncio
from aiogram.fsm.storage.memory import MemoryStorage

from config_data import Config, load_config
from .mocked_bot import MockedBot


@pytest_asyncio.fixture(scope="session")
async def memory_storage() -> AsyncGenerator[Any, Any]:
    storage = MemoryStorage()
    try:
        yield storage
    finally:
        await storage.close()


@pytest.fixture()
def bot() -> MockedBot:
    return MockedBot()


@pytest.fixture()
def config() -> Config:
    return load_config()
