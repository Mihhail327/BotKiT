async def before_dispatch(update: dict):
    """
    Хук до обработки апдейта.
    Можно добавить:
    - Авторизацию
    - Фильтрацию
    - Логирование
    """
    pass

async def after_dispatch(update: dict, response: str):
    """
    Хук после обработки апдейта.
    Можно добавить:
    - Метрику
    - Логирование результата
    - Отправку в сторонние сервисы
    """
    pass