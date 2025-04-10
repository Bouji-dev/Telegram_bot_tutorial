import telebot
from config import API_token


bot = telebot.TeleBot(API_token)

@bot.message_handler(func= lambda m: m.text == 'افزودن ادمین')
def promote(m):
    bot.promote_chat_member(
        m.chat.id, m.reply_to_message.json['from']['id'],
        can_change_info=True,
        can_delete_messages=True,
        can_edit_messages=True,
        can_pin_messages=True

        
        
    )
    bot.send_message(m.chat.id , f'user became an Admin')
    





bot.infinity_polling()    