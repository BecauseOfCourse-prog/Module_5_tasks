import telebot
import datetime
from telebot import types

TG_TOKEN = "7927045347:AAGN9sMEj0WjjSwh2USnpXGQyZ6AEuJ3KbM"
bot = telebot.TeleBot(TG_TOKEN)
data = {}

@bot.message_handler(commands=["start"])
def start(message):
    global data
    bot.send_message(message.chat.id, "Привет! Я буду помогать тебе отслеживать параметры сна. Используй команды /sleep, /wake, /quality и /notes.")
    user_id = message.from_user.id
    data = {user_id: {"start_time": datetime.datetime.now(), "wake_time": datetime.datetime.now(), "duration": 0,
                      "quality": 0, "notes": ""}}


@bot.message_handler(commands=["sleep"])
def sleep(message):
    global data
    bot.send_message(message.chat.id, "Спокойной ночи! Не забудь сообщить мне, когда проснёшься командой /wake.")
    data[message.from_user.id]["start_time"] = datetime.datetime.now()
    data[message.from_user.id]["notes"] = "-"

@bot.message_handler(commands=["wake"])
def wake(message):
    global data
    if data[message.from_user.id]["notes"] == "-":
        f_data = open("data.txt", "a")
        data[message.from_user.id]["wake_time"] = datetime.datetime.now()
        data[message.from_user.id]["duration"] = round(((datetime.datetime.now() - data[message.from_user.id]["start_time"]).total_seconds())/3600, 5)
        bot.send_message(message.chat.id, f"Доброе утро! Ты проспал около {data[message.from_user.id]["duration"]} часов. Не забудь оценить качество сна командой /quality и оставить заметки командой /notes.")
        f_data.write(f"\n{str(data)}")
        f_data.close()
    else:
        bot.send_message(message.chat.id,
                         "Я не вижу, что ты сообщил мне о начале сна. Используй команду /sleep.")

@bot.message_handler(commands=["quality"])
def quality(message):
    global data
    if data[message.from_user.id]["notes"] == "-":
        f_data = open("data.txt", "a")
        bot.send_message(message.chat.id, "Спасибо за оценку качества сна!")
        data[message.from_user.id]["quality"] = message.text[8:]
        f_data.write(f"\n{str(data)}")
        f_data.close()
    else:
        bot.send_message(message.chat.id,
                         "Я не вижу, что ты сообщил мне о начале сна. Используй команду /sleep.")

@bot.message_handler(commands=["notes"])
def notes(message):
    global data
    if data[message.from_user.id]["notes"] == "-":
        f_data = open("data.txt", "a")
        data[message.from_user.id]["notes"] = message.text[6:]
        f_data.write(f"\n{str(data)}")
        f_data.close()
        f_data = open("data.txt", "r")
        bot.send_message(message.chat.id, "Заметка успешно сохранена!")
        f_data.close()
    else:
        bot.send_message(message.chat.id,
                         "Я не вижу, что ты сообщил мне о начале сна. Используй команду /sleep.")




bot.polling(none_stop=True, interval=0)