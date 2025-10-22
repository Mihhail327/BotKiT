import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage

from core.router import Router
from core.dispatcher import Dispatcher as BotKitDispatcher

from modules.start import start_handler
from modules.hello import hello_handler
from modules.auth import auth_handler
from modules.feedback_form import feedback_handler
from modules.weather import weather_handler

# 🔐 Загрузка токена из .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("❌ Переменная BOT_TOKEN не найдена в .env")

# 🎛 Telegram-бот и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# 🧠 BotKit: маршрутизатор + диспетчер
router = Router()
router.register("/start", start_handler)
router.register("/hello", hello_handler)
router.register("/auth", auth_handler)
router.register("/feedback", feedback_handler)
router.register("/weather", weather_handler)

# 📥 Подключаем FSM-обработку как fallback
router.register(".*", feedback_handler)  # обрабатывает все входящие тексты

botkit = BotKitDispatcher(router)

# 📩 Обработка входящих сообщений
@dp.message()
async def handle_message(message: Message):
    update = {
        "text": message.text,
        "user_id": message.from_user.id,
        "chat_id": message.chat.id
    }
    response = await botkit.dispatch(update)
    await message.answer(response)

# 🚀 Запуск polling
async def start_bot():
    await dp.start_polling(bot)