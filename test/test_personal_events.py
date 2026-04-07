import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from conftest import USERNAME, PASSWORD
from pages.skyeng_page import TestSkyengPage



@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    ) 
    yield driver
    driver.quit()

@allure.epic("Дипломная работа")
@allure.severity("critical")
@allure.id("Test 1")
@allure.feature("Расписание UI")
@allure.title("Добавление личного события")
@allure.description("Автотест на проверку полного цикла добавления личного события в календаре")
@pytest.mark.ui
def test_add_event(driver):
    with allure.step("Назначить переменую для класса SkyengPage"):
        page = TestSkyengPage(driver)

    with allure.step("Открыть страницу сайта"):
        page.open()

    with allure.step("Авторизоваться и перейти во вкладку расписание"):
        page.authorization(USERNAME, PASSWORD)

    with allure.step("Получть список личных событий"):
        page.waiter()
        events_before = len(driver.find_elements(By.CSS_SELECTOR, "tcc-calendar-event-personal"))

    with allure.step("Нажать на сайте кнопку '+'"):
        page.click_button('[target="schedule page - icon plus - click"]')

    with allure.step("Перейти в окно создания личного события"):
        page.click_button('[class="root -size-m -type-secondary"]')

    with allure.step("Заполнить данные название и описание"):
        page.title_event("Диплом", "Опять работать")

    with allure.step("Создать личное событие"):
        page.click_button('[class="root -type-primary -color-brand -size-m -active"]')

    with allure.step("Проверка что личное событие добавлено"):
        driver.refresh()
        page.waiter()
        events_after = len(driver.find_elements(By.CSS_SELECTOR, "tcc-calendar-event-personal"))
        assert events_after == events_before + 1


@allure.epic("Дипломная работа")
@allure.severity("critical")
@allure.id("Test 2")
@allure.feature("Расписание UI")
@allure.title("Редоктирование личного события")
@allure.description("Автотест на проверку полного цикла редоктирования личного события в календаре")
@pytest.mark.ui
def test_relocation_event(driver):
    with allure.step("Назначить переменую для класса SkyengPage"):
        page = TestSkyengPage(driver)

    with allure.step("Открыть страницу сайта"):
        page.open()

    with allure.step("Авторизоваться и перейти во вкладку расписание"):
        page.authorization(USERNAME, PASSWORD)

    with allure.step("Кликнуть на личное событие"):
        page.waiter()
        page.get_event("Диплом")

    with allure.step("Кликнуть на кнопку редактировать"):
        page.click_button('[class="root -type-primary -color-brand -size-m -active"]')

    with allure.step("Отредактировать данные название и описание"):
        page.title_event("День 2 диплом", "работать и еще раз работать")

    with allure.step("Нажать на кнопку сохранить"):
        page.click_button('[class="root -type-primary -color-brand -size-m -active"]')

    with allure.step("Проверить изинения"):
        driver.refresh()
        page.waiter()
        page.assert_event("День 2 диплом")


@allure.epic("Дипломная работа")
@allure.severity("critical")
@allure.id("Test 3")
@allure.feature("Расписание UI")
@allure.title("Удаление личного события")
@allure.description("Автотест на проверку полного цикла удаления личного события в календаре")
@pytest.mark.ui
def test_delete_event(driver):
    with allure.step("Назначить переменую для класса SkyengPage"):
        page = TestSkyengPage(driver)

    with allure.step("Открыть страницу сайта"):
        page.open()

    with allure.step("Авторизоваться и перейти во вкладку расписание"):
        page.authorization(USERNAME, PASSWORD)

    with allure.step("Получть список личных событий"):
        page.waiter()
        events_before = len(driver.find_elements(By.CSS_SELECTOR, "tcc-calendar-event-personal"))

    with allure.step("Кликнуть на личное событие"):
        page.get_event("День 2 диплом")

    with allure.step("Кликнуть на кнопку удалить"):
        page.click_button('[class="root -type-secondary -color-brand -size-m -active"]')

    with allure.step("Проверка что личное событие удалено"):
        driver.refresh()
        page.waiter()
        events_after = len(driver.find_elements(By.CSS_SELECTOR, "tcc-calendar-event-personal"))
        assert events_after == events_before - 1


