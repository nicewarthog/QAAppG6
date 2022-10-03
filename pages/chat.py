from selenium.webdriver import Keys

from pages.base_page import BasePage


class Chat(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        from constants.chat import ChatConsts
        self.constants = ChatConsts()
        # from pages.header_before_sign_in import HeaderBeforeSignIn
        # self.header_before_sign_in = HeaderBeforeSignIn(self.driver)

    def send_message(self, message):
        """Send provided message"""
        self.fill_field(xpath=self.constants.CHAT_INPUT_XPATH, value=message + Keys.ENTER)  # введення за допомогою Enter

    def verify_messages(self, expected_messages):
        """Verify messages"""
        messages = self.wait_until_all_displayed(xpath=self.constants.CHAT_MESSAGES_XPATH)
        messages_text = [message.text for message in messages]
        assert messages_text == expected_messages
