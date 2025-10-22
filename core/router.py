from typing import Callable, Dict, Optional

class Router:
    """
    🧭 Router — маршрутизатор команд и текстов.
    Позволяет регистрировать обработчики и извлекать их по входящему тексту.
    Поддерживает точные команды, префиксы и fallback (.*).
    """
    def __init__(self):
        self.routes: Dict[str, Callable] = {}

    def register(self, pattern: str, handler: Callable):
        """
        📦 Регистрирует обработчик для команды или шаблона.
        Пример: register("/hello", hello_handler)
        """
        self.routes[pattern] = handler

    def match(self, text: str) -> Optional[Callable]:
        """
        🔍 Ищет подходящий обработчик по входящему тексту.
        Поддерживает:
        - Точное совпадение
        - Префикс (например, "/weather Таллин")
        - Fallback (.*)
        """
        # Точное совпадение
        if text in self.routes:
            return self.routes[text]

        # Префиксное совпадение
        for pattern in self.routes:
            if pattern != ".*" and text.startswith(pattern):
                return self.routes[pattern]

        # Fallback
        return self.routes.get(".*")