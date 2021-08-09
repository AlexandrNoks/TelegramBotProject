from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from date import config

# запросы к боту
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
# Хранение данных
storage = MemoryStorage()
# Диспатчер - обработчик абдейтов
dp = Dispatcher(bot,storage=storage)


