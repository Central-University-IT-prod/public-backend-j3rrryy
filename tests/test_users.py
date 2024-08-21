from unittest.mock import AsyncMock

import pytest
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.base import StorageKey
from aiogram.fsm.storage.memory import MemoryStorage


from handlers.users import *
from states import FSMSettings
from keyboards import menu_kb
from lexicon import LEXICON_RU
from .mocked_bot import MockedBot
from .setup import TEST_USER, TEST_CHAT, user


@pytest.mark.asyncio
async def test_start_command(memory_storage: MemoryStorage, bot: MockedBot):
    message = AsyncMock()
    state = FSMContext(
        memory_storage,
        StorageKey(
            bot.id,
            TEST_CHAT.id,
            TEST_USER.id,
        ),
    )
    await start_command(message, state)
    message.answer.assert_called_with(LEXICON_RU["start"])
    assert await state.get_state() == FSMSettings.set_age


@pytest.mark.asyncio
async def test_help_command(memory_storage: MemoryStorage, bot: MockedBot):
    message = AsyncMock()
    state = FSMContext(
        memory_storage,
        StorageKey(
            bot.id,
            TEST_CHAT.id,
            TEST_USER.id,
        ),
    )
    await help_command(message, state)
    message.answer.assert_called_with(LEXICON_RU["help"])
    assert await state.get_state() is None


@pytest.mark.asyncio
async def test_menu_command(memory_storage: MemoryStorage, bot: MockedBot):
    message = AsyncMock()
    state = FSMContext(
        memory_storage,
        StorageKey(
            bot.id,
            TEST_CHAT.id,
            TEST_USER.id,
        ),
    )
    await menu_command(message, user, state)
    message.answer.assert_called_with(LEXICON_RU["menu"], reply_markup=menu_kb())
    assert await state.get_state() is None
