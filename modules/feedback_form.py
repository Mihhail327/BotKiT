from core.fsm import fsm

async def feedback_handler(update: dict) -> str:

    """
    FSM-форма: имя → email → сообщение.
    Управляется через состояния и временные данные.
    """
    user_id = update.get("user_id")
    text = update.get("text", "").strip()

    # 🔍 Получаем текущее состояние пользователя
    state = fsm.get_state(user_id)

    if not state:
        # 🟢 Старт: устанавливаем начальное состояние
        fsm.set_state(user_id, "awaiting_name")
        return "Как вас зовут?"

    elif state == "awaiting_name":
        # 🟡 Сохраняем имя и переходим к email
        fsm.set_data(user_id, "name", text)
        fsm.set_state(user_id, "awaiting_email")
        return "Введите ваш email:"

    elif state == "awaiting_email":
        # 🔵 Сохраняем email и переходим к сообщению
        fsm.set_data(user_id, "email", text)
        fsm.set_state(user_id, "awaiting_message")
        return "Напишите ваше сообщение:"

    elif state == "awaiting_message":
        # 🟣 Финальный шаг: собираем все данные
        name = fsm.get_data(user_id, "name") or "неизвестно"
        email = fsm.get_data(user_id, "email") or "не указано"
        message = text

        # 🧹 Сбрасываем состояние после завершения
        fsm.reset_state(user_id)

        return (
            f"Спасибо, {name}!\n"
            f"Мы получили ваше сообщение:\n"
            f"📧 {email}\n"
            f"📝 {message}"
        )

    else:
        # ❌ Непредвиденное состояние — сбрасываем и перезапускаем
        fsm.reset_state(user_id)
        return "Что-то пошло не так. Начнём сначала: /feedback"

