---

# 🧩 FSM Patterns

**Шаблоны для форм, опросов и сценариев.**  
Эта глава показывает, как использовать конечные автоматы (FSM) для пошаговых взаимодействий: от простых форм до ветвящихся сценариев.

---

## 📋 Формы: линейный ввод данных

```python
class FormFSM:
    def __init__(self):
        self.state = "start"
        self.data = {}

    def handle(self, event):
        match (self.state, event.type):
            case ("start", "input_name"):
                self.data["name"] = event.payload
                self.state = "awaiting_email"
                return "Введите ваш email:"
            case ("awaiting_email", "input_email"):
                self.data["email"] = event.payload
                self.state = "done"
                return f"Спасибо, {self.data['name']}! Мы отправим письмо на {self.data['email']}."
            case _:
                return "Не понимаю, повторите ввод."
```

### 🧠 Архитектурные идеи

- `self.data`: временное хранилище, можно заменить на FSM-хранилище.
- `state = "done"`: финальное состояние — удобно для триггеров (отправка, логирование).
- Расширяемо: добавь поля, валидацию, таймауты.

---

## 📊 Опросы: пошаговые вопросы

```python
class SurveyFSM:
    def __init__(self):
        self.state = "q1"
        self.answers = {}

    def handle(self, event):
        match (self.state, event.type):
            case ("q1", "answer"):
                self.answers["q1"] = event.payload
                self.state = "q2"
                return "Вопрос 2: Как часто вы используете наш продукт?"
            case ("q2", "answer"):
                self.answers["q2"] = event.payload
                self.state = "done"
                return "Спасибо за участие!"
```

### 🧠 Архитектурные идеи

- FSM как линейная цепочка: `q1 → q2 → done`
- Можно добавить `q3`, `q4`, или ветвление по ответам
- Подходит для NPS, UX-опросов, сбора обратной связи

---

## 🧬 Сценарии: ветвление по выбору

```python
class ScenarioFSM:
    def __init__(self):
        self.state = "intro"

    def handle(self, event):
        match (self.state, event.type):
            case ("intro", "choose_path"):
                if event.payload == "A":
                    self.state = "path_a"
                    return "Вы выбрали путь A. Продолжаем..."
                elif event.payload == "B":
                    self.state = "path_b"
                    return "Вы выбрали путь B. Следующий шаг..."
            case ("path_a", "continue"):
                return "Вы завершили путь A!"
            case ("path_b", "continue"):
                return "Вы завершили путь B!"
```

### 🧠 Архитектурные идеи

- FSM как интерактивная история
- Подходит для обучения, квестов, сценариев
- Можно добавить таймеры, условия, возвраты

---

## 🧪 Тест-гайд: обучающие главы

```python
def test_form_fsm_flow():
    fsm = FormFSM()
    assert fsm.handle(Event("input_name", "Алиса")) == "Введите ваш email:"
    assert fsm.handle(Event("input_email", "alice@example.com")) == "Спасибо, Алиса! Мы отправим письмо на alice@example.com."
    assert fsm.state == "done"
```

### 📚 Паттерн: каждый тест — это мини-глава

- Инициализация → событие → проверка → финал
- Название теста = заголовок walkthrough
- Добавь аннотации, чтобы тест стал обучающим артефактом

---