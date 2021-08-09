from aiogram import types
from filters import IsPrivate
from loader import dp

from date.config import admins


@dp.message_handler(IsPrivate(), text='secret', user_id=admins)
async def admin_chat_secret(message: types.Message):
    await message.answer('Это секретное сообщение вызванное одним из администраторов ' 'в личной переписке')

# @dp.message_handlers_mailing(IsPrivate(),text='friend')
# async def chat_mailing(message: types.Message):
#     await message.answer('Привет друг!')


