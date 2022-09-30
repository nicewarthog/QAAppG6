import logging
from time import sleep

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import User, Post


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
    def primary_user(self, open_start_page):
        user = User()
        user.sign_in_correct_user_data()
        return user

    @pytest.fixture(scope="function")
    def open_hello_page(self, open_start_page, primary_user):
        """Open Hello page"""
        # username_value = f"{random_str()}{random_num()}"
        # email_value = f"{random_str()}{random_num()}@mail.com"
        # password_value = f"{random_str(6)}{random_num()}"
        # return open_start_page.sign_up_and_verify(username_value, email_value, password_value)
        open_start_page.header_before_sign_in.sign_in_and_verify(primary_user)
        self.log.info("Logged in with correct login and password")
        return open_start_page.hello_page_return()

    @pytest.fixture(scope="function")
    def open_create_post_page(self, open_hello_page):
        create_post_page = open_hello_page.header_after_sign_in.navigate_to_create_post()
        self.log.info("Move to Create Post Page")
        return create_post_page

    @pytest.fixture(scope="function")
    def create_new_post(self, open_create_post_page):
        new_post = Post()
        new_post.post_random_data()
        open_create_post_page.create_post(new_post)
        return new_post

    def test_create_not_unique_post(self, open_create_post_page):
        """
        Pre-conditions:
        - Sign Up/Sign In as the user
        - Navigate to Create Post Page
        Steps:
        - Create new post
        - Verify the post creating
        - Verify the post is not unique
        """

        # Create new post
        new_post = Post()
        new_post.post_random_data()
        open_create_post_page.create_post(new_post)

        # Verify the post creating
        open_create_post_page.verify_successfully_create_post()
        self.log.info("Message that post is successfully created is appeared")

        # Verify the post is not unique
        open_create_post_page.verify_not_unique_post()
        self.log.info("Message that post is not unique is appeared")

    def test_create_unique_post(self, open_create_post_page):
        """
        Pre-conditions:
        - Sign Up/Sign In as the user
        - Navigate to Create Post Page
        Steps:
        - Activate the checkbox
        - Create new post
        - Verify the post creating
        - Verify the post is unique
        """

        # Activate the checkbox
        open_create_post_page.click_checkbox()
        self.log.info("Checkbox is activated")

        # Create new post
        new_post = Post()
        new_post.post_random_data()
        open_create_post_page.create_post(new_post)

        # Verify the post creating
        open_create_post_page.verify_successfully_create_post()
        self.log.info("Message that post is successfully created is appeared")

        # Verify the post is not unique
        open_create_post_page.verify_unique_post()
        self.log.info("Message that post is unique is appeared")

    def test_post_data_saved(self, open_create_post_page):
        """
        Pre-conditions:
        - Sign Up/Sign In as the user
        - Navigate to Create Post Page
        Steps:
        - Create new post
        - Get the saved post and title
        - Verify that the saved post and title are the same to entered data
        """

        # Create new post
        new_post = Post()
        new_post.title = "Test post title"
        new_post.body = "Test post body content"
        open_create_post_page.create_post(Post(new_post.title, new_post.body))

        # Verify the post data is saved
        open_create_post_page.verify_post_data_is_saved()
        self.log.info("The saved data is same to entered data")

    def test_edit_post(self, open_create_post_page, create_new_post):
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
        open_create_post_page.go_to_edit_post()  # дані вводяться в pages.utils
        edited_post = Post()
        edited_post.post_random_data()
        open_create_post_page.edit_post(Post(title="Title is updated", body="Body content is updated"))
        sleep(3)

        # Verify the result
        open_create_post_page.verify_successfully_edit_post()
        self.log.info("Message that post is successfully edited is appeared")

    def test_delete_post(self, open_create_post_page, create_new_post):
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
