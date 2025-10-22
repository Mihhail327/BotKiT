from typing import Dict, Optional

class FSM:
    """
    🧠 FSM (Finite State Machine) — простое хранилище для пошаговых сценариев.
    Используется для форм, диалогов, авторизации и любых взаимодействий, где важно помнить контекст.

    Хранит:
    - user_id → текущее состояние (например, "awaiting_email")
    - user_id → временные данные (например, {"name": "Михаил", "email": "test@example.com"})
    """

    def __init__(self):
        # 📍 Состояния пользователей: user_id → state
        self.user_states: Dict[int, str] = {}

        # 🗂 Временные данные: user_id → {ключ: значение}
        self.user_data: Dict[int, Dict[str, str]] = {}

    def set_state(self, user_id: int, state: str):
        """
        🔧 Устанавливает новое состояние для пользователя.
        Пример: fsm.set_state(123, "awaiting_email")
        """
        self.user_states[user_id] = state

    def get_state(self, user_id: int) -> Optional[str]:
        """
        🔍 Получает текущее состояние пользователя.
        Если состояния нет — возвращает None.
        """
        return self.user_states.get(user_id)

    def reset_state(self, user_id: int):
        """
        🧹 Сбрасывает состояние и временные данные пользователя.
        Используется после завершения сценария или при ошибке.
        """
        self.user_states.pop(user_id, None)
        self.user_data.pop(user_id, None)

    def has_state(self, user_id: int) -> bool:
        """
        ✅ Проверяет, есть ли активное состояние у пользователя.
        Удобно для fallback-обработки.
        """
        return user_id in self.user_states

    def set_data(self, user_id: int, key: str, value: str):
        """
        📝 Сохраняет временные данные для пользователя.
        Пример: fsm.set_data(123, "email", "test@example.com")
        """
        if user_id not in self.user_data:
            self.user_data[user_id] = {}
        self.user_data[user_id][key] = value

    def get_data(self, user_id: int, key: str) -> Optional[str]:
        """
        📤 Получает сохранённые данные по ключу.
        Пример: fsm.get_data(123, "email") → "test@example.com"
        """
        return self.user_data.get(user_id, {}).get(key)

fsm = FSM()