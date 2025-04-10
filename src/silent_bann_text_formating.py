import telebot
import datetime 
from config import API_token


bot = telebot.TeleBot(API_token)
@bot.message_handler(commands= ['start'])
def start(m):
    bold_text = '<b>This text is bold</b>'
    italic_text = '<i>This text is italic</i>'
    mono_text = '<code>This text is mono</code>'
    underline_text = '<ins>This text is underline</ins>'
    stric_text = '<s>This text is stric</s>'
    spoiler_text = '|| شهرام چاقال است||'
    hyperlink_text = '[This is link text](https://www.linkedin.com/in/ehsan-shayegh/)'

    bot.send_message(m.chat.id, bold_text, parse_mode='HTML')
    bot.send_message(m.chat.id, italic_text, parse_mode='HTML')
    bot.send_message(m.chat.id, mono_text, parse_mode='HTML')
    bot.send_message(m.chat.id, underline_text, parse_mode='HTML')
    bot.send_message(m.chat.id, stric_text, parse_mode='HTML')
    bot.send_message(m.chat.id, spoiler_text, parse_mode='MarkdownV2')
    bot.send_message(m.chat.id, hyperlink_text, parse_mode='MarkdownV2')

#Silenting user
@bot.message_handler(func= lambda m: m.text.startswith('ساکت'))
def mute_user(m):
    duration = int(m.text.split()[-1])
    date = datetime.datetime.now()+ datetime.timedelta(minutes= duration)
    until_date = int(date.timestamp())

    bot.restrict_chat_member(
        m.chat.id, m.reply_to_message.from_user.id,
        until_date= until_date,
        can_send_media_messages=False,
        can_send_messages= False,
        can_send_other_messages=False,
        can_send_polls=False
    )
    bot.reply_to(m, f'کاربر فضول به مدت {duration} دقیقه ساکت شد')


#banning user
@bot.message_handler(func= lambda m: m.text.startswith('مسدود'))
def mute_user(m):
    duration = int(m.text.split()[-1])
    date = datetime.datetime.now()+ datetime.timedelta(minutes= duration)
    until_date = int(date.timestamp())

    bot.ban_chat_member(
        m.chat.id, m.reply_to_message.from_user.id,
        until_date= until_date,

    )
    bot.reply_to(m, f'کاربر فضول به مدت {duration} دقیقه مسدود شد')


bot.infinity_polling()
