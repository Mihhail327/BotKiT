from aiogram import Bot, Dispatcher as AiogramDispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram import F
import asyncio

from config.settings import BOT_TOKEN
from core.dispatcher import Dispatcher as BotKitDispatcher
from core.router import Router

# Импортируем обработчики
from modules.hello import hello_handler
from modules.feedback_form import feedback_handler
from modules.auth import auth_handler
from modules.weather import weather_handler
from modules.start import start_handler

# Инициализируем Telegram-бот
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = AiogramDispatcher()

# Инициализируем BotKit
router = Router()
router.register("/hello", hello_handler)
router.register("/feedback", feedback_handler)
router.register("/auth", auth_handler)
router.register("/weather", weather_handler)
router.register("/start", start_handler)

botkit = BotKitDispatcher(router)


@dp.message(CommandStart())
async def handle_start(message: Message):
    update = {
        "user_id": message.from_user.id,
        "text": "/start"
    }
    response = await botkit.dispatch(update)
    await message.answer(response)


@dp.message(F.text)
async def handle_text(message: Message):
    update = {
        "user_id": message.from_user.id,
        "text": message.text
    }
    response = await botkit.dispatch(update)
    await message.answer(response)


def run():
    print("🚀 BotKit Telegram Adapter запущен")
    dp.run_polling(bot)