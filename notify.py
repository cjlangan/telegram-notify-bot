#!/usr/bin/env python3

import os
import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')
bot = telebot.TeleBot(BOT_TOKEN)

# Command to send the Chat ID
@bot.message_handler(commands=['id'])
def send_id(message):
    chat_id = message.chat.id
    bot.reply_to(message, f"Your id is: {chat_id}")

# function to send the message
def notify():
    message = "Your Command Has Finished Executing."
    bot.send_message(CHAT_ID, message)

notify()
