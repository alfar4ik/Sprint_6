import allure
from pages.order_page import OrderPageHelper, ConfigUrl


class TestRedirectionPage:

    @allure.title("Проверка перехода на страницу заказа самоката")
    @allure.description("Проверяем кликабельность лого самоката и переход на страницу")
    def test_click_scooter_logo(self, driver_init):
        driver_init.get("https://qa-scooter.praktikum-services.ru")
        order_page = OrderPageHelper(driver_init)
        order_page.click_scooter_logo()
        assert order_page.is_scooter_logo_clickable(), "Логотип самоката не кликабелен"

    @allure.title("Проверка перехода на сайт Яндекса")
    @allure.description("Проверяем кликабельность лого яндекса и переход на страницу")
    def test_yandex_logo_redirection(self, driver_init):
        driver_init.get("https://qa-scooter.praktikum-services.ru")
        order_page = OrderPageHelper(driver_init)
        current_url = order_page.click_yandex_logo()
        expected_url = ConfigUrl.get_yandex_dzen_url()
        assert current_url == expected_url, f"Перенаправление на Яндекс не работает, текущий URL: {current_url}"




