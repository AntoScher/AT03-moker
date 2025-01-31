import pytest
from unittest.mock import patch
import requests
from main import get_random_cat_image  # Предположим, что ваша функция находится в файле main.py

def test_get_random_cat_image_success(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{'url': 'https://example.com/cat.jpg'}]

    mocker.patch('requests.get', return_value=mock_response)

    cat_api_key = "fake_api_key"
    result = get_random_cat_image(cat_api_key)
    assert result == 'https://example.com/cat.jpg'

def test_get_random_cat_image_failure(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 404

    mocker.patch('requests.get', return_value=mock_response)

    cat_api_key = "fake_api_key"
    result = get_random_cat_image(cat_api_key)
    assert result is None
