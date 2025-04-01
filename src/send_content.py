import telebot
from telebot import types
import time
from config import API_token

media = []

bot = telebot.TeleBot(API_token)

@bot.message_handler(commands= ['start'])
def send_content(message):
    #bot.send_chat_action(message.chat.id, action='typing')
    #we use sleep just for waisting time( not recommended in real code)
    #time.sleep(3)
    # bot.send_message(message.chat.id, "Welcome ...")
    # bot.send_chat_action(message.chat.id, action='upload_photo')
    # bot.send_photo(message.chat.id, open("/home/ehsan/projects/telegram-bot/src/logo.jpg", 'rb'))
    # bot.send_chat_action(message.chat.id, action='upload_audio')
    # bot.send_audio(message.chat.id, open("/home/ehsan/projects/telegram-bot/src/audio.mp3", 'rb'))
    # bot.send_chat_action(message.chat.id, action='upload_document')
    # bot.send_document(message.chat.id, open("/home/ehsan/projects/telegram-bot/src/resume.pdf", 'rb'))
    # bot.send_chat_action(message.chat.id, action='upload_video')
    # bot.send_video(message.chat.id, open("/home/ehsan/projects/telegram-bot/src/video.mp4", 'rb'))
    
    #sending many content to user
    p1 = types.InputMediaDocument(open("/home/ehsan/projects/telegram-bot/src/resume.pdf", 'rb'))
    p2 = types.InputMediaDocument(open("/home/ehsan/projects/telegram-bot/src/resume.pdf", 'rb'))
    media.append(p1)
    media.append(p2)
    bot.send_media_group(message.chat.id, media=media)










bot.infinity_polling()    