

from pages.base_page import BasePage
from pages.order_page import OrderPageHelper, OrderPageLocators
from conftest import driver_init

class TestRedirectionPage:

    def test_click_scooter_logo(self, driver_init):
        BasePage(driver_init).open_url("https://qa-scooter.praktikum-services.ru")
        order_page = OrderPageHelper(driver_init)
        order_page.click_scooter_logo()
        assert order_page.is_scooter_logo_clickable(), "Логотип самоката не кликабелен"

    def test_yandex_logo_redirection(self, driver_init):
        BasePage(driver_init).open_url("https://qa-scooter.praktikum-services.ru")
        order_page = OrderPageHelper(driver_init)
        current_url = order_page.click_yandex_logo()
        expected_url = OrderPageLocators.CHECK_YANDER_URL
        assert current_url == expected_url, f"Перенаправление на Яндекс не работает, текущий URL: {current_url}"




