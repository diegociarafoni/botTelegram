import telebot
from pytube import YouTube

TOKEN = '1775044147:AAGsOMKSzVBL8I1kyItYenhIBEDJ8PWwxbg'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcomeMessage = "Benvenuto "+message.from_user.first_name + \
        ", sono il primo bot creato da Diego digita /help per scoprire cosa posso fare"
    bot.reply_to(
        message, welcomeMessage)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(
        message, "Scarica i tuoi video da YouTube /youtube")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message)
    bot.reply_to(message, message.text)


@bot.message_handler(commands=['youtube'])
def youTube(message):
    print(message)


bot.polling()
