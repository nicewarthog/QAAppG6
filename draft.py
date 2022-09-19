import logging
import random
import string
from time import sleep

import pyautogui
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def chrome_driver():
    # Create driver
    return webdriver.Chrome(r"\Users\nicewarthog\PycharmProjects\QAAppG6\chromedriver.exe")


@pytest.fixture()
def open_start_page(chrome_driver):
    # Open start page
    return chrome_driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

    """-----REGISTRATION-----"""


class TestRegistration:
    log = logging.getLogger("[Registration]")

    @staticmethod
    def random_num():
        """Generate random number"""
        return str(random.randint(111111, 999999))

    @staticmethod
    def random_str(length=5):
        """Generate random string"""
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def test_empty_fields_validation(self, chrome_driver, open_start_page):
        """
        Fixture:
        - Create driver
        - Open page
        Steps:
        - Don't fill login, email, password in the registration form
        - Click Sign Up button
        - Verify validation messages above login, email and password fields
        """

        # Click Sign Up button
        sign_up_button = chrome_driver.find_element(by=By.XPATH,
                                                    value=".//button[text()='Sign up for OurApp']")
        sign_up_button.click()
        sleep(1)

        # Verify validation messages above login, email and password fields
        empty_login_validation = chrome_driver.find_element(by=By.XPATH,
                                                            value=".//div[contains(text(),'Username must be at least 3 characters.')]")
        assert empty_login_validation.text == "Username must be at least 3 characters."
        empty_email_validation = chrome_driver.find_element(by=By.XPATH,
                                                            value=".//div[contains(text(),'You must provide a valid email address.')]")
        assert empty_email_validation.text == "You must provide a valid email address."
        empty_pass_validation = chrome_driver.find_element(by=By.XPATH,
                                                           value=".//div[contains(text(),'Password must be at least 12 characters.')]")
        assert empty_pass_validation.text == "Password must be at least 12 characters."
        self.log.info("Validation messages for empty login, email and password fields are verified")
        assert sign_up_button.is_displayed()  # додаткова перевірка, що входу не було

        # Close driver
        chrome_driver.close()

    def test_login_is_taken(self, chrome_driver, open_start_page):
        """
        Fixture:
        - Create driver
        - Open page
        Steps:
        - Fill correct email, password
        - Fill login that was taken
        - Click Sign Up button
        - Verify error
        - Verify start page
        """

        # Fill email
        email_value = f"{self.random_str()}{self.random_num()}@mail.com"
        email = chrome_driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        email.clear()
        email.send_keys(email_value)
        sleep(1)

        # Fill password
        password_value = f"{self.random_str(6)}{self.random_num()}"
        password = chrome_driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        password.clear()
        password.send_keys(password_value)
        self.log.info("Fields were filled")
        sleep(1)

        # Fill login
        username = chrome_driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        taken_login = "nicewarthog"
        username.send_keys(taken_login)
        sleep(1)

        # Click Sign Up button
        chrome_driver.find_element(by=By.XPATH, value=".//button[text()='Sign up for OurApp']").click()
        sleep(1)

        # Verify error
        login_is_taken_message = chrome_driver.find_element(by=By.XPATH,
                                                            value=".//div[contains(text(),'That username is already taken.')]")
        assert login_is_taken_message.text == "That username is already taken."
        assert chrome_driver.find_element(by=By.XPATH,
                                          value=".//button[text()='Sign up for OurApp']").is_displayed()  # додаткова перевірка, що входу не було
        self.log.info(f"Login {taken_login} has already taken")

        # Close driver
        chrome_driver.close()

    @pytest.mark.parametrize(["lenght", "login"],
                             [("2 symbols", "2s"), ("31 symbols", "31symbols31symbols31symbols31sy"),
                              ("3 symbols", "3sy"), ("30 symbols", "30symbols30symbols30symbols30s")])
    def test_login_lenght(self, lenght, login):
        """
        Fixture:
        -
        Steps:
        - Fill login field with 2 symbols
        - Fill login field with 31 symbols
        - Fill login field with 3 symbols, login must already be taken
        - Fill login field with 30 symbols, login must already be taken
        - Verify error for 2 symbols - Username must be at least 3 characters.
        - Verify error for 31 symbols - Username cannot exceed 30 characters.
        - Verify error for 3, 30 symbols - That username is already taken.
        """

        # Create driver
        driver = webdriver.Chrome(r"\Users\nicewarthog\PycharmProjects\QAAppG6\chromedriver.exe")

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(1)

        # Fill login
        username = driver.find_element(by=By.XPATH,
                                       value=".//input[@id='username-register']")
        sleep(1)
        username.send_keys(login)
        sleep(1)
        driver.find_element(by=By.XPATH, value=".//button[text()='Sign up for OurApp']").click()
        sleep(1)
        if len(login) < 3:
            s2_login_validation = driver.find_element(by=By.XPATH,
                                                      value=".//div[contains(text(),'Username must be at least 3 characters.')]")
            assert s2_login_validation.text == "Username must be at least 3 characters."
            self.log.info("В логіні менше трьох символів")
        elif len(login) > 30:
            s31_login_validation = driver.find_element(by=By.XPATH,
                                                       value=".//div[contains(text(),'Username cannot exceed 30 characters.')]")
            assert s31_login_validation.text == "Username cannot exceed 30 characters."
            self.log.info("В логіні ,більше 30 символів")
        else:
            # Як перевірити, що валідація не з'являється???
            other_login_validation = driver.find_element(by=By.XPATH,
                                                         value=".//div[contains(text(),'That username is already taken.')]")
            assert other_login_validation.text == "That username is already taken."
            self.log.info("В логіні не менше 3 та не більше 31 символа")

        # Close driver
        driver.close()

    # Успішна реєстрація. Гірший варіант, без фікстур
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
        self.log.info(
            f"Результат теста - відображається кнопка виходу з аккаунта з текстом {success_element.text}")

        # Close driver
        driver.close()

    # Успішна реєстрація. Кращій варіант
    def test_success_registration(self, chrome_driver, open_start_page):
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
        # button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign up for OurApp']")
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

    """-----LOG IN-----"""
    """
    - correct login - nicewarthog
    - correct pass - nicewarthogpass 
    """


