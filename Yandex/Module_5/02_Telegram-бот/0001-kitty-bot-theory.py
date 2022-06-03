# не забудьте установить предварительно библиотеку 
# для раброты с API Telegram (pip install python-telegram-bot)
import telegram
import os
import requests
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler

# Загрузим переменные окружения- там хранится токен от телеграм бота
# Задаём директорию запущенного файла и нужный env файл
path_dotenv = os.path.join(os.path.dirname(__file__), '.env')
# Если в директории найден этот файл, то произведем его чтение
if os.path.exists(path_dotenv):
    load_dotenv(path_dotenv)

TOKEN_BOT = os.environ.get('TOKEN')
MY_CHAT_ID = int(os.environ.get('CHATID'))
API_KITTY = 'https://api.thecatapi.com/v1/images/search'

bot = telegram.Bot(token=TOKEN_BOT)

# Отправка сообщения выбранному чату (Нужно уже быть подписанным на бота /start)
sample_text = 'Тут должен быть самый классный текст!'
# bot.send_message(int(MY_CHAT_ID), sample_text)

updater = Updater(token=TOKEN_BOT)

def get_new_kitty_pic():
    response = requests.get(API_KITTY).json()
    url_kitty_pic = response[0].get('url')
    return url_kitty_pic

def send_kitty_pic(update, context):
    chat_info = update.effective_chat
    context.bot.send_photo(chat_info.id, get_new_kitty_pic())

# Напишем функцию для обработки входящих сообщений
def start_messageing_with__bot(update, context):
    # Сохраняем информацию о чате, откоторого пришло сообщщение
    chat_info = update.effective_chat
    # Узнаем имя нашего пользователя (распарсив запрос update.message)
    username = update.message.chat.first_name
    # Настроим кнопку для сообщения
    button = telegram.ReplyKeyboardMarkup(
        [['/newcat']], 
        resize_keyboard=True)
    # и напишем персональное сообщение
    context.bot.send_message(
        chat_id=chat_info.id,
        text=f'{username}, посмотри какого милого котика я нашёл',
        # добавим кнопку к интерфейсу
        reply_markup=button)
    context.bot.send_photo(chat_info.id, get_new_kitty_pic())

# Обработчик CommandHandler - обрабатывает только указанные команды (не сообщения)
# updater.dispatcher.add_handler(CommandHandler('start', say_hello))

# Зарегистрируем обработчик, который будет обрабатывать только заданные
# сообщения (text, photo, video) и передавать их в указанную функцию
# updater.dispatcher.add_handler(MessageHandler(Filters.text, response_from_bot))

updater.dispatcher.add_handler(CommandHandler('start', start_messageing_with__bot)) 
updater.dispatcher.add_handler(CommandHandler('newcat', send_kitty_pic)) 

# Запускаем polling-опрос бота на наличие обновлений(новых сообщений)
# с интервалом каждые 20 секунд
# updater.start_polling(poll_interval=20.0)
updater.start_polling()

# зацикливаем работу бота - будет работать до тех поро, пока не завершим программу
updater.idle()