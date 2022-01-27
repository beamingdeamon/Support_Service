import telebot
import requests
import json
from telebot import types

bot = telebot.TeleBot('1109720830:AAEbIPxSXS0c-S_6rRNx5TVNrg8Aoe2gFN0')
name = "admin"
password = "admin"

NewMessages = []
def sendTelegramMessage(message_text):
    Messages = message_text 

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Enter admin login!")
        bot.register_next_step_handler(message, get_admin_login) #следующий шаг – функция get_name

def get_admin_login(message):
    if message.text == name:
        bot.send_message(message.from_user.id, "Enter adming password!")
        bot.register_next_step_handler(message, get_admin_password)

def get_admin_password(message):
    if message.text == password:
        bot.send_message(message.from_user.id, "Please enter the name of topic to create")
        bot.register_next_step_handler(message, get_subjecttopic)


def get_subjecttopic(message):
    topic = message.text
    response = requests.post('http://localhost:8000/api/createticket/', json={"subject": topic})
    bot.send_message(message.from_user.id, response.status_code)
    bot.send_message(message.from_user.id, "Thks for using this bot :)")



bot.polling(none_stop=True, interval=0)