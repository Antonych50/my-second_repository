import telebot
import datetime
import time
from threading import Thread
import re

bot = telebot.TeleBot("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

@bot.message_handler(commands=['start'])

def start_message(message):
    bot.reply_to(message, 'Привет! Я чат бот, который будет напоминать тебе пить лекарства!')


def send_reminders():
    m_text = "Ковамлосет - 1 таблетка за 20-30 мин до еды"#morning
    d_text = "Кардицин - 1 капсула во время еды"#dinner
    e_text = "Флуконазол - 1 тбл за 20-30 мин до еды + 0.5 тбл Ковамлосет,\nесли арт давление выше 140"#evening
    while True:
        time.sleep(30)
        now = datetime.datetime.now().strftime("%H:%M")
        match now:
            case "08:00":
                bot.send_message(12345, now+": "+m_text)
                break
            case "12:40":
                bot.send_message(12345, now+": "+d_text)
                break
            case "18:00":
                bot.send_message(12345, now+": "+e_text)
        time.sleep(60)


th = Thread(target=send_reminders)  # , message.chat.id,)
th.start()


bot.polling(none_stop=True)
