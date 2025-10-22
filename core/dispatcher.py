from core.router import Router
from core.hooks import before_dispatch, after_dispatch
from core.logger import log_event, log_error

class Dispatcher:
    """
    🧭 Dispatcher — маршрутизатор апдейтов.
    Вызывает хуки, логирует события, передаёт текст в нужный обработчик.
    """
    def __init__(self, router: Router):
        self.router = router

    async def dispatch(self, update: dict) -> str:
        """
        📦 Обрабатывает входящий апдейт:
        - вызывает хуки до и после
        - извлекает текст
        - находит и вызывает обработчик
        - возвращает текстовый ответ
        """
        text = update.get("text", "")
        handler = self.router.match(text)  # 👈 заменили resolve → match

        await before_dispatch(update)

        try:
            if handler:
                log_event("dispatch", command=text, user_id=update.get("user_id"))
                response = await handler(update)
            else:
                response = "Команда не распознана."
        except Exception as e:
            log_error("dispatch_failed", error=str(e), command=text)
            response = "Произошла ошибка при обработке команды."

        await after_dispatch(update, response)
        return response