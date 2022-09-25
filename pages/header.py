import logging

from constants.header import HeaderConsts
from pages.base_page import BasePage
from pages.utils import wait_until_ok


class Header(BasePage):
    log = logging.getLogger("[CreatePostPage]")

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = HeaderConsts()

    """SIGN IN"""

    def sign_in_and_fail(self, login, password):
        """Sign in as the user"""
        # Fill login
        self.fill_field(xpath=self.constants.SIGN_IN_LOGIN_FIELD_XPATH, value=login)
        # Fill password
        self.fill_field(xpath=self.constants.SIGN_IN_PASS_FIELD_XPATH, value=password)
        # Click button
        self.click(xpath=self.constants.SIGN_IN_BUTTON_XPATH)

    def sign_in_and_verify(self, login, password):
        """Sign in as the user and verify that you are inside"""
        # Fill login
        self.fill_field(xpath=self.constants.SIGN_IN_LOGIN_FIELD_XPATH, value=login)
        # Fill password
        self.fill_field(xpath=self.constants.SIGN_IN_PASS_FIELD_XPATH, value=password)
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

    def hello_page_return(self):
        from pages.hello_page import HelloPage
        return HelloPage(self.driver)

    def sign_in_with_enter(self, login, password):
        """Sign in as the user"""
        # Fill login
        self.fill_field(xpath=self.constants.SIGN_IN_LOGIN_FIELD_XPATH, value=login)
        # Fill password
        self.fill_field(xpath=self.constants.SIGN_IN_PASS_FIELD_XPATH, value=password)
        # Click button
        self.press_enter()

    def verify_sign_in_error(self):
        """Verify invalid Sign In error"""
        assert self.get_element_text(
            self.constants.SIGN_IN_INVALID_DATA_MESSAGE_XPATH) == self.constants.SIGN_IN_INVALID_DATA_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.SIGN_IN_INVALID_DATA_MESSAGE_XPATH)}"

    def verify_sign_in_success(self):
        """Verify correct Sign In"""
        assert self.get_element_text(
            self.constants.ACCOUNT_NAME_XPATH) == self.constants.SIGN_IN_CORRECT_LOGIN_INPUT, \
            f"Actual message: {self.get_element_text(self.constants.ACCOUNT_NAME_XPATH)}"

    def sign_out_click(self):
        """Sign Out from Hello page"""
        # Click button
        self.click(xpath=self.constants.SIGN_OUT_BUTTON_XPATH)

    def verify_sign_out_success(self):
        """Verify correct Sign Out"""
        assert not self.is_exist(self.constants.ACCOUNT_NAME_XPATH)
        assert self.get_element_text(self.constants.SIGN_IN_BUTTON_XPATH) == self.constants.SIGN_IN_BUTTON_TEXT

    """CREATE POST"""

    def navigate_to_create_post(self):
        """Click on create post button"""
        self.click(xpath=self.constants.CREATE_POST_BUTTON_XPATH)
        from pages.create_post_page import CreatePostPage
        return CreatePostPage(self.driver)

    """MY PROFILE"""

    def open_my_profile_page(self):
        """Go to my profile page"""
        # Click My account button
        self.click(xpath=self.constants.MY_PROFILE_BUTTON)
        from pages.profile_page import ProfilePage
        return ProfilePage(self.driver)
