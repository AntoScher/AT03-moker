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

def get_weather(api_key, city):
   url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
   response = requests.get(url)
   if response.status_code == 200:
       return response.json()
   else:
       return None

def get_github_user(username):
   url = f'https://api.github.com/users/{username}'
   response = requests.get(url)
   if response.status_code == 200:
       return response.json()
   else:
       return None
