import logging
import random
import string
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

"""Homework 13"""

"""
- Створити тест на реєстрацію. 
- Нюанс номер 1: Тест має проходити більше 1 разу, тобто данні в полях мають бути повністю або чатсково випадковими
 (Оскільки той самий юзер не може бути зареєстрований двічі)
- Нюанс номер 2: Вам потрібно самостійно придумати перевірку, що буде підверджувати успішність реєстрації. 
Це може бути перевірка наявності якогось поля, його значення, повідомлення або первірка URL.
"""

log = logging.getLogger(__name__)


@pytest.fixture(scope="class")
def randomword():
    word = string.ascii_lowercase
    return ''.join(random.choice(word) for x in range(8))


class TestStartPage:

    def test_correct_registration(self, randomword):
        """
        Steps:
        - Create driver
        - Open page
        - Fill username
        - Fill email
        - Fill password
        - Click button
        - Verify registration
        """

        # Create driver
        driver = webdriver.Chrome(r"\Users\nicewarthog\PycharmProjects\QAAppG6\chromedriver.exe")

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(1)

        # Fill login
        login = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")

        login.send_keys(randomword, "name")
        sleep(1)

        # Fill email
        email = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        email.send_keys(randomword, "@mail.com")
        sleep(1)

        # Fill password
        password = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        password.send_keys(randomword, "pass")
        sleep(1)

        # Click button
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign up for OurApp']")
        button.click()
        sleep(1)

        # Verify success
        success_element = driver.find_element(by=By.XPATH, value=".//button[text()='Sign Out']")
        assert success_element.text == "Sign Out", f"Actual message: {success_element.text}"
        log.info(
            f"Результат теста - відображається кнопка виходу з аккаунта з текстом {success_element.text}")

        # Close driver
        driver.close()
