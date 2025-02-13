import telebot 
from src.config import API_token
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
import sqlite3

bot = telebot.TeleBot(API_token)
user_ID = []

######################################################
#getting documents from users

# @bot.message_handler(commands=['start', 'help'])
# def handle_start_help(message):
    
#     bot.send_message(message.chat.id, 'welcome to chat.')
#     bot.reply_to(message, 'welcome to chat.')

# @bot.message_handler(content_types = ['document', 'audio'])
# def handle_docs_audio(message):
    # if message.audio:
        # bot.reply_to(message, 'This is an audio file')

    # elif message.document:
    #     bot.reply_to(message, 'This is a document file') 


# @bot.message_handler(regexp= '2025')
# def handle_message(message):
#     bot.reply_to(message, 'This message has content "2025"')  

#######################################################
# handel all message for which the lambda returns True

# @bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])                 
# def handle_text_doc(message):
#     bot.reply_to(message, 'This is a text file')


# handel all message for which the costum function returns True
# def text_doc_message(message):
#     return message.document.mime_type == 'text/plain'

# @bot.message_handler(func=text_doc_message, content_types=['document'])                 
# def handle_text_doc(message):
#     bot.reply_to(message, 'This is a text file ...')


####################################################
# getting name and age from users

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, 'Please enter your name:')
#     bot.register_next_step_handler(message, process_name)

# def process_name(message):
#     name = message.text
#     bot.send_message(message.chat.id, f'Hello {name}!\nHow old are you?')
#     bot.register_next_step_handler(message, process_age)

# def process_age(message):
#     age = message.text
#     bot.send_message(message.chat.id, f'You are {age} years old.\nThank you.')        

###################################################
# getting user_id 

# @bot.message_handler(commands=['start'])
# def welcome(message):
#     bot.send_message(message.chat.id, 'Welcome to our bot')
#     if message.chat.id not in user_ID:
#         user_ID.append(message.chat.id)

# @bot.message_handler(commands=['SUPU2024'])
# def send_update(message):
#     for id in user_ID:
#         bot.send_message(id, 'The product is available.')

#####################################################
# creating inline button

# button1 = InlineKeyboardButton(text='Google', callback_data='Google')
# button2 = InlineKeyboardButton(text='Yahoo', callback_data='Yahoo')
# inline_keyboard = InlineKeyboardMarkup(row_width=1)
# inline_keyboard.add(button1, button2)

# @bot.message_handler(commands=['start'])
# def welcome(message):
#     bot.send_message(message.chat.id, 'Welcome to out Bot.', reply_markup=inline_keyboard)

# # callback query handler for the inline keyboard buttons
# @bot.callback_query_handler(func= lambda call:True)
# def check_button(call):
#     if call.data == 'Google':
#         bot.answer_callback_query(call.id , 'Google is tapped.', show_alert=True)
#     elif call.data == 'Yahoo':
#         bot.answer_callback_query(call.id , 'Yahoo is tapped.')

#####################################################
# adding button 

reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
reply_keyboard.add('Button 1', 'Button 2')

# Handeling the /start command
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, 'Check the following keyboard.', reply_markup=reply_keyboard)

# handeling buttons performance
@bot.message_handler(func=lambda message: True)
def check_button(message):
    if message.text == 'Button 1':
        bot.reply_to(message, 'Button 1 is pressed.')
    elif message.text == 'Button 2':
        bot.reply_to(message, 'Button 2 is pressed.')
    else:
        bot.reply_to(message, f'Your message is: "{message.text}"')        

#####################################################



bot.polling()    