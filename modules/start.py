from config.settings import AVAILABLE_COMMANDS

async def start_handler(update: dict) -> str:
    """
    Команда /start
    Показывает приветствие и список доступных команд.
    """
    # 👋 Приветствие
    lines = [
        "👋 Добро пожаловать в BotKit!",
        "Вот что я умею:"
    ]

    # 📋 Перечисляем зарегистрированные команды
    for cmd, desc in AVAILABLE_COMMANDS.items():
        lines.append(f"{cmd} — {desc}")

    # 🔚 Возвращаем итоговое сообщение
    return "\n".join(lines)