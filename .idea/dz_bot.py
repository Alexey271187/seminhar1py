


"""мой токен = '5980477244:AAHuGfJGv_t130JTpZCD0Fcnn_YPnXPVmgE'"""

import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import message
from aiogram.types import ParseMode
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)
bot = Bot('5980477244:AAHuGfJGv_t130JTpZCD0Fcnn_YPnXPVmgE')
dp = Dispatcher(bot)

async def start_bot(_):
    print('Бот запущен')

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('Это бот калькулятор\n'
                        'Введите пример на сложение или вычитание:')

@dp.message_handler(content_types=types.ContentType.TEXT)
async def evaluate_expression(message: types.Message):
    expression = message.text
    try:
        result = eval(expression)
        await message.reply(f'Вы в вели: `{expression}`\n Ответ: `{result}`', parse_mode=ParseMode.MARKDOWN)
    except (SyntaxError, ZeroDivisionError, TypeError, NameError):
        await message.reply('Не удалось посчитать.\n Введите пример на сложение или вычитание:')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=start_bot)