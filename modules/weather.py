import aiohttp
from config.settings import WEATHER_API_KEY  # ⬅️ Лучше брать ключ из settings

async def weather_handler(update: dict) -> str:
    """
    Команда /weather <город>
    Возвращает текущую погоду через OpenWeatherMap API.
    """
    # 📦 Извлекаем город из текста команды
    parts = update.get("text", "").split(maxsplit=1)

    if len(parts) < 2:
        return "Укажите город: /weather Таллин"

    city = parts[1]

    # 🌐 Формируем URL запроса к OpenWeatherMap
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    )

    # 🔄 Асинхронный HTTP-запрос
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return f"Не удалось получить погоду для {city}."
            data = await resp.json()

    # 🌡️ Извлекаем температуру и описание
    temp = data.get("main", {}).get("temp")
    desc = data.get("weather", [{}])[0].get("description", "нет данных")

    # ✅ Формируем ответ
    return f"🌡️ В {city} сейчас {temp}°C, {desc}"