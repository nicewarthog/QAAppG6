import pyautogui
import selenium
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def is_exist(self, xpath, by=By.XPATH):
        """Check that element exists"""
        try:
            self.driver.find_element(by=by, value=xpath)
            return True
        except selenium.common.exceptions.NoSuchElementException:
            return False

    def fill_field(self, xpath, value):
        """Clear and fill field"""
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        element.clear()
        element.send_keys(value)

    def click(self, xpath):
        """Find and click button"""
        self.driver.find_element(by=By.XPATH, value=xpath).click()

    def press_enter(self):
        """Press Enter key on keyboard"""
        pyautogui.press('Enter')
