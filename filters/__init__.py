from aiogram import Dispatcher

from .private_chat import IsPrivate


def setup(dp:Dispatcher):
    # Привязываем класс методом bind
    dp.filters_factory.bind(IsPrivate)
