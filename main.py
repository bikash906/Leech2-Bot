import telebot
import os

# अपने BotFather से मिला हुआ token यहाँ डालो
BOT_TOKEN = "8461675502:AAEjGXnXIlLGQFut_iPj0vzNLAnzOpEQU4k"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Hello! Leech1 Bot is online.\nSend me a video and I'll process it soon.")

@bot.message_handler(content_types=['video'])
def handle_video(message):
    bot.reply_to(message, "📸 Received your video!\n(Thumbnail change feature will be added soon.)")

# बॉट को चालू रखना
bot.polling(non_stop=True)
