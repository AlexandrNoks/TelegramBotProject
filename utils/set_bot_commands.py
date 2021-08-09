from aiogram import types

# Команды в боте при использовании слеша "/команда"
async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('help', 'Помощь')
    ])