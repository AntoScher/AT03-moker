import requests
import os
import logging
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()
api_key = os.getenv('api_key')

# Проверка, что переменные окружения корректно загружены
if not api_key:
    raise ValueError(" API_KEY должны быть заданы в файле .env")

# Настройка логирования
logging.basicConfig(level=logging.INFO)

