import logging

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage


class TestHeader:
    log = logging.getLogger("[Header]")

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

    # SIGN IN/OUT

    @pytest.fixture(scope="function")
    def log_in_as_user(self, open_start_page):
        self.log.info("Logged in with correct login and password")
        return open_start_page.header.sign_in_and_verify("nicewarthog", "nicewarthogpass")

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
        open_start_page.header.sign_in_and_fail("", "nicewarthogpass")
        self.log.info("Logged in as non-existing user")

        # Verify error
        open_start_page.header.verify_sign_in_error()
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
        open_start_page.header.sign_in_and_fail("nicewarthog", "")
        self.log.info("Logged in as non-existing user")

        # Verify error
        open_start_page.header.verify_sign_in_error()
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
        open_start_page.header.sign_in_and_fail("incorrectuser", "nicewarthogpass")
        self.log.info("Logged in as non-existing user")

        # Verify error
        open_start_page.header.verify_sign_in_error()
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
        open_start_page.header.sign_in_and_fail("nicewarthog", "incorrectpass")
        self.log.info("Logged in as non-existing user")

        # Verify error
        open_start_page.header.verify_sign_in_error()
        self.log.info("Error was verified")

    def test_correct_log_in(self, open_start_page, log_in_as_user):
        """
        Fixture:
        - Create driver, open page
        - Fill correct login, fill correct password
        - Click Sign In button
        Steps:
        - Verify successfull log in account
        """

        # Verify success
        open_start_page.header.verify_sign_in_success()
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
        open_start_page.header.sign_in_with_enter("nicewarthog", "nicewarthogpass")
        self.log.info("Logged in with correct login and password")

        # Verify success
        open_start_page.header.verify_sign_in_success()
        self.log.info("Account name was verified, Log In was successfully")

    def test_sign_out(self, open_start_page, log_in_as_user):
        """
        Fixture:
        - Log In as user
        Steps:
        - Sign Out
        - Verify successfull sign out
        """

        # Sign Out
        open_start_page.header.sign_out_click()

        # Verify account name is not displayed and Sign In button
        open_start_page.header.verify_sign_out_success()
        self.log.info("Sign In button was verified, Log In was successfully")

    # MY PROFILE

    def test_open_profile_page(self, open_start_page, log_in_as_user):
        """
           Fixture:
           - Log In as user
           Steps:
           - Click on My Profile button
           - Verify the Profile Page is opened
           """

        # Click Profile button
        profile_page = open_start_page.header.open_my_profile_page()

        # Verify success
        profile_page.verify_open_profile_page(login="nicewarthog")
        self.log.info(f"Profile name is verified")
