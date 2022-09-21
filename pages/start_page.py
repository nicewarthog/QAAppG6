from time import sleep

from selenium.webdriver.common.by import By

from constants.start_page import StartPageConstants
from pages.base_page import BasePage


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.costants = StartPageConstants()

    def get_element_text(self, xpath):
        """Find element and get text"""
        # Verify error
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        return element.text

    def sign_up(self, login, email, password):
        """Sign up as the user"""
        # Fill login
        self.fill_field(xpath=self.costants.REG_LOGIN_FIELD_XPATH, value=login)
        sleep(0.5)
        # Fill email
        self.fill_field(xpath=self.costants.REG_EMAIL_FIELD_XPATH, value=email)
        sleep(0.5)
        # Fill password
        self.fill_field(xpath=self.costants.REG_PASS_FIELD_XPATH, value=password)
        sleep(0.5)
        # Click button
        self.click(xpath=self.costants.REG_BUTTON_XPATH)
        sleep(0.5)

    def verify_success_sign_up(self, login):
        """Verify success Sign Up using Hello message"""
        username = login.lower()
        # Перевірка, що в Hello message є зареєстрований username
        assert self.get_element_text(self.costants.HELLO_MESSAGE_XPATH) == self.costants.HELLO_MESSAGE_TEXT.format(
            username=username), f"Actual message: {self.get_element_text(self.costants.HELLO_MESSAGE_XPATH)}"
        sleep(0.5)
        # Перевірка тільки зареєстрованого username
        assert self.get_element_text(self.costants.HELLO_MESSAGE_USERNAME_XPATH) == username, \
            f"Actual message: {self.get_element_text(self.costants.HELLO_MESSAGE_USERNAME_XPATH)}"
        sleep(0.5)

    def verify_sign_up_short_login_error(self):
        """Verify Sign Up to short login message"""
        assert self.get_element_text(
            self.costants.REG_LOGIN_TO_SHORT_MESSAGE_XPATH) == self.costants.REG_LOGIN_TO_SHORT_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(self.costants.REG_LOGIN_TO_SHORT_MESSAGE_XPATH)}"
        sleep(0.5)

    def verify_sign_up_long_login_error(self):
        """Verify Sign Up to long login message"""
        assert self.get_element_text(
            self.costants.REG_LOGIN_TO_LONG_MESSAGE_XPATH) == self.costants.REG_LOGIN_TO_LONG_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(self.costants.REG_LOGIN_TO_LONG_MESSAGE_XPATH)}"
        sleep(0.5)

    def verify_sign_up_taken_login_error(self):
        """Verify Sign Up login is taken message"""
        assert self.get_element_text(
            self.costants.REG_LOGIN_IS_TAKEN_MESSAGE_XPATH) == self.costants.REG_LOGIN_IS_TAKEN_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(self.costants.REG_LOGIN_IS_TAKEN_MESSAGE_XPATH)}"
        sleep(0.5)

    def verify_sign_up_empty_email_error(self):
        """Verify Sign Up to short login message"""
        assert self.get_element_text(
            self.costants.REG_EMAIL_EMPTY_MESSAGE_XPATH) == self.costants.REG_EMAIL_EMPTY_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(self.costants.REG_EMAIL_EMPTY_MESSAGE_XPATH)}"
        sleep(0.5)

    def verify_sign_up_empty_password_error(self):
        """Verify Sign Up to short login message"""
        assert self.get_element_text(
            self.costants.REG_PASS_TO_SHORT_MESSAGE_XPATH) == self.costants.REG_PASS_TO_SHORT_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(self.costants.REG_PASS_TO_SHORT_MESSAGE_XPATH)}"
        sleep(0.5)

    def verify_sign_up_button(self):
        """Verify Sign Up button"""
        assert self.get_element_text(
            self.costants.REG_BUTTON_XPATH) == self.costants.REG_BUTTON_TEXT, \
            f"Actual message: {self.get_element_text(self.costants.REG_BUTTON_XPATH)}"
        sleep(0.5)

    def sing_in(self, login, password):
        """Sign in as the user"""
        # Fill login
        self.fill_field(xpath=self.costants.SIGN_IN_LOGIN_FIELD_XPATH, value=login)
        sleep(0.5)
        # Fill password
        self.fill_field(xpath=self.costants.SIGN_IN_PASS_FIELD_XPATH, value=password)
        sleep(0.5)
        # Click button
        self.click(xpath=self.costants.SIGN_IN_BUTTON_XPATH)
        sleep(0.5)

    def sing_in_with_enter(self, login, password):
        """Sign in as the user"""
        # Fill login
        self.fill_field(xpath=self.costants.SIGN_IN_LOGIN_FIELD_XPATH, value=login)
        # Fill password
        self.fill_field(xpath=self.costants.SIGN_IN_PASS_FIELD_XPATH, value=password)
        sleep(0.5)
        # Click button
        self.press_enter()
        sleep(0.5)

    def verify_sign_in_error(self):
        """Verify invalid Sign In error"""
        assert self.get_element_text(
            self.costants.SIGN_IN_INVALID_DATA_MESSAGE_XPATH) == self.costants.SIGN_IN_INVALID_DATA_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(self.costants.SIGN_IN_INVALID_DATA_MESSAGE_XPATH)}"
        sleep(0.5)

    def verify_sign_in_success(self):
        """Verify correct Sign In"""
        assert self.get_element_text(
            self.costants.ACCOUNT_NAME_XPATH) == self.costants.SIGN_IN_CORRECT_LOGIN_INPUT, \
            f"Actual message: {self.get_element_text(self.costants.ACCOUNT_NAME_XPATH)}"
        sleep(0.5)
