import logging

from selenium.webdriver import Keys

from pages.base_page import BasePage
from pages.utils import wait_until_ok


class HeaderBeforeSignIn(BasePage):
    log = logging.getLogger("[CreatePostPage]")

    def __init__(self, driver):
        super().__init__(driver)
        from constants.header_before_sign_in import HeaderBeforeSignInConsts
        self.constants = HeaderBeforeSignInConsts()
        # from pages.header_after_sign_in import HeaderAfterSignIn
        # self.header_after_sign_in = HeaderAfterSignIn(self.driver)

    def sign_in_and_verify(self, user):
        """Sign in as the user and verify that you are inside"""
        # Fill login
        self.fill_field(xpath=self.constants.SIGN_IN_LOGIN_FIELD_XPATH, value=user.login)
        # login_text = self.get_element_text(xpath=self.constants.SIGN_IN_LOGIN_FIELD_XPATH)
        # Fill password
        self.fill_field(xpath=self.constants.SIGN_IN_PASS_FIELD_XPATH, value=user.password)
        # Click button
        self.click_sign_in_and_verify()
        from pages.hello_page import HelloPage
        return HelloPage(self.driver)

    @wait_until_ok(period=0.25)
    def click_sign_in_and_verify(self):
        """Click Sign In button and verify"""
        # Click button
        self.click(xpath=self.constants.SIGN_IN_BUTTON_XPATH)
        assert not self.is_exist(xpath=self.constants.SIGN_IN_BUTTON_XPATH)
        self.log.info("The Sign In button is not exist. User is on Hello Page")

    def sign_in_with_enter(self, user):
        """Sign in as the user"""
        # Fill login
        self.fill_field(xpath=self.constants.SIGN_IN_LOGIN_FIELD_XPATH, value=user.login)
        # Fill password and press Enter
        self.fill_field(xpath=self.constants.SIGN_IN_PASS_FIELD_XPATH, value=user.password + Keys.ENTER)

    def sign_in_and_fail(self, user):
        """Sign in as the user"""
        # Fill login
        self.fill_field(xpath=self.constants.SIGN_IN_LOGIN_FIELD_XPATH, value=user.login)
        # Fill password
        self.fill_field(xpath=self.constants.SIGN_IN_PASS_FIELD_XPATH, value=user.password)
        # Click button
        self.click(xpath=self.constants.SIGN_IN_BUTTON_XPATH)

    def verify_sign_in_error(self):
        """Verify invalid Sign In error"""
        assert self.get_element_text(
            self.constants.SIGN_IN_INVALID_DATA_MESSAGE_XPATH) == self.constants.SIGN_IN_INVALID_DATA_MESSAGE_TEXT
        self.log.info("Invalid Sign In message appears")

    def verify_sign_out_success(self):
        """Verify correct Sign Out"""
        assert not self.is_exist(self.constants.ACCOUNT_NAME_XPATH)
        assert self.get_element_text(self.constants.SIGN_IN_BUTTON_XPATH) == self.constants.SIGN_IN_BUTTON_TEXT
