import telebot

TOKEN = "7605281790:AAHhl2iUFuv0vtO4GvCsU3JQ5gQ5ED8wyx4"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    welcome_text = """
👋 Приветствуем тебя в *JarvisXBot*!

🎯 Здесь ты получаешь сигналы по *легендарным стратегиям Lucky Jet* — созданным на опыте, математике и анализе.

🎰 [НАЧАТЬ ИГРАТЬ на 1win](https://goo.su/qnkvtL)  
💰 *Промокод:* `FXX86` — получи бонус на депозит!

⚡ Просто следуй сигналам, делай ставки — и зарабатывай.  
🧠 Наш бот обучается, анализирует и совершенствуется с каждой минутой.

Удачи, чемпион!  
— *Твой Джарвис*
"""
    bot.send_message(message.chat.id, welcome_text, parse_mode="Markdown")

bot.polling()

