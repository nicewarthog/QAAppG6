import logging
from time import sleep

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import random_str, random_num


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    @pytest.fixture(scope="function")
    def open_start_page(self):
        """Open start page"""
        # create driver
        driver = webdriver.Chrome(DRIVER_PATH)
        # open Start Page URL
        driver.get(BASE_URL)
        yield StartPage(driver)
        # Close driver
        driver.close()

    """-----REGISTRATION-----"""

    def test_empty_fields_validation(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Don't fill login, email, password in the registration form
        - Click Sign Up button
        - Verify validation messages above login, email and password fields
        """

        # Sign Up as a user
        open_start_page.sign_up("", "", "")
        self.log.info("Sign Up with empty login, email, password")

        # Verify wrong registration dat errors
        open_start_page.verify_sign_up_short_login_error()
        self.log.info("Login was to short")
        open_start_page.verify_sign_up_empty_email_error()
        self.log.info("Email was empty")
        open_start_page.verify_sign_up_empty_password_error()
        self.log.info("Password was empty")

    def test_login_is_taken(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Fill correct email, password
        - Fill login that was taken
        - Click Sign Up button
        - Verify error, Verify start page
        """

        # Prepare data
        email_value = f"{random_str()}{random_num()}@mail.com"
        password_value = f"{random_str(6)}{random_num()}"

        # Sign Up as a user
        open_start_page.sign_up("nicewarthog", email_value, password_value)
        self.log.info("Sign Up with login, that was taken")

        # Verify login is taken error
        open_start_page.verify_sign_up_taken_login_error()
        self.log.info("Login has already taken")
        sleep(0.5)

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

        open_start_page.sign_up(login, email="", password="")
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
            sleep(0.5)

    def test_success_registration(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Fill username, email, password
        - Click Sign Up button
        - Verify success registration
        """

        # Prepare data
        username_value = f"{random_str()}{random_num()}"
        email_value = f"{random_str()}{random_num()}@mail.com"
        password_value = f"{random_str(6)}{random_num()}"

        # Sign Up as a user
        open_start_page.sign_up(username_value, email_value, password_value)
        self.log.info("Signed Up as user %s", username_value)  # замість %s додається username_value

        # Verify success
        open_start_page.verify_success_sign_up(username_value)
        self.log.info("Hello message was verified, Sign Up was successfully")

    """-----LOG IN-----"""
    """
    - correct login - nicewarthog
    - correct pass - nicewarthogpass 
    """

    def test_empty_login(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Clear login, fill correct password
        - Click Sign In button
        - Verify error
        """

        # Sign In with empty login
        open_start_page.sing_in("", "nicewarthogpass")
        self.log.info("Logged in as non-existing user")

        # Verify error
        open_start_page.verify_sign_in_error()
        self.log.info("Error was verified")

    def test_empty_password(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Fill correct login, clear password
        - Click Sign In button
        - Verify error
        """

        # Sign In with empty login
        open_start_page.sing_in("nicewarthog", "")
        self.log.info("Logged in as non-existing user")

        # Verify error
        open_start_page.verify_sign_in_error()
        self.log.info("Error was verified")

    def test_incorrect_login(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Fill incorrect login, correct password
        - Click Sign in button
        - Verify error
        """

        # Login as a user
        open_start_page.sing_in("incorrectuser", "nicewarthogpass")
        self.log.info("Logged in as non-existing user")

        # Verify error
        open_start_page.verify_sign_in_error()
        self.log.info("Error was verified")

    def test_incorrect_password(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Fill correct login, incorrect password
        - Click Sign in button
        - Verify error
        """

        # Login as a user
        open_start_page.sing_in("nicewarthog", "incorrectpass")
        self.log.info("Logged in as non-existing user")

        # Verify error
        open_start_page.verify_sign_in_error()
        self.log.info("Error was verified")

    def test_correct_log_in(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Fill correct login, fill correct password
        - Click Sign In button
        - Verify successfull log in account
        """

        # Login as a user
        open_start_page.sing_in("nicewarthog", "nicewarthogpass")
        self.log.info("Logged in with correct login and password")

        # Verify success
        open_start_page.verify_sign_in_success()
        self.log.info("Account name was verified, Log In was successfully")

    def test_log_in_with_enter_key(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Fill correct login, fill correct password
        - Press Enter on keyboard
        - Verify successfull log in account
        """

        # Login as a user with Enter key
        open_start_page.sing_in_with_enter("nicewarthog", "nicewarthogpass")
        self.log.info("Logged in with correct login and password")

        # Verify success
        open_start_page.verify_sign_in_success()
        self.log.info("Account name was verified, Log In was successfully")

# pytest test_start_page.py
