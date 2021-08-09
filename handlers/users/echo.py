from aiogram import types
from loader import dp

# Хендлер echo должен быть всегда внизу
# Сообщение от пользователя
@dp.message_handler()
async def bot_echo(message: types.Message):
    chat_id = message.from_user.id
    text = message.text
    # # Запрос
    from loader import bot

    await bot.send_message(chat_id=chat_id,text=text)
    # Ответ на сообщение
    # await message.answer(message.text)