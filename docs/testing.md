---

# 🧪 Testing Guide

**Как писать аннотированные тесты, которые обучают архитектурному мышлению.**  
В BotKit тест — это не просто проверка, а мини-глава: он показывает, как работает FSM, как устроен сценарий, и как его можно расширить.

---

## 📦 Структура обучающего теста

```python
def test_form_fsm_flow():
    fsm = FormFSM()
    assert fsm.handle(Event("input_name", "Алиса")) == "Введите ваш email:"
    assert fsm.handle(Event("input_email", "alice@example.com")) == "Спасибо, Алиса! Мы отправим письмо на alice@example.com."
    assert fsm.state == "done"
```

### 🧠 Аннотации

- `test_form_fsm_flow`: название = заголовок walkthrough.
- `fsm.handle(...)`: имитирует пользовательский ввод.
- `assert ...`: проверяет как поведение (ответ), так и архитектуру (состояние).

---

## 🧩 Паттерн: тест как мини-глава

Каждый тест:
- начинается с инициализации контекста (FSM, хранилище),
- вызывает событие (input, transition),
- проверяет результат (ответ, состояние),
- может быть аннотирован в коде или документации.

---

## ✅ Примеры: FSM-хранилище

```python
def test_set_and_get_state():
    fsm = FSM()
    fsm.set_state(42, "awaiting_input")
    assert fsm.get_state(42) == "awaiting_input"

def test_reset_state():
    fsm = FSM()
    fsm.set_state(42, "active")
    fsm.reset_state(42)
    assert fsm.get_state(42) is None

def test_has_state():
    fsm = FSM()
    fsm.set_state(1, "ready")
    assert fsm.has_state(1)
    fsm.reset_state(1)
    assert not fsm.has_state(1)
```

### 🧠 Архитектурные идеи

- Проверка атомарных операций FSM-хранилища
- Устойчивость к отсутствию состояния (`None`)
- Guard-логика через `has_state`

---

## 🧬 Примеры: FSM-сценарии

```python
def test_scenario_path_a():
    fsm = ScenarioFSM()
    assert fsm.handle(Event("choose_path", "A")) == "Вы выбрали путь A. Продолжаем..."
    assert fsm.state == "path_a"
    assert fsm.handle(Event("continue", None)) == "Вы завершили путь A!"

def test_scenario_path_b():
    fsm = ScenarioFSM()
    assert fsm.handle(Event("choose_path", "B")) == "Вы выбрали путь B. Следующий шаг..."
    assert fsm.state == "path_b"
    assert fsm.handle(Event("continue", None)) == "Вы завершили путь B!"
```

### 🧠 Архитектурные идеи

- Ветвление по выбору пользователя
- Проверка переходов и финальных состояний
- Расширяемость: можно добавить таймеры, условия, побочные эффекты

---

## 🛠️ Расширения

- Используй `pytest.mark.parametrize` для массовых проверок
- Введи `FSMTestCase` с helper-методами (`assert_transition`, `assert_state`)
- Добавь аннотации прямо в код или в docstring теста
- Синхронизируй тесты с документацией FSM-паттернов

---

## 🔗 Связанные главы

- [FSM Patterns](fsm_patterns.md) — шаблоны форм, опросов и сценариев
---
