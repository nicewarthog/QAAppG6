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


# Варіант 1. Гірший

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


# Варіант 2. Кращій

class TestStartPage2:
    log = logging.getLogger("[StartPage]")

    @staticmethod
    def random_num():
        """Generate random number"""
        return str(random.randint(111111, 999999))  # число конвертується в рядок

    @staticmethod
    def random_str(length=5):
        """Generate random string"""
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def test_registration(self):
        """
        Steps:
        - Open start page
        - Fill username, email, password
        - Click Sign Up button
        - Verify successfull registration
        """

        # Create driver
        driver = webdriver.Chrome(r"\Users\nicewarthog\PycharmProjects\QAAppG6\chromedriver.exe")

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(1)
        self.log.info("Open page")

        # Fill login
        # user = self.random_str() # змінна user прийняла рандомний рядок
        username_value = f"{self.random_str()}{self.random_num()}"  # змінна username_value з рандомних рядка і числа
        username = driver.find_element(by=By.XPATH,
                                       value=".//input[@id='username-register']")  # знаходимо поле
        username.clear()
        username.send_keys(username_value)
        sleep(1)

        # Fill email
        email_value = f"{self.random_str()}{self.random_num()}@mail.com"
        email = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        email.clear()
        email.send_keys(email_value)
        sleep(1)

        # Fill password
        password_value = f"{self.random_str(6)}{self.random_num()}"
        password = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        password.clear()
        password.send_keys(password_value)
        self.log.info("Fields were filled")
        sleep(1)

        # Click Sign Up button
        # button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign up for OurApp']").click()
        # button.click()
        driver.find_element(by=By.XPATH, value=".//button[text()='Sign up for OurApp']").click()
        sleep(1)

        # Verify success. Тут можна використати різні варіанти однієї перевірки
        """Для початку знаходимо повідомлення 'Hello {username}, your feed is empty.'"""
        hello_message = driver.find_element(by=By.XPATH, value=".//h2")
        """Перевіряємо, що ім'я нового юзера в ловері знаходиться в тексті повідомлення"""
        assert username_value.lower() in hello_message.text
        """Або перевіряємо повністю строку, ім'я повинно співпадати з зареєстрованим"""
        assert hello_message.text == f"Hello {username_value.lower()}, your feed is empty."
        """Або перевіряємо тільки зареєстроване ім'я"""
        assert driver.find_element(by=By.XPATH, value=".//strong").text == username_value.lower()
        self.log.info("Registration for user '%s' was success and verified", username_value)

        # Close driver
        driver.close()
