from aiogram import types

from loader import dp

@dp.message_handler(text='Пока')
async def goodnight(message: types.Message):
    await message.answer(text='Спокойной ночи!')