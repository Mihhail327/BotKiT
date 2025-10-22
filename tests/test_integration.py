import pytest
from core.dispatcher import Dispatcher
from core.router import Router
from modules.feedback_form import feedback_handler


@pytest.mark.asyncio
async def test_feedback_flow():
    """
    🧪 Проверяет:
    - Полный сценарий FSM: имя → email → сообщение
    - Сохранение промежуточных данных
    - Сброс состояния после завершения
    """

    # 🔧 Инициализация маршрутизатора и диспетчера
    router = Router()
    router.register("/feedback", feedback_handler)
    dispatcher = Dispatcher(router)

    user_id = 42  # 🧍 Тестовый пользователь

    # 🟢 Старт формы — FSM устанавливает состояние "awaiting_name"
    update1 = {"user_id": user_id, "text": "/feedback"}
    r1 = await dispatcher.dispatch(update1)
    assert "Как вас зовут" in r1

    # 🟡 Имя — FSM сохраняет имя и переходит к "awaiting_email"
    update2 = {"user_id": user_id, "text": "Алиса"}
    r2 = await dispatcher.dispatch(update2)
    assert "Введите ваш email" in r2

    # 🔵 Email — FSM сохраняет email и переходит к "awaiting_message"
    update3 = {"user_id": user_id, "text": "alice@example.com"}
    r3 = await dispatcher.dispatch(update3)
    assert "Напишите ваше сообщение" in r3

    # 🟣 Сообщение — FSM завершает сценарий, сбрасывает состояние
    update4 = {"user_id": user_id, "text": "Привет!"}
    r4 = await dispatcher.dispatch(update4)
    assert "Спасибо, Алиса" in r4
    assert "alice@example.com" in r4
    assert "Привет!" in r4

    # ✅ Проверка: FSM-состояние должно быть сброшено
    assert not fsm.has_state(user_id)
