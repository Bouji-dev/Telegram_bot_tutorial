import telebot
bot = telebot.TeleBot('7704240757:AAGcS1TrBvUg63CSWNPU6rrfYO59TUjClWM')
# handel all message for which the lambda returns True
# @bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])                 
# def handle_text_doc(message):
#     bot.reply_to(message, 'This is a text file')

# handel all message for which the costum function returns True
def text_message(message):
    return message.document.mime_type == 'text/plain'

@bot.message_handler(func=text_message, content_types=['document'])                 
def handle_text_doc(message):
    bot.reply_to(message, 'This is a text file ...')