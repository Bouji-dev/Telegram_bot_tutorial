import sqlite3
from telebot import TeleBot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
from config import API_token

# create the bot
bot = TeleBot(API_token)

# create keyboard
keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
button = KeyboardButton(text='Send My Info', request_contact=True)
keyboard.add(button)

# create the DataBase
with sqlite3.connect('user.db') as connection:
    cursor = connection.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS users(
        id integer primary key,
        first_name text,
        last_name,
        phone_number text
    
    );
    '''
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id , text='welcome to chat.', reply_markup=keyboard)

@bot.message_handler(content_types=['contact'])
def contact(message):
    #bot.send_message(message.chat.id, text=f'{message.contact}')
    with sqlite3.connect('user.db') as connection:
        cursor = connection.cursor()
        insert_data_query = '''
            INSERT INTO users (id, first_name, last_name, phone_number)
            VALUES (?, ?, ?, ?)
        '''
        data = (
            message.contact.user_id,
            f'{message.contact.first_name}',
            f'{message.contact.last_name}',
            f'{message.contact.phone_number}'
        )
        cursor.execute(insert_data_query, data)

bot.polling()