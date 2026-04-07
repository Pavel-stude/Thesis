# Автоматизированные тесты (UI и API)

## Описание проекта

Проект содержит автоматизированные тесты для веб-приложения расписания преподавателей онлайн-школы Skyeng.

Реализованы:

* UI-тесты с использованием Selenium
* API-тесты с использованием Requests

Тесты написаны на Python с использованием pytest.
Для формирования отчетов используется Allure.

---

## Используемые технологии

* Python
* Pytest
* Selenium WebDriver
* Requests
* Allure
* WebDriver Manager

---

## Установка зависимостей

Перед запуском тестов установите зависимости:

```bash
pip install -r requirements.txt
```

---

## Подготовка данных для авторизации

Перед запуском тестов необходимо указать свои данные в файле `conftest.py`:

```python
USERNAME = "your_login"
PASSWORD = "your_password"
TOKEN = "your_token"
```

* `USERNAME` — логин от аккаунта
* `PASSWORD` — пароль
* `TOKEN` — значение `token_global`, полученное через скрипт

---

## Получение токена

Для получения `token_global` выполните:

```bash
python gettoken.py
```

Скопируйте полученное значение и вставьте его в переменную `TOKEN` в файле `conftest.py`.

---

## Запуск тестов

### Запуск всех тестов

```bash
pytest
```

---

### Запуск только UI-тестов

```bash
pytest -m ui
```

---

### Запуск только API-тестов

```bash
pytest -m api
```

---

## Формирование отчета Allure

```bash
pytest --alluredir=allure-results
```

После выполнения тестов будет создана папка `allure-results`.

---

## Просмотр отчета

```bash
allure serve allure-results
```

После выполнения команды откроется браузер с результатами выполнения тестов.

---

## Структура проекта

```
Thesis/
│
├── test/              # тесты
├── pages/             # Page Object
├── conftest.py        # фикстуры и данные авторизации
├── pytest.ini         # конфигурация pytest
├── requirements.txt   # зависимости
```

---

## Примечание

Если используется Python из Microsoft Store, запуск выполняется так:

```bash
python -m pytest
```
