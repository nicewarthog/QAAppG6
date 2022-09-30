import datetime
import logging
import random
import string
from time import sleep


def random_num():
    """Generate random number"""
    return str(random.randint(111111, 999999))


def random_str(length=5):
    """Generate random string"""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def wait_until_ok(timeout=5, period=0.5):
    """Reties until OK"""

    log = logging.getLogger("[WaitUntilOk]")

    def decorator(original_function):
        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    if datetime.datetime.now() > end_time:
                        log.error(f"Catch: {err}")
                        raise err
                    sleep(period)

        return wrapper

    return decorator


# USERS
class User:

    def __init__(self, login="", email="", password=""):
        self.login = login
        self.email = email
        self.password = password

    def sign_up_random_user_data(self, login="", email="", password=""):
        """Fill user with sample data and values if provided"""
        user = random_str()
        # якщо логін порожній (not login), тоді заповни значенням з f"", якщо не порожній (else), тоді тим значенням, яке передамо
        self.login = f"{user}{random_num()}" if not login else login
        self.email = f"{user}{random_num()}@mail.com" if not email else email
        self.password = f"{random_str(6)}{random_num()}" if not password else password

    def sign_in_correct_user_data(self, login="", password=""):
        """Fill fields correct user data"""
        self.login = "nicewarthog" if not login else login
        self.password = "nicewarthogpass" if not password else password


class Post:
    def __init__(self, title="", body=""):
        self.title = title
        self.body = body

    def post_random_data(self, title="", body=""):
        """Fill fields using random data"""
        self.title = f"{random_str(15)}" if not title else title
        self.body = f"{random_str(50)}" if not body else body
