from config import API_token
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
import telebot
bot = telebot.TeleBot(API_token)
user_data = {}

first_button = InlineKeyboardButton("Button1", callback_data="Hi")
second_button = InlineKeyboardButton('Button2', callback_data="Hello")
markup = InlineKeyboardMarkup(row_width=1)
markup.add(first_button ,second_button)

#keyboard button
key_markup = ReplyKeyboardMarkup(resize_keyboard=True , row_width=2)
key_markup.add("ثبت اطلاعات", 'تنظیمات')

#call back query
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.data == 'Hi':
        bot.answer_callback_query(call.id, "خیلی کسخلی به مولا", show_alert=True)
    elif call.data == 'Hello':
        bot.answer_callback_query(call.id, "کی بریم دشت هویج", show_alert=True)

##########################################################
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Menu" , reply_markup = key_markup)

#Reply to keyboard button
@bot.message_handler()
def keyboard(message):
    if message.text == "Shahram":
        bot.send_message(message.chat.id, "Shahram is chamarband")
    elif message.text == "Ehsan":
        bot.send_message (message.chat.id, "Ehsan is the best")    

#######################################################################
#next step handler
@bot.message_handler(func= lambda message: message.text == 'ثبت اطلاعات')
def info(message):
    msg = bot.send_message(message.chat.id , "نام خود را وارد کنید:")
    bot.register_next_step_handler(msg, name)

def name(message) :
    user_data[message.chat.id] = {'name': message.text}
    nm = message.text
    msg = bot.send_message(message.chat.id, "آدرس (کوچه) خود را وارد کنید:")  
    bot.register_next_step_handler(msg, address)

def address(message):
    user_data[message.chat.id]['address'] = message.text
    
    msg = bot.send_message(message.chat.id, "اندازه سایز قد خود را وارد کنید:") 
    bot.register_next_step_handler(msg, ghad) 

def ghad(message):
    user_data[message.chat.id]['height'] = message.text
    bot.send_message(message.chat.id , f":اسم شما {user_data[message.chat.id]['name']} \n"
                                        f"آدرس شما : {user_data[message.chat.id]['address']} \n"
                                        f"قد شما : {user_data[message.chat.id]['height']} ")    
    
######################################################
#message handler
@bot.message_handler(commands=['help', 'cancel'])
def cancel(message):
    bot.send_message(message.chat.id, 'Your command is done')







bot.infinity_polling()    