from config import API_token
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
import telebot
bot = telebot.TeleBot(API_token)
user_data = {}




####################################################################
#keyboard button
key_markup = ReplyKeyboardMarkup(resize_keyboard=True , row_width=2)
key_markup.add("ثبت اطلاعات", 'تنظیمات')
key = ReplyKeyboardMarkup(resize_keyboard=True , row_width=2)
key.add(" سوالات متداول", 'خروج')

##########################################################
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Menu" , reply_markup = key_markup)
    bot.send_message(message.chat.id, "Choose an option:", reply_markup= key_markup)

#######################################################################
#next step handler for start command
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
    bot.send_message(message.chat.id , f"اسم شما: {user_data[message.chat.id]['name']} \n"
                                        f"آدرس شما : {user_data[message.chat.id]['address']} \n"
                                        f"قد شما : {user_data[message.chat.id]['height']} ")    

############################################################
#help and cancel command handler
@bot.message_handler(commands=['help', 'cancel'])
def cancel(message):
    bot.send_message(message.chat.id, 'Your command is done', reply_markup= key)


# cancel and help handeler
@bot.message_handler(func= lambda m : m.text == "سوالات متداول")
def faq(message):
    bot.send_message(message.chat.id, 'به بخش سوالات متداول خوش آمدید')

@bot.message_handler(func= lambda m : m.text == "خروج")
def exit(message):
    bot.send_message(message.chat.id, 'خروج شما موفقیت آمیز بود')

# detecting number in messages
@bot.message_handler(regexp= r'\d+')
def number(message):
    bot.send_message(message.chat.id, 'پیام شما حاوی عدد است')

# detecting group and private
@bot.message_handler(chat_types= ['group', 'supergroup'])
def group (message):
    bot.send_message(message.chat.id, 'این پیام شما در گروه است')

@bot.message_handler(chat_types= ['group', 'supergroup'])
def private(message):
    bot.send_message(message.chat.id, 'این پیام شما در چت خصوصی است')

#detecting photo
@bot.message_handler(content_types= ['photo'])
def number(message):
    bot.send_message(message.chat.id, "این پیام حاوی عکس است")


















bot.infinity_polling()    