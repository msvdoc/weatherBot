import telebot
import config
from telebot import types
import pyowm
from pyowm.utils.config import get_default_config
import parsPogoda

#установка русского языка для отображения погоды
config_dict = get_default_config()
config_dict['language'] = 'ru' 

owm = pyowm.OWM(config.tokenOWM, config_dict)

bot = telebot.TeleBot(config.tokenTelebot, "html")

#обработка события "старт", происходит при запуске
@bot.message_handler(commands=["start"])
def start_user(message):
    sti = open("images/Atomicpesets_011.webp", "rb")
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(message.from_user, bot.get_me()))
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    button1 = types.KeyboardButton("Южно-Курильск")
    button2 = types.KeyboardButton("Южно-Сахалинск")
    button3 = types.KeyboardButton("Благовещенск")
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, "Добро пожаловать ", reply_markup = markup)                                                                                  

#обработчик срабатывает при получении сообщения от пользователя
@bot.message_handler(content_types = ["text"])
def speak_echo(message):
    
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]
    bot.send_message(message.chat.id, "Температура: " + str(temp) + " \n" + w.detailed_status)

    if message.text == "Южно-Курильск":
         bot.send_message(message.chat.id, "завтра ночью: " + parsPogoda.tempYKTommor[2].text + ", днём: " + parsPogoda.tempYKTommor[3].text)
    elif message.text == "Южно-Сахалинск":
        bot.send_message(message.chat.id, "завтра ночью: " + parsPogoda.tempYSTommor[2].text + ", днём: " + parsPogoda.tempYSTommor[3].text)
    elif message.text == "Благовещенск":
        bot.send_message(message.chat.id, "завтра ночью: " + parsPogoda.tempBlgTommor[2].text + ", днём: " + parsPogoda.tempBlgTommor[3].text)

bot.polling(none_stop=True)

    
