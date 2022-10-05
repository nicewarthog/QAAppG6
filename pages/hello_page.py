from pages.base_page import BasePage


class HelloPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        from constants.hello_page import HelloPageConst
        self.constants = HelloPageConst()
        from pages.header_before_sign_in import HeaderBeforeSignIn
        self.header_before_sign_in = HeaderBeforeSignIn(self.driver)
        from pages.header_after_sign_in import HeaderAfterSignIn
        self.header_after_sign_in = HeaderAfterSignIn(self.driver)

    def verify_success_sign_up(self, login):
        """Verify success Sign Up using Hello message"""
        login = login.lower()
        # Перевірка, що в Hello message є зареєстрований username
        assert self.get_element_text(self.constants.HELLO_MESSAGE_XPATH) == self.constants.HELLO_MESSAGE_TEXT.format(
            login=login), f"Actual message: {self.get_element_text(self.constants.HELLO_MESSAGE_XPATH)}"
        # Перевірка тільки зареєстрованого username
        assert self.get_element_text(self.constants.HELLO_MESSAGE_USERNAME_XPATH) == login, \
            f"Actual message: {self.get_element_text(self.constants.HELLO_MESSAGE_USERNAME_XPATH)}"
