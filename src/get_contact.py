from telebot.types import KeyboardButton,InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from config import API_token
import telebot


bot = telebot.TeleBot(API_token)

#getting contact number
@bot.message_handler(commands = ['start'])
def get_number(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = KeyboardButton(text="ارسال شماره موبایل")
    markup.add(button)
    bot.send_message(message.chat.id, 'خوش آمدید \n قبل از استفاده شماره تلفن خود را وارد کنید', reply_markup = markup)


@bot.message_handler(content_types = ['contact'])
def contact(m):
    print(m.contact)    




bot.infinity_polling()