@allure.epic("Дипломная работа")
@allure.severity("critical")
@allure.id("Test 4")
@allure.feature("Расписание UI")
@allure.title("Добавление личных событий разного цвета")
@allure.description("Автотест на проверку полного цикла добавления личных событий разного цвета в календаре")
@pytest.mark.ui
def test_add_different_colors_event(driver):
    with allure.step("Назначить переменую для класса SkyengPage"):
        page = TestSkyengPage(driver)

    with allure.step("Открыть страницу сайта"):
        page.open()

    with allure.step("Авторизоваться и перейти во вкладку расписание"):
        page.authorization(USERNAME, PASSWORD)

    with allure.step("Получть список личных событий"):
        page.waiter()
        events_before = len(driver.find_elements(By.CSS_SELECTOR, "tcc-calendar-event-personal"))

    with allure.step("Нажать на сайте кнопку '+'"):
        page.click_button('[target="schedule page - icon plus - click"]')

    with allure.step("Перейти в окно создания личного события"):
        page.click_button('[class="root -size-m -type-secondary"]')

    with allure.step("Заполнить данные название и описание"):
        page.title_event("Диплом", "Опять работать")

    with allure.step("Заполнить данные цвета"):
        page.color_event(0)

    with allure.step("Создать личное событие серого цвета"):
        page.click_button('[class="root -type-primary -color-brand -size-m -active"]')

    with allure.step("Нажать на сайте кнопку '+'"):
        page.click_button('[target="schedule page - icon plus - click"]')

    with allure.step("Перейти в окно создания личного события"):
        page.click_button('[class="root -size-m -type-secondary"]')

    with allure.step("Заполнить данные название и описание"):
        page.title_event("Диплом", "Опять работать")

    with allure.step("Заполнить данные цвета"):
        page.color_event(1)

    with allure.step("Создать личное событие желтого цвета"):
        page.click_button('[class="root -type-primary -color-brand -size-m -active"]')

    with allure.step("Нажать на сайте кнопку '+'"):
        page.click_button('[target="schedule page - icon plus - click"]')

    with allure.step("Перейти в окно создания личного события"):
        page.click_button('[class="root -size-m -type-secondary"]')

    with allure.step("Заполнить данные название и описание"):
        page.title_event("Диплом", "Опять работать")

    with allure.step("Заполнить данные цвета"):
        page.color_event(2)

    with allure.step("Создать личное событие зеленого цвета"):
        page.click_button('[class="root -type-primary -color-brand -size-m -active"]') 

    with allure.step("Нажать на сайте кнопку '+'"):
        page.click_button('[target="schedule page - icon plus - click"]')

    with allure.step("Перейти в окно создания личного события"):
        page.click_button('[class="root -size-m -type-secondary"]')

    with allure.step("Заполнить данные название и описание"):
        page.title_event("Диплом", "Опять работать")

    with allure.step("Заполнить данные цвета"):
        page.color_event(3)

    with allure.step("Создать личное событие фиолетового цвета"):
        page.click_button('[class="root -type-primary -color-brand -size-m -active"]')    

    with allure.step("Проверка что личные события добавлены"):
        driver.refresh()
        page.waiter()
        events_after = len(driver.find_elements(By.CSS_SELECTOR, "tcc-calendar-event-personal"))
        assert events_after == events_before + 4


@allure.epic("Дипломная работа")
@allure.severity("critical")
@allure.id("Test 5")
@allure.feature("Расписание UI")
@allure.title("Добавление личных событий разной продолжительностью")
@allure.description("Автотест на проверку полного цикла добавления личных событий разной продолжительностью в календаре")
@pytest.mark.ui
def test_add_different_time_event(driver):
    with allure.step("Назначить переменую для класса SkyengPage"):
        page = TestSkyengPage(driver)

    with allure.step("Открыть страницу сайта"):
        page.open()

    with allure.step("Авторизоваться и перейти во вкладку расписание"):
        page.authorization(USERNAME, PASSWORD)

    with allure.step("Получть список личных событий"):
        page.waiter()
        events_before = len(driver.find_elements(By.CSS_SELECTOR, "tcc-calendar-event-personal"))

    with allure.step("Нажать на сайте кнопку '+'"):
        page.click_button('[target="schedule page - icon plus - click"]')

    with allure.step("Перейти в окно создания личного события"):
        page.click_button('[class="root -size-m -type-secondary"]')

    with allure.step("Заполнить данные название и описание"):
        page.title_event("Диплом", "Опять работать")

    with allure.step("Заполнить данные по дате"):
        page.date_event("2026-04-02")

    with allure.step("Заполнить данные время начала и окончания"):
        page.time_event("15", "00", "15", "05")

    with allure.step("Создать личное событие продолжительностью 5 мин"):
        page.click_button('[class="root -type-primary -color-brand -size-m -active"]')

    with allure.step("Нажать на сайте кнопку '+'"):
        page.click_button('[target="schedule page - icon plus - click"]')

    with allure.step("Перейти в окно создания личного события"):
        page.click_button('[class="root -size-m -type-secondary"]')

    with allure.step("Заполнить данные название и описание"):
        page.title_event("Диплом", "Опять работать")

    with allure.step("Заполнить данные по дате"):
        page.date_event("2026-04-03")

    with allure.step("Заполнить данные время начала и окончания"):
        page.time_event("10", "00", "18", "00")

    with allure.step("Создать личное событие продолжительностью 8 часов"):
        page.click_button('[class="root -type-primary -color-brand -size-m -active"]')

    with allure.step("Нажать на сайте кнопку '+'"):
        page.click_button('[target="schedule page - icon plus - click"]')

    with allure.step("Перейти в окно создания личного события"):
        page.click_button('[class="root -size-m -type-secondary"]')

    with allure.step("Заполнить данные название и описание"):
        page.title_event("Диплом", "Опять работать")

    with allure.step("Заполнить данные по дате"):
        page.date_event("2026-04-04")

    with allure.step("Заполнить данные время начала и окончания"):
        page.time_event("00", "00", "23", "00")

    with allure.step("Создать личное событие продолжительностью 23 часа"):
        page.click_button('[class="root -type-primary -color-brand -size-m -active"]')

    with allure.step("Проверка что личные события добавлены"):
        driver.refresh()
        page.waiter()
        events_after = len(driver.find_elements(By.CSS_SELECTOR, "tcc-calendar-event-personal"))
        assert events_after == events_before + 3