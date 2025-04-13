import telebot
import datetime 
from config import API_token


bot = telebot.TeleBot(API_token)

@bot.message_handler(commands=['admin'])
def get_admin(m):
    admins_list = bot.get_chat_administrators(m.chat.id)
    #for admin in admins_list:
        #print(admin.user.username)


    chat = bot.get_chat(chat_id=m.chat.id)
    chat_member = bot.get_chat_member(chat_id= m.chat.id, user_id= m.from_user.id)
    chat_member_count = bot.get_chat_member_count(m.chat.id)
    chat_members_count = bot.get_chat_members_count(m.chat.id)

    # print(chat)
    # print('------------------------')
    # print(chat_member)
    # print('------------------------')
    # print(chat_member_count)
    # print('------------------------')
    # print(chat_members_count)

    #creating invite link
    link = bot.create_chat_invite_link(m.chat.id)
    bot.send_message(m.chat.id , link )




bot.infinity_polling()