import telebot

TOKEN = "7605281790:AAHhl2iUFuv0vtO4GvCsU3JQ5gQ5ED8wyx4"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(
        message.chat.id,
        "Добро пожаловать в JetSignalBot!\n\n"
        "Регистрируйся по ссылке: https://goo.su/qnkvtL\n"
        "Промокод: *FXX86* — активируй его при регистрации и получи бонусы!\n\n"
        "Нажми /signal чтобы получить торговый сигнал."
    )

@bot.message_handler(commands=['signal'])
def signal(message):
    bot.send_message(
        message.chat.id,
        "Сигнал: ставка 100₽, автокэшаут 1.5x. Шанс: 85%.")
    
bot.polling()
