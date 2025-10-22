# 🔐 Список допустимых токенов
VALID_TOKENS = {"secret123", "admin456"}

async def auth_handler(update: dict) -> str:
    """
    Команда /auth <токен>
    Проверяет, есть ли доступ по токену.
    Возвращает текстовый результат.
    """
    # 📦 Извлекаем текст команды
    parts = update.get("text", "").split(maxsplit=1)

    # ❓ Если токен не передан — просим ввести
    if len(parts) < 2:
        return "Введите токен: /auth secret123"

    token = parts[1]

    # ✅ Проверка токена
    if token in VALID_TOKENS:
        return "✅ Доступ разрешён."
    else:
        return "❌ Неверный токен."