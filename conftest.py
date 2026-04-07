import requests
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

USERNAME = "Тут вставьте свой логин"
PASSWORD = "Тут вставьте свой пароль"

BASE_URL = "https://api-teachers.skyeng.ru/v2/schedule/"

TOKEN = "Тут вставьте токен, полученный через скрипт"

headers = {
    "Content-Type": "application/json",
    "Cookie": f"token_global={TOKEN}"
}


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    yield driver
    driver.quit()


@pytest.fixture
def created_event_id():
    """
		Эта функция создает личное событие и 
        возвращает его id.
	""" 
    data = {
    "backgroundColor":"#16A64D",
    "color":"#1FB514",
    "description":"Опять работать",
    "title":"Диплом API",
    "startAt":"2026-04-01T16:00:00+00:00",
    "endAt":"2026-04-01T19:00:00+00:00"
    }
        
    response = requests.post(
        BASE_URL + "createPersonal", 
            headers=headers,
            json=data)
    
    body = response.json()
    event_id = body['data']['payload']['id']

    assert response.status_code == 200

    yield event_id