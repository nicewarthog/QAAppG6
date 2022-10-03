import logging

from pages.utils import User


class TestHeaderBeforeSignIn:
    log = logging.getLogger("[Header]")

    # SIGN IN

    # @pytest.fixture(scope="function")
    # def log_in_as_user(self, open_start_page):
    #     self.log.info("Logged in with correct login and password")
    #     return open_start_page.header_before_sign_in.sign_in_and_verify("nicewarthog", "nicewarthogpass")

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
        empty_login = User()
        empty_login.sign_in_correct_user_data()
        open_start_page.header_before_sign_in.sign_in_and_fail(User(login="", password="nicewarthogpass"))
        self.log.info("Logged in as non-existing user")

        # Verify error
        open_start_page.header_before_sign_in.verify_sign_in_error()
        self.log.info("Login is empty")

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
        empty_password = User()
        empty_password.sign_in_correct_user_data()
        open_start_page.header_before_sign_in.sign_in_and_fail(User(login="nicewarthog", password=""))
        self.log.info("Logged in as non-existing user")

        # Verify error
        open_start_page.header_before_sign_in.verify_sign_in_error()
        self.log.info("Password is empty")

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
        incorrect_login = User()
        incorrect_login.sign_in_correct_user_data()
        open_start_page.header_before_sign_in.sign_in_and_fail(User(login="incorrectuser", password="nicewarthogpass"))
        self.log.info("Logged in as non-existing user")

        # Verify error
        open_start_page.header_before_sign_in.verify_sign_in_error()
        self.log.info("Password incorrect")

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
        incorrect_password = User()
        incorrect_password.sign_in_correct_user_data()
        open_start_page.header_before_sign_in.sign_in_and_fail(User(login="nicewarthog", password="incorrectpass"))
        self.log.info("Logged in as non-existing user")

        # Verify error
        open_start_page.header_before_sign_in.verify_sign_in_error()
        self.log.info("Password is incorrect")

    def test_correct_log_in(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        - Fill correct login, fill correct password
        - Click Sign In button
        Steps:
        - Verify successfull log in account
        """

        # Log in as user
        correct_user = User()  # логін і пароль коректного юзера задані в pages.utils - User().sign_in_correct_user_data
        correct_user.sign_in_correct_user_data()
        open_start_page.header_before_sign_in.sign_in_and_verify(correct_user)

        # open_start_page.header_before_sign_in.click_sign_in_and_verify()
        # from time import sleep
        # sleep(3)

        # Verify success
        open_start_page.header_after_sign_in.verify_sign_in_success()
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

        # Log in as user
        correct_user = User()
        correct_user.sign_in_correct_user_data()
        open_start_page.header_before_sign_in.sign_in_with_enter(correct_user)

        # Verify success
        open_start_page.header_after_sign_in.verify_sign_in_success()
        self.log.info("Account name was verified, Log In was successfully")
