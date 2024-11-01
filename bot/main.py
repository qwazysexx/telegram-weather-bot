import requests
import datetime
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()

open_weather_token = os.getenv("OPEN_WEATHER_TOKEN")


def get_weather(city, open_weather_token):

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
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Подивись у вікно"


        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        leng_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода в місті: {city}\nТемпература: {cur_weather}C° {wd}\n"
              f"Вологість: {humidity}%\nТиск: {pressure} mmHg\nВітер: {wind} m/s\n"
              f"Схід сонця: {sunrise_timestamp}\nЗахід сонця: {sunset_timestamp}\nТривалість дня: {leng_of_the_day}\n"
              f"Гарного дня!")

    except Exception as ex:
        print(ex)
        print("Check the name city")


def main():
    city = input("Enter a city: ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
