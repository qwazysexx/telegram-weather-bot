import requests
import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
import os
from dotenv import load_dotenv
import pytz

load_dotenv()

open_weather_token = os.getenv("OPEN_WEATHER_TOKEN")
tg_bot_token = os.getenv("TG_BOT_TOKEN")

bot = Bot(token=tg_bot_token)
dp = Dispatcher()

def get_recommendation(temp, weather_description, wind_speed):
    if temp > 25:
        return "На вулиці спекотно! Надягніть легкий одяг і візьміть з собою воду."
    elif temp < 5:
        return "Холодно! Одягніться тепліше, шапка і шарф не завадять."
    elif weather_description in ["Rain", "Drizzle"]:
        return "Очікується дощ. Візьміть парасольку і відповідне взуття."
    elif wind_speed > 10:
        return "Сильний вітер. Вдягніть щось тепліше, особливо якщо плануєте гуляти."
    else:
        return "Погода гарна для прогулянки!"

def activity_recommendation(temp, weather_description):
    if temp > 25 and weather_description == "Clear":
        return "Чудова погода для походу на пляж або пікніка!"
    elif temp > 15 and weather_description == "Clear":
        return "Час для прогулянки або легкої пробіжки на свіжому повітрі."
    elif weather_description in ["Rain", "Drizzle"]:
        return "Краще залишитися вдома або взяти з собою парасольку, якщо потрібно вийти."
    elif weather_description == "Snow":
        return "Відмінний день для зимових видів спорту! Не забудьте одягтися тепліше."
    elif temp < 0:
        return "Морозний день. Ідеально для зимових розваг, але одягайтеся тепло!"
    else:
        return "Ви можете насолоджуватися будь-якою активністю на свіжому повітрі!"

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.reply("Привіт! Напиши мені назву міста, і я скажу, яка там зараз погода, а також дам рекомендації щодо одягу та активностей!")

@dp.message()
async def get_weather(message: Message):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Хмарно \U00002601", 
        "Rain": "Дощ \U00002614",
        "Drizzle": "Дощ \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Сніг \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        wd = code_to_smile.get(weather_description, "Подивись у вікно")

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
   
        timezone_offset = data["timezone"]  
        local_timezone = datetime.timezone(datetime.timedelta(seconds=timezone_offset))

        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"], local_timezone)
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"], local_timezone)
        leng_of_the_day = sunset_timestamp - sunrise_timestamp

        clothing_recommendation = get_recommendation(cur_weather, weather_description, wind)
        activity_suggestion = activity_recommendation(cur_weather, weather_description)

        await message.reply(
            f"***{datetime.datetime.now().astimezone(local_timezone).strftime('%Y-%m-%d %H:%M')}***\n"
            f"Погода в місті: {city}\nТемпература: {cur_weather}C° {wd}\n"
            f"Вологість: {humidity}%\nТиск: {pressure} mmHg\nВітер: {wind} m/s\n"
            f"Схід сонця: {sunrise_timestamp.strftime('%H:%M')}\n"
            f"Захід сонця: {sunset_timestamp.strftime('%H:%M')}\nТривалість дня: {leng_of_the_day}\n\n"
            f"***Рекомендації: {clothing_recommendation}***\n"
            f"***Активності: {activity_suggestion}***\n"
            f"***Гарного дня!***"
        )

    except Exception:
        await message.reply("\U00002620 Перевірте назву міста \U00002620")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
