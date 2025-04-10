import telebot
from config import API_token


bot = telebot.TeleBot(API_token)

#accepting a new member   
@bot.chat_join_request_handler(func= lambda r: True)
def approve(r):
    bot.approve_chat_join_request(r.chat.id, r.from_user.id)
    bot.send_message(r.chat.id, f'User {r.from_user.first_name} joined the group !')


#sending a message to new member
@bot.message_handler(content_types= ['new_chat_members'])
def welcome(m):
    bot.reply_to(m, f'User {m.from_user.first_name} welcome to the group.')

# pin a message
@bot.message_handler(func= lambda m: m.text == 'پین')
def pin(m):
    bot.pin_chat_message(m.chat.id, m.reply_to_message.id)
    bot.reply_to(m, 'پیام مورد نظر پین شد')




bot.infinity_polling()    