#!/usr/bin/env python3

import os
import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')
bot = telebot.TeleBot(BOT_TOKEN)

# function to send the message
def notify():
    message = "Your Command Has Finished Executing."
    bot.send_message(CHAT_ID, message)

notify()
