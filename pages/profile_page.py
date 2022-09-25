from constants.profile_page import ProfilePageConsts
from pages.base_page import BasePage
from pages.header import Header


class ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = ProfilePageConsts
        self.header = Header(self.driver)

    def verify_open_profile_page(self, login):
        """Verify success open the Profile Page"""
        username = login.lower()
        assert self.get_element_text(self.constants.PROFILE_NAME_XPATH) == username, \
            f"Actual message: {self.get_element_text(self.constants.PROFILE_NAME_XPATH)}"
