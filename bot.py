import telebot
from telebot import types
import os

# ====== Настройки ======
TOKEN = os.environ.get("TELEGRAM_TOKEN")
if not TOKEN:
    print("❌ Ошибка: TELEGRAM_TOKEN не задан!")
    exit(1)

bot = telebot.TeleBot(TOKEN)

# ====== Тарифы ======
tariffs = {
    "Базовый": "💡 Базовый тариф — 4800 руб/мес.\n2 занятия в неделю, доступ к записям, проверка дз.",
    "Стандарт": "📘 Стандарт — 6800 руб/мес.\n+ Чат для разговорной практики и дополнительные материалы.",
    "Премиум": "🌟 Премиум — 9500 руб/мес.\n+ Индивидуальное сопровождение и аудиопрактика.",
    "Интенсив": "🔥 Интенсив — 12000 руб/мес.\n3 занятия в неделю + ускоренная программа.",
    "Мини-группа": "👥 Мини-группа — 7200 руб/мес.\nДо 5 человек, живые занятия и обратная связь.",
    "Онлайн": "💻 Онлайн — 4800 руб/мес.\nЗанятия в Zoom + доступ к платформе.",
    "Оффлайн": "🏫 Оффлайн — 7500 руб/мес.\nОчные уроки в школе, все материалы включены.",
    "Пробный": "🎁 Пробный — 0 руб.\nПервое занятие бесплатно, чтобы познакомиться с форматом.",
    "Групповой": "👨‍🏫 Групповой — 5800 руб/мес.\n10 человек, групповая динамика, обратная связь.",
    "Индивидуальный": "👤 Индивидуальный — 14000 руб/мес.\nПолностью под Ваш уровень и график.",
    "Разговорный": "🗣 Разговорный — 5200 руб/мес.\nФокус на живую речь и аудирование.",
    "Детский": "🧒 Детский — 4500 руб/мес.\nИгровая форма, простая грамматика и слова.",
    "Кураторский": "📚 Кураторский — 8800 руб/мес.\nПроверка домашних заданий и персональная обратная связь."
}

# ====== Команда /start ======
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📖 Тарифы")
    btn2 = types.KeyboardButton("📞 Контакты")
    btn3 = types.KeyboardButton("🏫 О школе")
    markup.add(btn1, btn2, btn3)
    bot.send_message(
        message.chat.id,
        "🌸 Добро пожаловать в школу арабского языка, Марии!\nВыберите действие:",
        reply_markup=markup
    )

# ====== Обработка текста ======
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    text = message.text.lower()

    if "тариф" in text or message.text == "📖 Тарифы":
        markup = types.InlineKeyboardMarkup()
        for name in tariffs:
            markup.add(types.InlineKeyboardButton(name, callback_data=name))
        bot.send_message(message.chat.id, "Выберите тариф 👇", reply_markup=markup)

    elif "контакт" in text or message.text == "📞 Контакты":
        bot.send_message(
            message.chat.id,
            "📞 Связаться с нами:\nTelegram: @arabic_school\nEmail: info@arabic-school.ru"
        )

    elif "о школе" in text or message.text == "🏫 О школе":
        bot.send_message(
            message.chat.id,
            "🏫 Наша школа обучает литературному арабскому языку с нуля.\n"
            "— Уроки 2 раза в неделю\n— Проверка домашних заданий\n— Кураторская поддержка\n"
            "— Разговорная практика в Telegram"
        )

    else:
        bot.send_message(
            message.chat.id,
            "Извините, я пока понимаю только команды: тарифы, контакты или о школе 😊"
        )

# ====== Обработка кнопок тарифов ======
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    tariff = call.data
    if tariff in tariffs:
        bot.send_message(call.message.chat.id, tariffs[tariff])
    else:
        bot.send_message(call.message.chat.id, "❌ Неизвестный тариф.")

# ====== Запуск ======
print("✅ Бот запущен и готов к работе!")
bot.infinity_polling()
