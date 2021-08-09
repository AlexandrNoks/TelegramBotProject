from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.deep_linking import get_start_link


from filters import IsPrivate
from loader import dp
from re import compile


@dp.message_handler(CommandStart(deep_link=compile(r'\w+')),IsPrivate())
async def bot_start_deeplink(message: types.Message):
    deep_link_args = message.get_args()
    await message.answer(f'Привет, {message.from_user.full_name}! \n'
                         f'Вы находитесь в личной переписке. \n'
                         f'В вашей команде есть диплинк\n'
                         f'Вы передали аргумент {deep_link_args}.\n')


@dp.message_handler(CommandStart(), IsPrivate())
async def bot_start(message: types.Message):
    bot_user = await dp.bot.get_me()
    # Формируем deep_link ссылку
    deep_link = await get_start_link('123')

    # deep_link = f'https://t.me/{bot_user.username}?start=123'
    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         f'Вы находитесь в личной переписке\n'
                         f'В вашей команде нет диплинка\n'
                         f'Ваш диплинк ссылка - {deep_link}.')

