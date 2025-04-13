import telebot
from telebot import types
from config import API_token


bot = telebot.TeleBot(API_token)

items =[
    {
        "id": 1,
        "title": "تحلیل تکنیکال",
        "description": "آموزش اصول تحلیل نمودارهای قیمت بازار فارکس",
        "thumb": "https://i.imgur.com/YsRVrBO.jpg",
        "message": "با تحلیل تکنیکال می‌توانید روند بازار را شناسایی کنید."
    },
    {
        "id": 2,
        "title": "مدیریت ریسک",
        "description": "استراتژی‌های حرفه‌ای برای کنترل ضرر و حفظ سرمایه",
        "thumb": "https://i.imgur.com/EfEOP12.jpg",
        "message": "مدیریت ریسک یکی از کلیدهای موفقیت در معامله‌گری است."
    },
    {
        "id": 3,
        "title": "روانشناسی معامله‌گر",
        "description": "نقش احساسات در تصمیم‌گیری‌های مالی",
        "thumb": "https://i.imgur.com/NLF6WNl.jpg",
        "message": "کنترل هیجانات در معاملات بسیار مهم است."
    },
    {
        "id": 4,
        "title": "تحلیل فاندامنتال",
        "description": "بررسی اخبار و شاخص‌های اقتصادی تأثیرگذار",
        "thumb": "https://i.imgur.com/saUT3UB.jpg",
        "message": "تحلیل فاندامنتال کمک می‌کند تاثیر رویدادهای اقتصادی را پیش‌بینی کنید."
    }
]


@bot.inline_handler(func= lambda query: len(query.query) == 0)
def handle_inline_query(query):
    results = []
    for i in items:
        result = types.InlineQueryResultArticle(
            id= i['id'],
            title= i['title'],
            description= i['description'],
            input_message_content= types.InputTextMessageContent(
                message_text= i['message']
            ),
            thumbnail_url= i['thumb']

        )
        results.append(result)

    bot.answer_inline_query(query.id, results)    











bot.infinity_polling()