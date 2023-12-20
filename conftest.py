import pytest
from selenium import webdriver



@pytest.fixture(scope="session")
def driver_init(request):
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

