import pytest
from selenium import webdriver



@pytest.fixture(scope="session")
def driver_init(request):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

