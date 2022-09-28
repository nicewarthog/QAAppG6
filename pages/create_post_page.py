import logging

from pages.base_page import BasePage


class CreatePostPage(BasePage):
    log = logging.getLogger("[CreatePostPage]")

    def __init__(self, driver):
        super().__init__(driver)
        from constants.create_post_page import CreatePostPageConsts
        self.constants = CreatePostPageConsts()
        from pages.header_before_sign_in import HeaderBeforeSignIn
        self.header_before_sign_in = HeaderBeforeSignIn(self.driver)

    def click_checkbox(self):
        """Click 'Is this post unique?' checkbox"""
        self.click(xpath=self.constants.POST_CHECKBOX_XPATH)

    def create_post(self, post):
        """Create post using provided values"""
        self.fill_field(xpath=self.constants.TITLE_FIELD_XPATH, value=post.title)
        self.fill_field(xpath=self.constants.BODY_FIELD_XPATH, value=post.body)
        self.click(xpath=self.constants.CREATE_POST_BUTTON_XPATH)

    def verify_successfully_create_post(self):
        """Verify the post is successfully created message"""
        assert self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH) == self.constants.SUCCESS_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH)}"

    def verify_unique_post(self):
        """Verify the post is unique message"""
        assert self.get_element_text(xpath=self.constants.UNIQUE_MESSAGE_YES_XPATH) == self.constants.UNIQUE_MESSAGE_YES_TEXT, \
            f"Actual message: {self.get_element_text(xpath=self.constants.UNIQUE_MESSAGE_YES_XPATH)}"

    def verify_not_unique_post(self):
        """Verify the post is not unique message"""
        assert self.get_element_text(xpath=self.constants.UNIQUE_MESSAGE_NO_XPATH) == self.constants.UNIQUE_MESSAGE_NO_TEXT, \
            f"Actual message: {self.get_element_text(xpath=self.constants.UNIQUE_MESSAGE_NO_XPATH)}"

    def verify_post_data_is_saved(self):
        """Verify the post title and body data are saved"""
        assert self.get_element_text(xpath=self.constants.SUCCESS_MESSAGE_XPATH) == self.constants.SUCCESS_MESSAGE_TEXT
        assert self.get_element_text(xpath=self.constants.SAVED_POST_BODY_XPATH) == self.constants.POST_BODY_INPUT
        self.log.info(f"Actual message: {self.get_element_text(xpath=self.constants.SAVED_POST_BODY_XPATH)}")
        assert self.get_element_text(xpath=self.constants.SAVED_POST_TITLE_XPATH) == self.constants.POST_TITLE_INPUT
        self.log.info(f"Actual message: {self.get_element_text(xpath=self.constants.SAVED_POST_TITLE_XPATH)}")

    def go_to_edit_post(self):
        """Edit post"""
        self.click(xpath=self.constants.EDIT_POST_BUTTON_XPATH)

    def edit_post(self, post):
        """Update post using provided values"""
        self.fill_field(xpath=self.constants.TITLE_FIELD_XPATH, value=post.title)
        self.fill_field(xpath=self.constants.BODY_FIELD_XPATH, value=post.body)
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
