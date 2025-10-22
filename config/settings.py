import os
from dotenv import load_dotenv

load_dotenv()

# 🔐 Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN", "no-token")

# ⛅ Weather API
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "demo")

# 🔐 Авторизация
VALID_TOKENS = {token for token in os.getenv("VALID_TOKENS", "").split(",") if token}

# 📋 Команда для /start (если понадобится)
AVAILABLE_COMMANDS = {
    "/hello": "Приветствие",
    "/feedback": "Форма обратной связи",
    "/weather <город>": "Погода",
    "/auth <токен>": "Авторизация",
}