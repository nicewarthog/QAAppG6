import logging
from time import sleep

import pytest

from pages.utils import User, random_str


class TestChat:
    log = logging.getLogger("[CreatePostPage]")

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

    def test_chat_message(self, open_hello_page):
        """
        Pre-conditions:
        - Sign Up/Sign In as the user
        - Navigate to Chat
        Steps:
        - Send chat message 1
        - Verify the message 1 sent
        - Send chat message 2
        - Verify two messages
        """

        # Open Chat
        chat = open_hello_page.header_after_sign_in.open_chat()

        # Send message_1
        message_1 = random_str(20)
        chat.send_message(message_1)
        self.log.info("Message 1 has sent")

        # Verify message 1
        chat.verify_messages([message_1])
        self.log.info("Message 1 has displayed")

        # Send message_2
        message_2 = random_str(30)
        chat.send_message(message_2)
        self.log.info("Message 2 has sent")

        # Verify two messages
        chat.verify_messages([message_1, message_2])
        self.log.info("Messages 1 and 2 has displayed")
        sleep(3)
