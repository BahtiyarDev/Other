from telebot import *
import requests

bot = TeleBot('7640420677:AAHfJyL41xSxLL0Nzn_1ODwUJk2DXPdTLNg')
weather_api = 'd43998f72cfece7fb287c00284895803'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, я бот, который поможет вам определить погоду в заданном регионе! Пожалуйста, введи регион для определения погоды: ")

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api}&units=metric')
    if data.status_code == 200:
        data = data.json()
        print(data["weather"][0]["main"])
        if data["weather"][0]["main"] == 'Clouds':
            file = open('cloud.png', 'rb')
            bot.send_photo(message.chat.id,file, caption=f'В {city.capitalize()} сейчас: {data["main"]["temp"]}°С\nПогода Облачная!', reply_to_message_id=message.message_id)
            file.close()
        if data["weather"][0]["main"] == 'Rain':
            file = open('cloud.png', 'rb')
            bot.send_photo(message.chat.id,file, caption=f'В {city.capitalize()} сейчас: {data["main"]["temp"]}°С\nПогода Дождливая!', reply_to_message_id=message.message_id)
            file.close()
        elif data["weather"][0]["main"] == 'Clear':
            file = open('clear.png', 'rb')
            bot.send_photo(message.chat.id,file, caption=f'В {city.capitalize()} сейчас: {data["main"]["temp"]}°С\nПогода Ясная!', reply_to_message_id=message.message_id)
            file.close()
    else:
        bot.reply_to(message, "Проверьте название города")

bot.infinity_polling()


string = ''
