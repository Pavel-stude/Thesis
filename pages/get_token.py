"""Это скрипт для получения значеня token_global из Cookie"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from skyeng_page import TestSkyengPage

USERNAME = "test.tst345@skyeng.ru"
PASSWORD = "2DbhAAPG6q"

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )

page = TestSkyengPage(driver)
token = page.get_token_api(USERNAME, PASSWORD)

print(token)

driver.quit()
