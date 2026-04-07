from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestSkyengPage:
    """
		Этот класс представляет собой набор функций для работы с сайтом Skyeng
	"""

    URL = "https://skyeng.ru/teachers"

    def __init__(self, driver) -> None:
        """
			Эта функция инициализирует веб-драйвер
		"""
        self.driver = driver
        driver.maximize_window()


    def open(self) -> None:
        """
			Эта функция открывает страницу по указаному URL
		"""
        self.driver.get(self.URL)


    def click_button(self, item: str) -> None:
        """
			Эта функция принимает на ввод один параметр (локатор кнопки), 
            по которому ищет кнопки на странице и кликает на них.
		""" 
        button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, item))
        )
        button.click()


    def waiter(self) -> None:
        """
			Ожидание загрузки страницы
		""" 
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "tcc-calendar-event-personal"))
        )


    def get_event(self, title_event: str) -> None:
        """
			Эта функция принимает на ввод один параметр название личного события и 
            кликает на него.
		""" 
        events: list = self.driver.find_elements(By.CSS_SELECTOR, "tcc-calendar-event-personal")

        num_in_list: int = None

        for i, event in enumerate(events): 
            if title_event in event.text:
                num_in_list = i
                break

        events[num_in_list].click()


    def assert_event(self, tit_event: str) -> None:
        """
			Эта функция принимает на ввод один параметр название личного события и 
            проверяет что событие с таким название существует.
		""" 
        events: list = self.driver.find_elements(By.CSS_SELECTOR, "tcc-calendar-event-personal")

        num_in_list: int = None

        for i, event in enumerate(events): 
            if tit_event in event.text:
                num_in_list = i
                break

        assert events[num_in_list] is not None
        

    def title_event(self, title: str, description: str) -> None:
        """
			Эта функция принимает на ввод два параметра (название и описание ЛС), 
            вводит их в форму заполнения данных на сайте.
		""" 
        tit = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "input.mt8"))
        )
        tit.clear()
        tit.send_keys(title)

        desc = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.mt8"))
        )
        desc.clear()
        desc.send_keys(description)


    def date_event(self, date_at: str) -> None:
        """
			Эта функция принимает на ввод один параметр дата, формат даты должен быть:
            2026-03-15 минус 1 от для который нужен.
		""" 
        WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "select.mr12"))
        ).click()
        WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 
                        f'option[value="{date_at}T21:00:00.000Z"]'))
        ).click()


    def time_event(self, start_at_hours: str, start_at_min: str,
                  end_at_hours: str, end_at_min: str) -> None:
        """
			Эта функция принимает на ввод четыре параметра (время начала часы, 
            время начала минуты, время окончания часы, время окончания минуты), 
            вводит их в форму заполнения данных на сайте.
		""" 
        hours = self.driver.find_elements(By.CSS_SELECTOR, "input.input-hours")
        minutes = self.driver.find_elements(By.CSS_SELECTOR, "input.input-minutes")

        hours[0].clear()
        hours[0].send_keys(start_at_hours)
        hours[1].clear()
        hours[1].send_keys(end_at_hours)

        minutes[0].clear()
        minutes[0].send_keys(start_at_min)
        minutes[1].clear()
        minutes[1].send_keys(end_at_min)


    def color_event(self, color: int) -> None:
        """
			Эта функция принимает на ввод один параметр - индекс цвета в списке:
            0-серый, 1-желтый, 2-зеленый, 3-фиолетовый.
		""" 
        colors = self.driver.find_elements(By.CSS_SELECTOR, "div.color-circle")
        colors[color].click()

    
    def authorization(self, username: str, password: str) -> None:
        """
			Эта функция принимает на ввод два параметра(лонин и пароль),
            авторизовывает на сайте и переходит во вкладку расписание
		"""
        WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".auth-block-login-button"))
        ).click()
        WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".js-send-otp-form-to-username-password"))
        ).click()
        WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='username']"))
        ).send_keys(username)
        WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='password']"))
        ).send_keys(password)
        WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".js-username-password-form-button"))
        ).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-qa-id='left-menu-item:Расписание']"))
        ).click()


    def get_token_api(self, username: str, password: str):
        """
			Эта функция принимает на ввод два параметра(лонин и пароль),
            авторизовывает на сайте и возвращает Token для API тестов
		"""
        self.open()
        WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".auth-block-login-button"))
        ).click()
        WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".js-send-otp-form-to-username-password"))
        ).click()
        WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='username']"))
        ).send_keys(username)
        WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='password']"))
        ).send_keys(password)
        WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".js-username-password-form-button"))
        ).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[data-qa-id='left-menu-item:Расписание']"))
        ).click()        
        cookies = self.driver.get_cookies()

        for cookie in cookies:
            if cookie['name'] == 'token_global':
                return cookie['value']

        raise Exception("token_global не найден")