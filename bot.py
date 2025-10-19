import telebot
from telebot import types

# 🔹 Ваш токен
TOKEN = "8276344966:AAFJYL6ixjl45owzCckww4kAK5C5javgfH0"

bot = telebot.TeleBot(TOKEN)

# 🔹 Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("🎁 Получить подарок")
    markup.add(btn)
    bot.send_message(
        message.chat.id,
        "🎉 Привет! Рада видеть Вас здесь!\n\n"
        "Я приготовил для Вас подарок — полезный PDF-файл с арабским алфавитом.\n"
        "Нажмите кнопку ниже, чтобы получить его 👇",
        reply_markup=markup
    )

# 🔹 Когда пользователь нажимает кнопку
@bot.message_handler(func=lambda message: message.text == "🎁 Получить подарок")
def send_gift(message):
    try:
        with open("Написание арабских букв.pdf", "rb") as file:
            bot.send_document(
                message.chat.id,
                file,
                caption="📘 Вот Ваш подарок — «Написание арабских букв»!\nУдачи в изучении арабского языка 🌙"
            )
    except Exception as e:
        bot.reply_to(message, f"⚠️ Ошибка при отправке файла: {e}")

# 🔹 Остальные сообщения
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Нажмите кнопку 🎁, чтобы получить подарок!")

if __name__ == "__main__":
    print("🚀 Бот запущен...")
    bot.infinity_polling()
