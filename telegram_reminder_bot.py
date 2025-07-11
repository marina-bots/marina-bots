import telebot
import threading
import time

TOKEN = 'ВАШ_ТОКЕН_ОТ_BOTFATHER'

bot = telebot.TeleBot(TOKEN)
reminders = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Отправь мне сообщение в формате: \n"
                          "/remind <время в секундах> <текст напоминания>")

@bot.message_handler(commands=['remind'])
def set_reminder(message):
    try:
        parts = message.text.split(' ', 2)
        delay = int(parts[1])
        text = parts[2]
        chat_id = message.chat.id

        def reminder():
            time.sleep(delay)
            bot.send_message(chat_id, f"Напоминание: {text}")

        threading.Thread(target=reminder).start()
        bot.reply_to(message, f"Напоминание установлено на {delay} секунд")
    except:
        bot.reply_to(message, "Неверный формат. Используй /remind <секунды> <текст>")

bot.polling()
