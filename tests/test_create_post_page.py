import logging

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import random_str


class TestCreatePostPage:
    log = logging.getLogger("[CreatePostPage]")

    @pytest.fixture(scope="function")
    def open_start_page(self):
        """Open Start page"""
        # create driver
        driver = webdriver.Chrome(DRIVER_PATH)
        # open Start Page URL
        driver.get(BASE_URL)
        driver.implicitly_wait(1)
        # Steps
        yield StartPage(driver)
        # Close driver
        driver.close()

    @pytest.fixture(scope="function")
    def open_hello_page(self, open_start_page):
        """Open Hello page"""
        # username_value = f"{random_str()}{random_num()}"
        # email_value = f"{random_str()}{random_num()}@mail.com"
        # password_value = f"{random_str(6)}{random_num()}"
        # return open_start_page.sign_up_and_verify(username_value, email_value, password_value)
        username_value = "nicewarthog"
        password_value = "nicewarthogpass"
        open_start_page.header.sign_in_and_verify(username_value, password_value)
        self.log.info("Logged in with correct login and password")
        return open_start_page.header.hello_page_return()

    @pytest.fixture(scope="function")
    def open_create_post_page(self, open_hello_page):
        create_post_page = open_hello_page.header.navigate_to_create_post()
        self.log.info("Move to Create Post Page")
        return create_post_page

    @pytest.fixture(scope="function")
    def create_new_post(self, open_create_post_page):
        new_post = open_create_post_page.create_post(title=random_str(15), body=random_str(50))
        return new_post

    def test_create_new_post(self, create_new_post, open_create_post_page):
        """
        Pre-conditions:
        - Sign Up/Sign In as the user
        - Navigate to Create Post Page
        - Create new post
        Steps:
        - Verify the result
        """

        # Verify the result
        open_create_post_page.verify_successfully_create_post()
        self.log.info("Message that post is successfully created is appeared")

    def test_edit_post(self, create_new_post, open_create_post_page):
        """
        Pre-conditions:
        - Sign Up/Sign In as the user
        - Navigate to Create Post Page
        - Create new post
        Steps:
        - Edit created post
        - Verify the post is edited
        """

        # Edit Post
        open_create_post_page.go_to_edit_post()
        edited_title = "Title is updated"
        edited_body = "Body content is updated"
        open_create_post_page.edit_post(title=edited_title, body=edited_body)

        # Verify the result
        open_create_post_page.verify_successfully_edit_post()
        self.log.info("Message that post is successfully edited is appeared")

    def test_delete_post(self, create_new_post, open_create_post_page):
        """
        Pre-conditions:
        - Sign Up/Sign In as the user
        - Navigate to Create Post Page
        - Create new post
        Steps:
        - Delete created post
        - Verify the post is deleted
        """

        # Delete Post
        open_create_post_page.delete_post()
        self.log.info("Post is deleted")

        # Verify the post is deleted
        open_create_post_page.verify_successfully_delete_post()
        self.log.info("Message that post is successfully deleted is appeared")
