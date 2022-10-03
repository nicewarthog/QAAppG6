import logging

import pytest

from pages.utils import User


class TestHeaderAfterSignIn:
    log = logging.getLogger("[Header]")

    @pytest.fixture(scope="function")
    def primary_user(self, open_start_page):
        correct_user = User()
        correct_user.sign_in_correct_user_data()
        open_start_page.header_before_sign_in.sign_in_and_verify(correct_user)
        return correct_user

    # SIGN OUT

    def test_sign_out(self, open_start_page, primary_user):
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

    def test_open_profile_page(self, open_start_page, primary_user):
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
