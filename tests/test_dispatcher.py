import pytest
from core.dispatcher import Dispatcher
from core.router import Router

# 🎯 Хендлер, который просто возвращает текст
# Демонстрирует базовый контракт: принимает update: dict, возвращает str
async def echo_handler(update: dict) -> str:
    return f"echo: {update['text']}"

@pytest.mark.asyncio
async def test_dispatcher_known_command():
    """
    ✅ Проверяет:
    - Что Dispatcher вызывает нужный хендлер
    - Что ответ соответствует ожиданиям
    """

    # 🔧 Создаём маршрутизатор и регистрируем команду
    router = Router()
    router.register("/echo", echo_handler)

    # 🚀 Создаём диспетчер с этим маршрутизатором
    dispatcher = Dispatcher(router)

    # 📦 Симулируем входящий апдейт
    update = {"user_id": 1, "text": "/echo Hello"}

    # 🧪 Вызываем диспетчер и проверяем результат
    response = await dispatcher.dispatch(update)
    assert response == "echo: /echo Hello"

@pytest.mark.asyncio
async def test_dispatcher_unknown_command():
    """
    ❓ Проверяет:
    - Что Dispatcher корректно обрабатывает неизвестные команды
    """

    # 🔧 Пустой маршрутизатор — ни одна команда не зарегистрирована
    router = Router()
    dispatcher = Dispatcher(router)

    # 📦 Апдейт с неизвестной командой
    update = {"user_id": 1, "text": "/unknown"}

    # 🧪 Проверяем, что возвращается дефолтный ответ
    response = await dispatcher.dispatch(update)
    assert response == "Команда не распознана."