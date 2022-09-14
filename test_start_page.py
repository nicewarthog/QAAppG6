from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:

    def test_incorrect_login(self):
        """
        Steps:
        - Create driver
        - Open page
        - Fill login
        - Fill password
        - Click button
        - Verify error
        """
        # Create driver
        driver = webdriver.Chrome(r"\Users\nicewarthog\PycharmProjects\QAAppG6\chromedriver.exe")

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(1)

        # Fill login
        login = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login.send_keys("User11")
        sleep(1)

        # Fill password
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.send_keys("Psw11")
        sleep(1)

        # Click button
        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        sleep(1)

        # Verify error
        error_element = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_element.text == "Invalid username / pasword", f"Actual message: {error_element.text}"

        # Close driver
        driver.close()

    # def test_empty_login(self):
    #     """
    #     - Create driver
    #     - Open page
    #     - Clear login
    #     - Clear password
    #     - Click button
    #     - Verify error
    #     """

# pytest test_start_page.py
