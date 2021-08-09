import os
from dotenv import load_dotenv


load_dotenv()
# os.getenv возвращает значение ключа key переменной среды.
BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
admins = [
    1875053743,
]
# friends = [1875053743, 1875053747,1875053749,1875053746]

ip = os.getenv('ip')
aiogram_redis = {
    'host': ip,
}
redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
