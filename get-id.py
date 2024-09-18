import os
import telebot
import subprocess

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# Function to send the chat id.
@bot.message_handler(func=lambda message: True)
def send_id(message):
    chat_id = message.chat.id
    bot.reply_to(message, f"Your chat id is: {chat_id}")

    # Stop the bot from checking for messages
    bot.stop_polling() 
    
    # Export chat ID to an environment variable
    export = f"""echo 'export CHAT_ID="{chat_id}"' >> ~/.bashrc"""
    source = "source ~/.bashrc"
    subprocess.run(export, shell=True)
    subprocess.run(source, shell=True)

    # Give user information
    print(f"Your chat id is: {chat_id}, and has been exported to your path")
    

bot.polling(timeout=1, long_polling_timeout=1)
