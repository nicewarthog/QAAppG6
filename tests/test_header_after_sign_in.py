import logging

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage


class TestHeaderAfterSignIn:
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

    @pytest.fixture(scope="function")
    def log_in_as_user(self, open_start_page):
        self.log.info("Logged in with correct login and password")
        return open_start_page.header_before_sign_in.sign_in_and_verify("nicewarthog", "nicewarthogpass")

    # SIGN OUT

    def test_sign_out(self, open_start_page, log_in_as_user):
        """
        Fixture:
        - Log In as user
        Steps:
        - Sign Out
        - Verify successfull sign out
        """

        # Sign Out
        open_start_page.header_after_sign_in.sign_out_click()

        # Verify account name is not displayed and Sign In button
        header_before_sign_in = open_start_page.header_before_sign_in_return()
        header_before_sign_in.verify_sign_out_success()
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
        profile_page = open_start_page.header_after_sign_in.open_my_profile_page()

        # Verify success
        profile_page.verify_open_profile_page(login="nicewarthog")
        self.log.info(f"Profile name is verified")
