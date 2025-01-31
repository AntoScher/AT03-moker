import requests
import os
import logging
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()
api_key = os.getenv('api_key')
cat_api_key= os.getenv('cat_api_key')


# Проверка, что переменные окружения корректно загружены
if not api_key or not cat_api_key:
    raise ValueError("api_key & cat_api_key должны быть заданы в файле .env")

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

if __name__ == "__main__":
   print(get_weather(api_key, 'London'))

#THE_CAT_API_KEY
def get_random_cat_image(cat_api_key):
    """
    Функция для получения случайного изображения кошки с использованием TheCatAPI.

    :param cat_api_key: Ключ доступа к API TheCatAPI
    :return: URL случайного изображения кошки
    """
    url = "https://api.thecatapi.com/v1/images/search"
    headers = {
        'x-api-key': cat_api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data[0]['url']
    else:
        print(f"Ошибка: {response.status_code}")
        return None


# Пример использования функции

cat_image_url = get_random_cat_image(cat_api_key)
if cat_image_url:
    print(f"URL случайного изображения кошки: {cat_image_url}")
else:
    print("Не удалось получить изображение кошки")
