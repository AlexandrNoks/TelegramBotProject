import logging

from aiogram import Dispatcher

from date.config import admins
# Обработка исключений
async def on_startup_notify(dp: Dispatcher):
    # Проходим по всем admin отправлем им сообщение, что бот запущен
    for admin in admins:
        try:
            await dp.bot.send_message(admin,'Бот Запущен и готов к работе')
        except Exception as err:
            logging.exception(err)
