import requests
import pytest
import allure
from conftest import BASE_URL, headers, created_event_id

@allure.epic("Дипломная работа")
@allure.severity("critical")
@allure.id("Test 6")
@allure.feature("Расписание API")
@allure.title("Добавление ЛС API")
@allure.description("Автотест на проверку полного цикла добавления личного события в календаре через API")
@pytest.mark.api
def test_add_event(created_event_id):
    with allure.step("Проверить что ЛС создано"):
        assert created_event_id is not None
    

@allure.epic("Дипломная работа")
@allure.severity("critical")
@allure.id("Test 7")
@allure.feature("Расписание API")
@allure.title("Добавление ЛС за месяц в прошлом API")
@allure.description("Автотест на проверку полного цикла добавления ЛС за месяц в прошлом в календаре через API")
@pytest.mark.api
def test_add_event_past():
    with allure.step("Назначить переменую data для тела запроса с указанием даты за месяц в прошлом"):
        data = {
        "backgroundColor":"#16A64D",
        "color":"#1FB514",
        "description":"Опять работать",
        "title":"Диплом API",
        "startAt":"2026-03-01T16:00:00+00:00",
        "endAt":"2026-03-01T19:00:00+00:00"
    }

    with allure.step("Отправить post запрос"):    
        response = requests.post(
            BASE_URL + "createPersonal", 
                headers=headers,
                json=data)
    
    with allure.step("Записать тело ответа в переменную body"):
        body = response.json()

    with allure.step("Записать в переменную дату начала ЛС"):
        date_event = body['data']['startAt']

    with allure.step("Проверить статус код"):
        assert response.status_code == 200

    with allure.step("Проверить что дата в переменной равна указанной дате"):
        assert date_event == "2026-03-01T16:00:00+00:00"


@allure.epic("Дипломная работа")
@allure.severity("critical")
@allure.id("Test 8")
@allure.feature("Расписание API")
@allure.title("Добавление ЛС разными с цветами API")
@allure.description("Автотест на проверку полного цикла добавления нескольких ЛС с разными цветами через API")
@pytest.mark.api
def test_add_event_different_colors():
    with allure.step("Назначить переменую data для тела запроса с зеленым цветом ЛС"):
        data_green = {
        "backgroundColor":"#16A64D",
        "color":"#1FB514",
        "description":"Опять работать",
        "title":"Диплом API",
        "startAt":"2026-04-01T16:00:00+00:00",
        "endAt":"2026-04-01T19:00:00+00:00"
    }

    with allure.step("Назначить переменую data для тела запроса с красным цветом ЛС"):
        data_red = {
        "backgroundColor":"#E7140D",
        "color":"#E40F0B",
        "description":"Опять работать",
        "title":"Диплом API",
        "startAt":"2026-04-01T16:00:00+00:00",
        "endAt":"2026-04-01T19:00:00+00:00"
    }

    with allure.step("Назначить переменую data для тела запроса с синим цветом ЛС"):
        data_blue = {
        "backgroundColor":"#0D11E7",
        "color":"#0B24E4",
        "description":"Опять работать",
        "title":"Диплом API",
        "startAt":"2026-04-01T16:00:00+00:00",
        "endAt":"2026-04-01T19:00:00+00:00"
    }

    with allure.step("Отправить post запрос на создание ЛС с зеленым цветом"):    
        response = requests.post(
            BASE_URL + "createPersonal", 
                headers=headers,
                json=data_green)
    
    with allure.step("Записать тело ответа в переменную body"):
        body = response.json()

    with allure.step("Записать в переменную цвет ЛС"):
        color_event_1 = body['data']['payload']['payload']['color']

    with allure.step("Проверить статус код"):
        assert response.status_code == 200

    with allure.step("Проверить что цвет в переменной равен указанному цвету"):
        assert color_event_1 == "#1FB514"

    with allure.step("Отправить post запрос на создание ЛС с красным цветом"):    
        response = requests.post(
            BASE_URL + "createPersonal", 
                headers=headers,
                json=data_red)
    
    with allure.step("Записать тело ответа в переменную body"):
        body = response.json()

    with allure.step("Записать в переменную цвет ЛС"):
        color_event_2 = body['data']['payload']['payload']['color']

    with allure.step("Проверить статус код"):
        assert response.status_code == 200

    with allure.step("Проверить что цвет в переменной равен указанному цвету"):
        assert color_event_2 == "#E40F0B"

    with allure.step("Отправить post запрос на создание ЛС с синим цветом"):    
        response = requests.post(
            BASE_URL + "createPersonal", 
                headers=headers,
                json=data_blue)
    
    with allure.step("Записать тело ответа в переменную body"):
        body = response.json()

    with allure.step("Записать в переменную цвет ЛС"):
        color_event_3 = body['data']['payload']['payload']['color']

    with allure.step("Проверить статус код"):
        assert response.status_code == 200

    with allure.step("Проверить что цвет в переменной равен указанному цвету"):
        assert color_event_3 == "#0B24E4"


@allure.epic("Дипломная работа")
@allure.severity("critical")
@allure.id("Test 9")
@allure.feature("Расписание API")
@allure.title("Редоктирование ЛС API")
@allure.description("Автотест на проверку полного цикла редоктирования всех данных ЛС в календаре через API")
@pytest.mark.api
def test_relocation_event(created_event_id):
    with allure.step("Назначить переменую data для тела запроса, изменив данные"):
        data = {
        "backgroundColor":"#D6129F",
        "color":"#580EBF",
        "description":"работать и еще раз работать",
        "title":"Диплом API день 3",
        "startAt":"2026-04-02T10:00:00+00:00",
        "endAt":"2026-04-02T14:00:00+00:00",
        "id": created_event_id,
        "oldStartAt":"2026-04-01T16:00:00+00:00"
    }

    with allure.step("Отправить post запрос"):    
        response = requests.post(
            BASE_URL + "updatePersonal", 
                headers=headers,
                json=data)
    
    with allure.step("Записать тело ответа в переменную body"):
        body = response.json()

    with allure.step("Записать в переменную название ЛС"):    
        event_title = body['data']['payload']['payload']['title']

    with allure.step("Проверить статус код"):
        assert response.status_code == 200

    with allure.step("Проверить что название в переменной равно указанному названию"):
        assert event_title == "Диплом API день 3"



@allure.epic("Дипломная работа")
@allure.severity("critical")
@allure.id("Test 10")
@allure.feature("Расписание API")
@allure.title("Удаление ЛС API")
@allure.description("Автотест на проверку полного цикла удаления ЛС в календаре через API")
@pytest.mark.api
def test_delete_event(created_event_id):
    with allure.step("Назначить переменую data для тела запроса на удаление ЛС"):
        data = {
        "id": created_event_id,
        "startAt":"2026-04-01T16:00:00+00:00"
    }

    with allure.step("Отправить post запрос"):   
        response = requests.post(
            BASE_URL + "removePersonal", 
                headers=headers,
                json=data)
    
    with allure.step("Записать тело ответа в переменную body"):
        body = response.json()

    with allure.step("Записать в переменную данные"):
        event = body['data']

    with allure.step("Проверить статус код"):
        assert response.status_code == 200

    with allure.step("Проверить что ЛС удалено"):
        assert event == True
    