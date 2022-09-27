from time import sleep

from pages.base_page import BasePage
from pages.utils import wait_until_ok


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        from constants.start_page import StartPageConstants
        self.constants = StartPageConstants()
        from pages.header_before_sign_in import HeaderBeforeSignIn
        self.header_before_sign_in = HeaderBeforeSignIn(self.driver)
        from pages.header_after_sign_in import HeaderAfterSignIn
        self.header_after_sign_in = HeaderAfterSignIn(self.driver)

    # SIGN UP
    def sign_up_and_fail(self, login, email, password):
        """Sign up as the user. Only for incorrect Sign Up"""
        # Fill login
        self.fill_field(xpath=self.constants.REG_LOGIN_FIELD_XPATH, value=login)
        # Fill email
        self.fill_field(xpath=self.constants.REG_EMAIL_FIELD_XPATH, value=email)
        # Fill password
        self.fill_field(xpath=self.constants.REG_PASS_FIELD_XPATH, value=password)
        # Click button
        sleep(1)
        self.click(xpath=self.constants.REG_BUTTON_XPATH)

    def sign_up_and_verify(self, login, email, password):
        """Sign up as the user and verify that you are inside"""
        """
        Це попередній метод, але без сліпа. Разом з методом click_sign_up_and_verify нижче він:
        - заповнює поля
        - за допомогою @wait_until_ok(period=0.25) з base_page перевіряє, що кнопка реєстрації відсутня
        - поки кнопка реєстрації присутня, він запускається протягом 5 сек з інтервалом 0.25 сек
        - як тільки кнопка пропаде і assert виконається, тест піде далі
        """
        # Fill login
        self.fill_field(xpath=self.constants.REG_LOGIN_FIELD_XPATH, value=login)
        # Fill email
        self.fill_field(xpath=self.constants.REG_EMAIL_FIELD_XPATH, value=email)
        # Fill password
        self.fill_field(xpath=self.constants.REG_PASS_FIELD_XPATH, value=password)
        # Click button
        self.click_sign_up_and_verify()  # використали метод нижче, в ньому вже є потрібні @wait_until_ok та assert
        # Return Hello Page
        from pages.hello_page import HelloPage
        return HelloPage(self.driver)

    @wait_until_ok(period=0.25)
    def click_sign_up_and_verify(self):
        """Click Sign Up button and verify"""
        # Click button
        self.click(xpath=self.constants.REG_BUTTON_XPATH)
        assert not self.is_exist(xpath=self.constants.REG_BUTTON_XPATH)

    def verify_sign_up_short_login_error(self):
        """Verify Sign Up to short login message"""
        assert self.get_element_text(
            self.constants.REG_LOGIN_TO_SHORT_MESSAGE_XPATH) == self.constants.REG_LOGIN_TO_SHORT_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.REG_LOGIN_TO_SHORT_MESSAGE_XPATH)}"

    def verify_sign_up_long_login_error(self):
        """Verify Sign Up to long login message"""
        assert self.get_element_text(
            self.constants.REG_LOGIN_TO_LONG_MESSAGE_XPATH) == self.constants.REG_LOGIN_TO_LONG_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.REG_LOGIN_TO_LONG_MESSAGE_XPATH)}"

    def verify_sign_up_taken_login_error(self):
        """Verify Sign Up login is taken message"""
        assert self.get_element_text(
            self.constants.REG_LOGIN_IS_TAKEN_MESSAGE_XPATH) == self.constants.REG_LOGIN_IS_TAKEN_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.REG_LOGIN_IS_TAKEN_MESSAGE_XPATH)}"

    def verify_sign_up_empty_email_error(self):
        """Verify Sign Up to short login message"""
        assert self.get_element_text(
            self.constants.REG_EMAIL_EMPTY_MESSAGE_XPATH) == self.constants.REG_EMAIL_EMPTY_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.REG_EMAIL_EMPTY_MESSAGE_XPATH)}"

    def verify_sign_up_empty_password_error(self):
        """Verify Sign Up to short login message"""
        assert self.get_element_text(
            self.constants.REG_PASS_TO_SHORT_MESSAGE_XPATH) == self.constants.REG_PASS_TO_SHORT_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.REG_PASS_TO_SHORT_MESSAGE_XPATH)}"

    def verify_sign_up_button(self):
        """Verify Sign Up button"""
        assert self.get_element_text(
            self.constants.REG_BUTTON_XPATH) == self.constants.REG_BUTTON_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.REG_BUTTON_XPATH)}"