class TestLogIn:
    log = logging.getLogger("[Log In]")

    def test_empty_login(self, chrome_driver, open_start_page):
        """
        Fixture:
        - Create driver
        - Open page
        Steps:
        - Clear login, fill correct password
        - Click Sign In button
        - Verify error
        """

        # Fill login
        login = chrome_driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login.clear()
        sleep(1)

        # Fill password
        password = chrome_driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.send_keys("nicewarthogpass")
        sleep(1)

        # Click button
        button = chrome_driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        sleep(1)

        # Verify error
        error_element = chrome_driver.find_element(by=By.XPATH,
                                                   value=".//div[@class='alert alert-danger text-center']")
        assert error_element.is_displayed()  # перевірка, що "Invalid username / pasword" відображається
        assert error_element.text == "Invalid username / pasword", f"Actual message: {error_element.text}"

        # Close driver
        chrome_driver.close()

    def test_empty_password(self, chrome_driver, open_start_page):
        """
        Fixture:
        - Create driver
        - Open page
        Steps:
        - Fill correct login, clear password
        - Click Sign In button
        - Verify error
        """

        # Fill login
        login = chrome_driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login.send_keys("nicewarthog")
        sleep(1)

        # Fill password
        password = chrome_driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        sleep(1)

        # Click button
        button = chrome_driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        sleep(1)

        # Verify error
        error_element = chrome_driver.find_element(by=By.XPATH,
                                                   value=".//div[@class='alert alert-danger text-center']")
        assert error_element.is_displayed()  # перевірка, що "Invalid username / pasword" відображається
        assert error_element.text == "Invalid username / pasword", f"Actual message: {error_element.text}"

        # Close driver
        chrome_driver.close()

    def test_incorrect_login(self, chrome_driver, open_start_page):
        """
        Fixture:
        - Create driver
        - Open page
        Steps:
        - Fill incorrect login
        - Fill correct password
        - Click Sign in button
        - Verify error
        """

        # Fill login
        login = chrome_driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login.send_keys("incorrectuser")
        sleep(1)

        # Fill password
        password = chrome_driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.send_keys("nicewarthogpass")
        sleep(1)

        # Click button
        button = chrome_driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        sleep(1)

        # Verify error
        error_element = chrome_driver.find_element(by=By.XPATH,
                                                   value=".//div[@class='alert alert-danger text-center']")
        assert error_element.text == "Invalid username / pasword", f"Actual message: {error_element.text}"

        # Close driver
        chrome_driver.close()

    def test_incorrect_password(self, chrome_driver, open_start_page):
        """
        Fixture:
        - Create driver
        - Open page
        Steps:
        - Fill correct login
        - Fill incorrect password
        - Click Sign in button
        - Verify error
        """

        # Fill login
        login = chrome_driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login.send_keys("nicewarthog")
        sleep(1)

        # Fill password
        password = chrome_driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.send_keys("incorrectpass")
        sleep(1)

        # Click button
        button = chrome_driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        sleep(1)

        # Verify error
        error_element = chrome_driver.find_element(by=By.XPATH,
                                                   value=".//div[@class='alert alert-danger text-center']")
        assert error_element.text == "Invalid username / pasword", f"Actual message: {error_element.text}"

        # Close driver
        chrome_driver.close()

    def test_correct_log_in(self, chrome_driver, open_start_page):
        """
        Fixture:
        - Create driver
        - Open page
        Steps:
        - Fill correct login, fill correct password
        - Click Sign In button
        - Verify successfull log in account
        """

        # Fill login
        login = chrome_driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login_value = "nicewarthog"
        login.send_keys(login_value)
        sleep(1)

        # Fill password
        password = chrome_driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.send_keys("nicewarthogpass")
        sleep(1)

        # Click button
        button = chrome_driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        sleep(1)

        # Verify account name
        account_name = chrome_driver.find_element(by=By.XPATH,
                                                  value=".//span[@class='text-white mr-2']")
        assert account_name.text == f"{login_value}", f"Actual message: {login_value}"

        # Close driver
        chrome_driver.close()

    def test_enter_key(self, chrome_driver, open_start_page):
        """
        Fixture:
        - Create driver
        - Open page
        Steps:
        - Fill correct login, fill correct password
        - Press Enter on keyboard
        - Verify successfull log in account
        """

        # Fill login
        login = chrome_driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login_value = "nicewarthog"
        login.send_keys(login_value)
        sleep(0.5)

        # Fill password
        password = chrome_driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.send_keys("nicewarthogpass")
        sleep(0.5)

        # Press Enter
        pyautogui.press('Enter')
        sleep(0.5)

        # Verify account name
        account_name = chrome_driver.find_element(by=By.XPATH,
                                                  value=".//span[@class='text-white mr-2']")
        assert account_name.text == f"{login_value}", f"Actual message: {login_value}"

        # Close driver
        chrome_driver.close()

# pytest test_start_page.py
