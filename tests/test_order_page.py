import pytest
import allure
from pages.order_page import OrderPageHelper, OrderPageLocators
from conftest import driver_init


class TestOrderPage:

    @pytest.mark.parametrize(
        "button_locator, name, last_name, address, phone, date_of_delivery_locator, amount_of_time_locator, scooter_color_locator",
        [
            (OrderPageLocators.ORDER_BUTTON, "Владимир", "Альфаро", "Васильковская 22", "+73058428248",
             OrderPageLocators.DATE_OF_DELIVERY,
             OrderPageLocators.AMOUNT_OF_TIME,
             OrderPageLocators.SCOOTER_COLOR),

            (OrderPageLocators.ORDER_BUTTON_BODY, "Елена", "Иванова", "Ленина 15", "+71234567890",
             OrderPageLocators.DATE_OF_DELIVERY,
             OrderPageLocators.AMOUNT_OF_TIME,
             OrderPageLocators.SCOOTER_COLOR),
        ]
    )
    @allure.title("Оформляем заказ и проверяем создан ли он")
    @allure.description("Заполняем все поля поочередно и проверяем, что все проходит валидацию")
    def test_fill_out_customer_info(self, driver_init, button_locator, name, last_name, address, phone,
                                    date_of_delivery_locator, amount_of_time_locator, scooter_color_locator):
        driver_init.get("https://qa-scooter.praktikum-services.ru")
        order_page = OrderPageHelper(driver_init)
        order_page.click_button_by_locator(button_locator)
        order_page.fill_out_name(name)
        order_page.fill_out_last_name(last_name)
        order_page.fill_out_delivery_address(address)
        order_page.select_metro_station()
        order_page.select_named_metro_station()
        order_page.fill_out_phone(phone)
        order_page.click_next_button()
        order_page.click_agree_cookie()
        order_page.click_when_to_delivery_button()
        order_page.click_date_of_delivery(date_of_delivery_locator)
        order_page.click_rental_period()
        order_page.click_amount_of_time(amount_of_time_locator)
        order_page.click_scooter_color(scooter_color_locator)
        order_page.click_comments_for_courier("call me")
        order_page.click_final_order_button()
        order_page.click_agree_with_order_button()
        assert order_page.check_status(), "Заказ не был создан"
