# First of all, you need to register and get a subscription to this API // В первую очередь вам необходимо зарегистрироваться и получить подписку на этот API:
# https://rapidapi.com/segnayt-e1RorVbq3qe/api/dimondevosint/

import logging
from aiogram import Bot, Dispatcher, executor, types
import requests
import json
from config import *

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher. // Инициализировать бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

print("!Бот запущен!")

# Message handler that sends greeting when bot started // Обработчик сообщений, который отправляет приветствие при запуске бота
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command // Этот обработчик будет вызываться, когда пользователь отправляет команду `/start` или `/help`
    """
    await message.reply("EyeOfGod Bot Template by nulls18: @nulls18")


# This is the main probiv function that returns a json and formats it, then sends it // Это основная функция EyeOfGod, которая возвращает json и форматирует его, а затем отправляет
@dp.message_handler(content_types=['text'])
async def text(message: types.Message):

    # Get the message text and interpret it as a phone number // Получить текст сообщения и интерпретировать его как номер телефона
    nomer = message.text

    # The endpoint for the probiv API that passes as a query the phone number // Конечная точка для EyeOfGod API, которая передает в качестве запроса номер телефона
    url = f"https://dimondevosint.p.rapidapi.com/main?phone={nomer}"

    # Necessary headers for the API to work // Необходимые заголовки для работы API
    head = {
        # RapidAPI necessary host header // Необходимый заголовок хоста RapidAPI
        "X-RapidAPI-Host": "dimondevosint.p.rapidapi.com",
        # API key that you can get by subscribing to the API // Ключ API, который вы можете получить, подписавшись на API
        "X-RapidAPI-Key": RapidAPI_Key
    }

    # Send the request with all the parameters and print the result for debugging // Отправьте запрос со всеми параметрами и распечатайте результат для отладки
    response = requests.get(url, headers=head)
    try:
        data = json.loads(response.text)
        name , country , operator , obyavleniya = data['name'] , data['country'] , data['operator'] , data['obyavleniya']
        await bot.send_message(message.chat.id,f"""
                           
                           👨 ФИО: {name}
                           🏳️ Страна: {country}
                           📱 Оператор: {operator}
                           📓 Объявления: {obyavleniya}

                           @nulls18
                           
                           Код бота: https://github.com/a-wow/EyeOfGod/
                           """)
    except:
        await bot.send_message(message.chat.id,f"""
                           
                           ⛔️ Не удалось достать информацию!
                           @nulls18
                           
                           Код бота: https://github.com/a-wow/EyeOfGod/
                           """)

# Main loop // Основной цикл
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
