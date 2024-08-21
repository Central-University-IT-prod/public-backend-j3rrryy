from aiogram.types import User, Chat


TEST_USER = User(
    id=123,
    is_bot=False,
    first_name="Bot",
    last_name="Tester",
    username="BotTester",
    language_code="ru-RU",
    is_premium=False,
)

TEST_CHAT = Chat(
    id=321,
    type="private",
    title="Test",
    username=TEST_USER.username,
    first_name=TEST_USER.first_name,
    last_name=TEST_USER.last_name,
)

user = {
    "id": TEST_USER.id,
    "username": TEST_USER.username,
    "age": 50,
    "sex": "M Male",
    "latitude": 58.154,
    "longitude": 40.621,
    "country": "Russia",
    "currency": "rubble RUB",
    "bio": "",
}
