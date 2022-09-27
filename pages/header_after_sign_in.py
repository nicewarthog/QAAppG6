import logging

from pages.base_page import BasePage


class HeaderAfterSignIn(BasePage):
    log = logging.getLogger("[CreatePostPage]")

    def __init__(self, driver):
        super().__init__(driver)
        from constants.header_after_sign_in import HeaderAfterSignInConsts
        self.constants = HeaderAfterSignInConsts
        from pages.header_before_sign_in import HeaderBeforeSignIn
        self.header_before_sign_in = HeaderBeforeSignIn(self.driver)
        # from pages.start_page import StartPage
        # self.start_page = StartPage(self.driver)

    # SIGN OUT

    def sign_out_click(self):
        """Sign Out from Hello page"""
        # Click button
        self.click(xpath=self.constants.SIGN_OUT_BUTTON_XPATH)

    # SIGN IN

    def verify_sign_in_success(self):
        """Verify correct Sign In"""
        assert self.get_element_text(
            self.constants.ACCOUNT_NAME_XPATH) == self.constants.SIGN_IN_CORRECT_LOGIN_INPUT, \
            f"Actual message: {self.get_element_text(self.constants.ACCOUNT_NAME_XPATH)}"

    # CREATE POST

    def navigate_to_create_post(self):
        """Click on create post button"""
        self.click(xpath=self.constants.CREATE_POST_BUTTON_XPATH)
        from pages.create_post_page import CreatePostPage
        return CreatePostPage(self.driver)

    # MY PROFILE

    def open_my_profile_page(self):
        """Go to my profile page"""
        # Click My account button
        self.click(xpath=self.constants.MY_PROFILE_BUTTON)
        from pages.profile_page import ProfilePage
        return ProfilePage(self.driver)
