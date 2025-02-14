from config import API_token
from telebot import TeleBot
from telebot.types import KeyboardButton,InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup

import telebot


bot = telebot.TeleBot(API_token)

# Define the main menu
def main_menu():
    markup = InlineKeyboardMarkup()  # for adjust button locations
    button1 = InlineKeyboardButton('Downloads', callback_data='Downloads')
    button2 = InlineKeyboardButton('Setting', callback_data='Setting')
    markup.add(button1, button2)
    return markup

# Define Downloads (Movie and Series)
def submenu1():
    markup = InlineKeyboardMarkup(row_width=1)  # for adjust button locations , # row_width=1 means set buttons as a column 
    button1 = InlineKeyboardButton('Movie', callback_data='submenu1-1')
    button2 = InlineKeyboardButton('Series', callback_data='submenu1-2')
    return_button = InlineKeyboardButton('Return', callback_data='return_to_main')
    markup.add(button1, button2, return_button)
    return markup

# submenu for downloads (Titanic and Breaking Bad)
def submenu1_1():
    markup = InlineKeyboardMarkup(row_width=1)  # for adjust button locations , # row_width=1 means set buttons as a column 
    button = InlineKeyboardButton('Titanic', callback_data='button')
    return_button = InlineKeyboardButton('Return', callback_data='return_to_submenu1')
    markup.add(button, return_button)
    return markup

def submenu1_2():
    markup = InlineKeyboardMarkup(row_width=1)  # for adjust button locations , # row_width=1 means set buttons as a column 
    button = InlineKeyboardButton('Breaking Bad', callback_data='button')
    return_button = InlineKeyboardButton('Return', callback_data='return_to_submenu1')
    markup.add(button, return_button)
    return markup

# Define setting (My profile and Languages)
def submenu2():
    markup = InlineKeyboardMarkup(row_width=1)  # for adjust button locations , # row_width=1 means set buttons as a column 
    button1 = InlineKeyboardButton('My Profile', callback_data='submenu2-1')
    button2 = InlineKeyboardButton('Languages', callback_data='submenu2-2')
    return_button = InlineKeyboardButton('Return', callback_data='return_to_main')
    markup.add(button1, button2, return_button)
    return markup

# submenu for setting (Profile picture and English)
def submenu2_1():
    markup = InlineKeyboardMarkup(row_width=1)  # for adjust button locations , # row_width=1 means set buttons as a column 
    button = InlineKeyboardButton('Profile picture', callback_data='button')
    return_button = InlineKeyboardButton('Return', callback_data='return_to_submenu2')
    markup.add(button, return_button)
    return markup

def submenu2_2():
    markup = InlineKeyboardMarkup(row_width=1)  # for adjust button locations , # row_width=1 means set buttons as a column 
    button = InlineKeyboardButton('English', callback_data='button')
    return_button = InlineKeyboardButton('Return', callback_data='return_to_submenu2')
    markup.add(button, return_button)
    return markup


# Start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Main Menu', reply_markup=main_menu())


# Callback query handler
@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    if call.data == 'Downloads':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Downloads', reply_markup=submenu1())

    elif call.data == 'submenu1-1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Movie', reply_markup=submenu1_1())

    elif call.data == 'submenu1-2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Series', reply_markup=submenu1_2())

    elif call.data == 'Setting':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Setting', reply_markup=submenu2())

    elif call.data == 'submenu2-1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Profile', reply_markup=submenu2_1())

    elif call.data == 'submenu2-2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Languages', reply_markup=submenu2_2())    

    elif call.data == 'return_to_main':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Main Mnue', reply_markup=main_menu())

    elif call.data == 'return_to_submenu1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Downloads', reply_markup=submenu1())

    elif call.data == 'return_to_submenu2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Setting', reply_markup=submenu2())

bot.polling()