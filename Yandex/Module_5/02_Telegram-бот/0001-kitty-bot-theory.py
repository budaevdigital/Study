# не забудьте установить предварительно библиотеку 
# для раброты с API Telegram (pip install python-telegram-bot)
import telegram
import os
from dotenv import load_dotenv
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler

# Загрузим переменные окружения- там хранится токен от телеграм бота
# Задаём директорию запущенного файла и нужный env файл
path_dotenv = os.path.join(os.path.dirname(__file__), '.env')
# Если в директории найден этот файл, то произведем его чтение
if os.path.exists(path_dotenv):
    load_dotenv(path_dotenv)

TOKEN_BOT = os.environ.get('TOKEN')
MY_CHAT_ID = int(os.environ.get('CHATID'))

bot = telegram.Bot(token=TOKEN_BOT)

# Отправка сообщения выбранному чату (Нужно уже быть подписанным на бота /start)
sample_text = 'Тут должен быть самый классный текст!'
# bot.send_message(int(MY_CHAT_ID), sample_text)

updater = Updater(token=TOKEN_BOT)

# Напишем функцию для обработки входящих сообщений
def response_from_bot(update, context):
    # Сохраняем информацию о чате, откоторого пришло сообщщение
    chat_info = update.effective_chat
    
    # задаём сообщение, которое будет отправляться в ответ
    context.bot.send_message(chat_id=chat_info.id, text='Я, KittyBot!')
                       
def say_hello(update, context):
    chat_info = update.effective_chat
    context.bot.send_message(chat_id=chat_info.id, text='И снова здравствуйте!')

# Обработчик CommandHandler - обрабатывает только указанные команды (не сообщения)
updater.dispatcher.add_handler(CommandHandler('start', say_hello))

# Зарегистрируем обработчик, который будет обрабатывать только заданные
# сообщения (text, photo, video) и передавать их в указанную функцию
updater.dispatcher.add_handler(MessageHandler(Filters.text, response_from_bot))

# Запускаем polling-опрос бота на наличие обновлений(новых сообщений)
# с интервалом каждые 20 секунд
updater.start_polling(poll_interval=20.0)

# зацикливаем работу бота - будет работать до тех поро, пока не завершим программу
updater.idle()