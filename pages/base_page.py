from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver_init):
        self.driver = driver_init

    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator), message=f"Не дождались {locator}")




    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def open_url(self, url):
        return self.driver.get(url)

    def wait_for_element_to_be_clickable(self, locator, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент {locator} не стал кликабельным в течение {timeout} секунд"
        )

    def click_if_element_clickable(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
            return True
        except TimeoutException:
            print(f"Элемент с локатором {locator} не стал кликабельным в течение {timeout} секунд.")
            return False


    def is_element_present(self, by, value):
        try:
            self.driver.find_element(by, value)
            return True
        except NoSuchElementException:
            return False

    def click_question_and_verify_text(self, question_locator, expected_text):
        self.scroll_to_element(question_locator)
        self.wait_for_element_to_be_clickable(question_locator)
        self.find_element(question_locator).click()
        return self.is_element_present(By.XPATH, f"//*[contains(text(), '{expected_text}')]")





