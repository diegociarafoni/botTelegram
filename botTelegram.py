import telebot

TOKEN = '1775044147:AAGsOMKSzVBL8I1kyItYenhIBEDJ8PWwxbg'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message, "Benvenuto, sono il primo bot creato da Diego digita /help per scoprire cosa posso fare")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(
        message, "Comando 1 /comando1 \n Comando 2 /comando2")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message)
    bot.reply_to(message, message.text)


bot.polling()
