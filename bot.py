import telebot
from telebot import types
import os

# ====== Приветствие ======
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("🎁 Получить подарок", callback_data="get_gift")
    markup.add(btn)

    bot.send_message(
        message.chat.id,
        "Привет! 👋\nНажми на кнопку ниже, чтобы получить подарок 🎁",
        reply_markup=markup
    )

# ====== Обработка нажатия кнопки ======
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "get_gift":
        # Отправляем файл (может быть PDF, TXT, изображение и т.д.)
        with open("gift.pdf", "rb") as f:
            bot.send_document(call.message.chat.id, f)

        # Можно добавить сообщение с текстом
        bot.send_message(
            call.message.chat.id,
            "📚 Вот ваш подарок! Здесь также арабский алфавит и слова с транскрипцией."
        )

# ====== Запуск бота ======
bot.infinity_polling()
