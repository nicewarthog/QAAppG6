import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import User


@pytest.fixture(scope="function")
def open_start_page():
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
def random_user():
    user = User()
    user.sign_up_random_user_data()
    return user
