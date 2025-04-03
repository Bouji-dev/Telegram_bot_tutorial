import telebot
from telebot import types
import time
from config import API_token


bot = telebot.TeleBot(API_token)
first_photo = open("/home/ehsan/projects/telegram-bot/src/logo.jpg", "rb")
second_photo = open("/home/ehsan/projects/telegram-bot/src/logo2.jpg", "rb")

key = types.InlineKeyboardMarkup()
btn = types.InlineKeyboardButton("Button 1", callback_data="btn1")
key.add(btn)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    global mid
    

    f = bot.send_photo(chat_id=message.chat.id, photo= first_photo, caption="first photo ...", reply_markup= key)
    mid = f.message_id
    #time.sleep(3)
    #edit caption of photo
    #bot.edit_message_caption(chat_id= message.chat.id , message_id= f.message_id, caption="caption edited ........")
    #edit photo
    #time.sleep(3)
    #bot.edit_message_media(chat_id= message.chat.id, message_id= f.message_id, media= types.InputMediaPhoto(second_photo, caption= "This is second editet photo"))
    
    #m = bot.send_message(message.chat.id, "This is a test text ... ")
    #time.sleep(3)
    #edit message
    #bot.edit_message_text(chat_id= message.chat.id , message_id= m.message_id, text="This is the edited text ... ...")

    #adding button to photo
    key2 = types.InlineKeyboardMarkup()
    btn2 = types.InlineKeyboardButton("New Button", callback_data="btn2")
    key2.add(btn2)
    @bot.callback_query_handler(func= lambda call : call.data == "btn1")
    def change(call):
        bot.edit_message_reply_markup(chat_id= call.message.chat.id , message_id=mid, reply_markup= key2)
        time.sleep(3)
        #delete message
        
        bot.delete_message(chat_id= call.message.chat.id, message_id= mid)
        bot.send_message(chat_id= call.message.chat.id, text="Message deleted")



















bot.infinity_polling()