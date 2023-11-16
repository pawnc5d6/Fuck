import os
import telebot
import requests

# Get the bot token from environment variables
bot_token = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['vc'])
def tell_vehicle_info(message):
    try:
        vehicle_id = message.text.split(' ')[1]
        response = requests.get(f"https://lol.game-quasar.com//?vehicleId={vehicle_id}")

        if response.status_code == 200:
            bot.reply_to(message, f"Response: {response.text}")
        else:
            bot.reply_to(message, f"Error: Unable to fetch information for vehicle {vehicle_id}")
    except IndexError:
        bot.reply_to(message, "Error: Please provide a vehicleId after /vc")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

bot.infinity_polling()
