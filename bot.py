import telebot

# 🔹 Вставьте сюда ваш токен
TOKEN = "8276344966:AAFPrnz2VMnMli4L3xm8gwC6SydeGnnH6tU"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "✅ Бот успешно запущен и работает!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Вы написали: {message.text}")

if __name__ == "__main__":
    print("🚀 Бот запущен...")
    bot.infinity_polling()
