import logging

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import User


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    @pytest.fixture(scope="function")
    def open_start_page(self):
        """Open start page"""
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
    def random_user(self):
        user = User()
        user.sign_up_random_user_data()
        return user

    # SIGN UP

    def test_empty_fields_validation(self, open_start_page, random_user):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Don't fill login, email, password in the registration form
        - Click Sign Up button
        - Verify validation messages above login, email and password fields
        """

        # Sign Up as a user
        open_start_page.sign_up_and_fail(User())
        self.log.info("Sign Up with empty login, email, password")

        # Verify wrong registration dat errors
        open_start_page.verify_sign_up_short_login_error()
        self.log.info("Login was to short")
        open_start_page.verify_sign_up_empty_email_error()
        self.log.info("Email was empty")
        open_start_page.verify_sign_up_empty_password_error()
        self.log.info("Password was empty")

    def test_login_is_taken(self, open_start_page, random_user):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Fill correct email, password
        - Fill login that was taken
        - Click Sign Up button
        - Verify error, Verify start page
        """

        # Sign Up as a user
        open_start_page.sign_up_and_fail(User("nicewarthog", random_user.email, random_user.password))
        self.log.info("Sign Up with login, that was taken")

        # Verify login is taken error
        open_start_page.verify_sign_up_taken_login_error()
        self.log.info("Login has already taken")

        # Verify a user is on the start page
        open_start_page.verify_sign_up_button()
        self.log.info("User is on the start page")

    @pytest.mark.parametrize(["lenght", "login"],
                             [("2 symbols", "2s"), ("31 symbols", "31symbols31symbols31symbols31sy"),
                              ("3 symbols", "3sy"), ("30 symbols", "30symbols30symbols30symbols30s")])
    def test_login_lenght(self, lenght, login, open_start_page):
        """
        Fixture:
        -
        Steps:
        - Fill login field with 2 symbols
        - Fill login field with 31 symbols
        - Fill login field with 3 symbols, login must already be taken
        - Fill login field with 30 symbols, login must already be taken
        - Verify error for 2 symbols - Username must be at least 3 characters.
        - Verify error for 31 symbols - Username cannot exceed 30 characters.
        - Verify error for 3, 30 symbols - That username is already taken.
        """

        open_start_page.sign_up_parametrize(login, email="", password="")
        self.log.info("Sign Up with login, that was taken")

        if len(login) < 3:
            # Verify login is to short error
            open_start_page.verify_sign_up_short_login_error()
            self.log.info("Login has less 3 symbols")
        elif len(login) > 30:
            # Verify login is to long error
            open_start_page.verify_sign_up_long_login_error()
            self.log.info("Login has more 30 symbols")
        else:
            # Verify login is taken error
            open_start_page.verify_sign_up_taken_login_error()
            self.log.info("Login has from 3 to 30 symbols and has already taken")

    def test_success_registration(self, open_start_page, random_user):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Fill username, email, password
        - Click Sign Up button
        - Verify success registration
        """

        # Sign Up as a user
        hello_page = open_start_page.sign_up_and_verify(random_user)
        self.log.info("Signed Up as user %s", random_user.login)  # замість %s додається username_value

        # Verify success
        hello_page.verify_success_sign_up(random_user.login)
        self.log.info("Hello message was verified, Sign Up was successfully")

# pytest test_start_page.py
