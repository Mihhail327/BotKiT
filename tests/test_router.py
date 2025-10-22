from core.router import Router

# 🎯 Dummy-хендлер для тестирования
# Симулирует обработчик команды, возвращающий фиксированный ответ
async def dummy_handler(update: dict) -> str:
    return "ok"

def test_register_and_resolve():
    """
    🧪 Проверяет:
    - Регистрацию команды через router.register
    - Разрешение маршрута через router.resolve
    - Корректную обработку неизвестной команды
    """

    # 🔧 Инициализируем маршрутизатор
    router = Router()

    # 📌 Регистрируем команду "/test" с dummy-хендлером
    router.register("/test", dummy_handler)

    # ✅ Проверяем, что команда найдена
    handler = router.resolve("/test")
    assert handler is dummy_handler

    # ❌ Проверяем, что неизвестная команда возвращает None
    handler_none = router.resolve("/unknown")
    assert handler_none is None