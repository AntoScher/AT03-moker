main.py

import requests

def get_weather(api_key, city):
   url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
   response = requests.get(url)
   if response.status_code == 200:
       return response.json()
   else:
       return None


test.py

import pytest
from main import get_weather  # замените my_module на имя вашего модуля


def test_get_weather_success(mocker):
   mock_get = mocker.patch('main.requests.get')

   # Создаем мок-ответ для успешного запроса
   mock_get.return_value.status_code = 200
   mock_get.return_value.json.return_value = {
       'weather': [{'description': 'clear sky'}],
       'main': {'temp': 282.55}
   }

   api_key = 'test_api_key'
   city = 'London'
   weather_data = get_weather(api_key, city)

   assert weather_data == {
       'weather': [{'description': 'clear sky'}],
       'main': {'temp': 282.55}
   }

def test_get_weather_failure(mocker):
   mock_get = mocker.patch('main.requests.get')

   # Создаем мок-ответ для неуспешного запроса
   mock_get.return_value.status_code = 404

   api_key = 'test_api_key'
   city = 'UnknownCity'
   weather_data = get_weather(api_key, city)

   assert weather_data is None

