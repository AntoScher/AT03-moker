main.py

import requests

def get_github_user(username):
   url = f'https://api.github.com/users/{username}'
   response = requests.get(url)
   if response.status_code == 200:
       return response.json()
   else:
       return None


test.py

import pytest
from main import get_github_user

def test_get_github_user(mocker):
   mock_get = mocker.patch('main.requests.get')
   mock_get.return_value.status_code = 200
   mock_get.return_value.json.return_value = {
       'login' : 'nizavr',
       'id' : 345178,
       'name' : 'Nina'
   }

   user_data = get_github_user('cat')
   assert user_data == {
       'login' : 'nizavr',
       'id' : 345178,
       'name' : 'Nina'
   }

def test_get_github_user_with_error(mocker):
   mock_get = mocker.patch('main.requests.get')
   mock_get.return_value.status_code = 500

   user_data = get_github_user('cat')
   assert user_data == None


