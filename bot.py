import telebot
from telebot import types

# === 1. Указываем токен Бота ===
TOKEN = "ВАШ_ТОКЕН_ОТ_BOTFATHER"

# === 2. Создаём объект бота ===
bot = telebot.TeleBot(TOKEN)

# === 3. Команда /start ===
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

# === 4. Когда нажимают на кнопку ===
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "get_gift":
        # Отправляем файл
        with open("gift.pdf", "rb") as f:
            bot.send_document(call.message.chat.id, f)
        bot.send_message(call.message.chat.id, "📚 Вот ваш подарок! ❤️")

# === 5. Запуск ===
print("✅ Бот запущен и готов к работе!")
bot.infinity_polling()
