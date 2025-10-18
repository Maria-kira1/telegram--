import telebot
from telebot import types
import os

# ====== Команда /start ======
@bot.message_handler(commands=['start'])
def start(message):
    # Приветственное сообщение
    text = (
        "🎉 Поздравляем! У вас есть подарок 🎁\n"
        "➡️ Ссылка для получения подарка: https://example.com/gift\n\n"
        "📚 Сегодня мы изучаем арабский алфавит и слова:\n"
        "أ — Alif — Алиф\n"
        "ب — Ba — Ба\n"
        "ت — Ta — Та\n\n"
        "Слова:\n"
        "كِتَاب — Kitaab — Книга\n"
        "مَدْرَسَة — Madrasa — Школа\n"
        "سَلَام — Salaam — Привет"
    )
    bot.send_message(message.chat.id, text)

# ====== Запуск бота ======
print("Бот запущен!")
bot.infinity_polling()
