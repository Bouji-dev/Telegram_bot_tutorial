import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from config import API_token

bot = telebot.TeleBot(API_token)



key_markup = ReplyKeyboardMarkup()
key_markup.add('one', 'two', 'three')

@bot.message_handler(commands=['help'])
def help_me(message):
    bot.reply_to(message, 'what can i do?', reply_markup = key_markup )


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Hi to you')












bot.polling()