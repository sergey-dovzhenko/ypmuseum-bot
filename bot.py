import telebot

telegram_bot_key = "8127384745:AAH9Ce83P1lYegIOrRlW261g4YVvl9WXKyg"
# telegram_chat_id = "-4849379875"
bot = telebot.TeleBot(telegram_bot_key)

# Replace "YOUR_BOT_TOKEN" with your actual bot token
# bot = telebot.TeleBot("YOUR_BOT_TOKEN")

# Handler for the /start and /help commands
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message.chat.id)
    bot.reply_to(message, "Hello! I am your first Telebot. How can I help you?")

# Handler for all other text messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Start polling for new messages
bot.infinity_polling()