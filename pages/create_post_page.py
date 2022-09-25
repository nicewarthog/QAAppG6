import logging

from constants.create_post_page import CreatePostPageConsts
from pages.base_page import BasePage
from pages.header import Header


class CreatePostPage(BasePage):
    log = logging.getLogger("[CreatePostPage]")

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CreatePostPageConsts()
        self.header = Header(self.driver)

    def create_post(self, title, body):
        """Create post using provided values"""
        self.fill_field(xpath=self.constants.TITLE_FIELD_XPATH, value=title)
        self.fill_field(xpath=self.constants.BODY_FIELD_XPATH, value=body)
        self.click(xpath=self.constants.CREATE_POST_BUTTON_XPATH)

    def verify_successfully_create_post(self):
        """Verify the post is successfully created message"""
        assert self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH) == self.constants.SUCCESS_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH)}"

    def go_to_edit_post(self):
        """Edit post"""
        self.click(xpath=self.constants.EDIT_POST_BUTTON_XPATH)

    def edit_post(self, title, body):
        """Update post using provided values"""
        self.fill_field(xpath=self.constants.TITLE_FIELD_XPATH, value=title)
        self.fill_field(xpath=self.constants.BODY_FIELD_XPATH, value=body)
        self.click(xpath=self.constants.UPDATE_POST_BUTTON_XPATH)

    def verify_successfully_edit_post(self):
        """Verify that the body us updated and message appears"""
        assert self.get_element_text(xpath=self.constants.EDIT_MESSAGE_XPATH) == self.constants.EDIT_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(xpath=self.constants.EDIT_MESSAGE_XPATH)}"
        assert self.get_element_text(xpath=self.constants.BODY_FIELD_XPATH) == self.constants.UPDATE_POST_BODY_TEXT
        self.log.info(f"Actual message: {self.get_element_text(xpath=self.constants.BODY_FIELD_XPATH)}")
        # assert self.get_element_text(xpath=self.constants.TITLE_FIELD_XPATH) == self.constants.UPDATE_POST_TITLE_TEXT

    def delete_post(self):
        """Delete post"""
        self.click(xpath=self.constants.DELETE_POST_BUTTON_XPATH)

    def verify_successfully_delete_post(self):
        """Verify the post is successfully deleted message"""
        assert self.get_element_text(xpath=self.constants.DELETE_MESSAGE_XPATH) == self.constants.DELETE_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(xpath=self.constants.DELETE_MESSAGE_XPATH)}"
