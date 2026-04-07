Автоматизированные тесты Selenium и Requests
Описание проекта

Проект содержит автоматизированные UI-тесты и API-тесты, написанные на Python с использованием Selenium, Pytest и Requests.
Тесты проверяют работу веб-приложения расписание, личные события для преподователей онлайн школы Skyeng

Для формирования отчётов используется Allure.

Используемые технологии:
Python
Pytest
Selenium WebDriver
Requests
Allure
WebDriver Manager

Установка зависимостей
Перед запуском тестов необходимо установить зависимости:
pip install pytest
pip install selenium
pip install requests
pip install webdriver-manager
pip install allure-pytest

Запуск тестов
Перед запуском тестов необходимо запустить скрипт get_token.py, для этого выполните в терминале команду python get_token.py
скрипт печатает в терминале значение token_global необходимое для запуска API-тестов, это значение необходимо подставить в
переменную TOKEN в файле conftest.py
Для запуска всех тестов выполните команду:
pytest
В случае когда Python установлен со стандартного магазина Microsoft:
python -m pytest -v
Для запуска всех UI-тестов выполните команду:
pytest test_personal_events.py
В случае когда Python установлен со стандартного магазина Microsoft:
python -m pytest test_personal_events.py
Для запуска всех API-тестов выполните команду:
pytest test_api_personal_events.py
В случае когда Python установлен со стандартного магазина Microsoft:
python -m pytest test_api_personal_events.py
Для запуска тестов с формированием отчёта Allure:
pytest --alluredir=./allure-results
В случае когда Python установлен со стандартного магазина Microsoft:
python -m pytest --alluredir=./allure-results
После выполнения тестов будет создана папка allure-results, содержащая данные для отчёта.

Просмотр отчёта Allure
Чтобы открыть отчёт, выполните команду:
allure serve allure-results
После этого автоматически откроется браузер с отчётом, где можно посмотреть:
список тестов
статус выполнения
шаги тестов
возможные ошибки