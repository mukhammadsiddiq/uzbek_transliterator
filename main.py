from transliterate import to_cyrillic, to_latin
import telebot

Token = '6339346788:AAGEeM5PYnasZDZotGRnTcLkhMp3XQDIIxI'
bot = telebot.TeleBot(Token, parse_mode=None)


@bot.message_handler(commands=['start'])
def greeting(message):
    bot.reply_to(message, "Hey, glad to see you here ;)")


@bot.message_handler(func=lambda message: True)
def echo(message):
    msg = message.text
    result = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, result(msg))


bot.polling()