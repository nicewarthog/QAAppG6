import pyautogui
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver=driver, timeout=5)  # у параметрах віддаємо драйвер і граничний таймаут

    def wait_until_displayed(self, xpath):
        """Wait until element is displayed"""
        # додаємо метод expected_conditions + умову, що елемент буде видимий + локатор - тупл з двох параметрів (тип локатора: By,
        # і сам локатор: xpath
        return self.waiter.until(method=expected_conditions.visibility_of_element_located((By.XPATH, xpath)),
                                 message=f"XPATH '{xpath}' is not displayed or cannot be found")

    def wait_until_clickable(self, xpath):
        """Wait until element is clicable"""
        # додаємо метод expected_conditions + умову + тупл з двох параметрів - тип локатора: By, і сам локтор: xpath
        return self.waiter.until(method=expected_conditions.element_to_be_clickable((By.XPATH, xpath)),
                                 message=f"XPATH '{xpath}' is not clickable or cannot be found")  # можна додати месседж

    def is_exist(self, xpath, by=By.XPATH):
        """Check that element exists"""
        try:
            self.driver.find_element(by=by, value=xpath)
            return True
        except selenium.common.exceptions.NoSuchElementException:
            return False

    def fill_field(self, xpath, value):
        """Clear and fill field"""
        element = self.wait_until_clickable(xpath=xpath)  # пошук елемента з вейтером
        # element = self.driver.find_element(by=By.XPATH, value=xpath)  # пошук елемента без вейтера
        element.clear()
        element.send_keys(value)

    def click(self, xpath):
        """Find and click button"""
        self.wait_until_clickable(xpath=xpath).click()

    def press_enter(self):
        """Press Enter key on keyboard"""
        pyautogui.press('Enter')

    def get_element_text(self, xpath):
        """Find element and get text"""
        # Verify error
        element = self.wait_until_displayed(xpath=xpath)
        return element.text
