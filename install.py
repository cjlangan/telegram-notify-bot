import os
import telebot
import subprocess

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# Function to get id and install the software
@bot.message_handler(func=lambda message: True)
def install(message):
    # Send chat id inside telegram.  THis is technically not needed.
    chat_id = message.chat.id
    bot.reply_to(message, f"Your chat id is: {chat_id}")

    # Stop the bot from checking for messages
    bot.stop_polling() 
    
    # Command to set enivronment variable and add script to path
    var_name = "CHAT_ID"
    export = f"""echo 'export {var_name}="{chat_id}"' >> ~/.bashrc"""
    source = "source ~/.bashrc"
    add_path = "sudo cp notify.py /usr/local/bin/notify"

    # Open bashrc file
    bashrc_path = os.path.expanduser("~/.bashrc")
    with open(bashrc_path, "r") as bashrc:
        bashrc_content = bashrc.read()

    # Only export if variable name doesn't already exist in bashrc
    if var_name not in bashrc_content:
        subprocess.run(export, shell=True)

    # Run command
    subprocess.run(source, shell=True)
    subprocess.run(add_path, shell=True)

    # Give user information
    print(f"""Your chat id is: {chat_id}, and has been exported to your path. 
    You may now use append " && notify" to any command""")

    # Use the notify script :)
    subprocess.run("notify", shell=True)
    

bot.polling(timeout=1, long_polling_timeout=1)
