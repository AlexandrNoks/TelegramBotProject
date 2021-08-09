from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


# Вызов команды help
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Список комманд: ',
        '/start - Начать диалог',
        '/help - Получить справку'
    ]
    await message.answer('\n'.join(text))