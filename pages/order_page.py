import allure
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class OrderPageLocators:
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    INPUT_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    INPUT_LAST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    DELIVERY_ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[contains(@class, 'select-search__input')]")
    NAMED_METRO_STATION_INPUT = (By.XPATH, "//div[contains(text(), 'Черкизовская')]")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(),'Далее')]")
    ORDER_BUTTON_BODY = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM')]")
    COOCKIE = (By.XPATH, "//button[@class='App_CookieButton__3cvqF']")
    WHEN_TO_DELIVERY_SCOOTER = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_OF_DELIVERY = (By.XPATH, "//div[@aria-label='Choose среда, 29-е ноября 2023 г.']")
    RENTAL_PERIOD = (By.XPATH, "//div[contains(text(),'* Срок аренды')]")
    AMOUNT_OF_TIME = (By.XPATH, "//div[text()='четверо суток']")
    SCOOTER_COLOR = (By.XPATH, "//label[normalize-space()='серая безысходность']")
    COMMENT_FOR_COURIER = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    FINAL_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")
    AGREE_WITH_ORDER = (By.XPATH, "//button[text()='Да']")
    CHECK_STATUS = (By.XPATH, "//*[contains(text(),'Заказ оформлен')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex__3TSOI')]")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter__3lsAR')]")
    CHECK_IF_CLICKABLE_SCOOTER = (By.XPATH, "//button[@class='Button_Button__ra12g']")

class ConfigUrl:
    @staticmethod
    def get_yandex_dzen_url():
        return "https://dzen.ru/?yredirect=true"

class OrderPageHelper(BasePage):
    def __init__(self, driver_init):
        super().__init__(driver_init)
        self.__check_page()

    @allure.step("Проверка наличия кнопки 'Заказать' на странице")
    def __check_page(self):
        self.find_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Выбор и клик по одной из кнопок 'Заказать'")
    def click_button_by_locator(self, button_locator):
        if button_locator == OrderPageLocators.ORDER_BUTTON:
            self.click_order_button()
        elif button_locator == OrderPageLocators.ORDER_BUTTON_BODY:
            self.click_order_button_body()
        else:
            raise ValueError("Неправильный локатор кнопки")

    @allure.step("Нажать на верхнюю кнопку 'Заказать'")
    def click_order_button(self):
        self.find_element(OrderPageLocators.ORDER_BUTTON).click()

    @allure.step("Нажать на нижнюю кнопку 'Заказать'")
    def click_order_button_body(self):
        self.scroll_to_element(OrderPageLocators.ORDER_BUTTON_BODY)
        self.find_element(OrderPageLocators.ORDER_BUTTON_BODY).click()

    @allure.step("Заполнение поля 'Имя'")
    def fill_out_name(self, name):
        name_field = self.find_element(OrderPageLocators.INPUT_NAME_FIELD)
        name_field.clear()
        name_field.send_keys(name)

    @allure.step("Заполнение поля  'Фамилия'")
    def fill_out_last_name(self, last_name):
        last_name_field = self.find_element(OrderPageLocators.INPUT_LAST_NAME_FIELD)
        last_name_field.clear()
        last_name_field.send_keys(last_name)

    @allure.step("Заполнение поля 'Адрес доставки'")
    def fill_out_delivery_address(self, address):
        delivery_address_field = self.find_element(OrderPageLocators.DELIVERY_ADDRESS_FIELD)
        delivery_address_field.clear()
        delivery_address_field.send_keys(address)

    @allure.step("Открытие списка станций метро")
    def select_metro_station(self):
        self.find_element(OrderPageLocators.METRO_STATION_INPUT).click()

    @allure.step("Выбор станции метро")
    def select_named_metro_station(self):
        self.find_element(OrderPageLocators.NAMED_METRO_STATION_INPUT).click()

    @allure.step("Заполнение поля 'Телефон'")
    def fill_out_phone(self, phone):
        phone_number_field = self.find_element(OrderPageLocators.PHONE_FIELD)
        phone_number_field.clear()
        phone_number_field.send_keys(phone)

    @allure.step("Переход к следующему шагу заказа")
    def click_next_button(self):
        self.find_element(OrderPageLocators.NEXT_BUTTON).click()

    @allure.step("Принятие куки на странице")
    def click_agree_cookie(self):
        try:
            agree_cookie_button = self.find_element(OrderPageLocators.COOCKIE, time=2)
            agree_cookie_button.click()
        except (TimeoutException, NoSuchElementException):

            print("Кнопка согласия на cookies не найдена. Продолжаем тест.")

    @allure.step("Выбор времени доставки самоката")
    def click_when_to_delivery_button(self):
        self.find_element(OrderPageLocators.WHEN_TO_DELIVERY_SCOOTER).click()

    @allure.step("Выбор даты доставки самоката")
    def click_date_of_delivery(self, date_of_delivery_locator):
        self.find_element(date_of_delivery_locator).click()

    @allure.step("Выбор срока аренды самоката")
    def click_rental_period(self):
        self.find_element(OrderPageLocators.RENTAL_PERIOD).click()

    @allure.step("Выбор количества дней аренды")
    def click_amount_of_time(self, amount_of_time_locator):
        self.find_element(amount_of_time_locator).click()

    @allure.step("Выбрать цвет самоката")
    def click_scooter_color(self, scooter_color_locator):
        self.find_element(scooter_color_locator).click()

    @allure.step("Ввод комментария для курьера")
    def click_comments_for_courier(self, comment):
        comment_field = self.find_element(OrderPageLocators.COMMENT_FOR_COURIER)
        comment_field.clear()
        comment_field.send_keys(comment)

    @allure.step("Финальное подтверждение заказа")
    def click_final_order_button(self):
        self.find_element(OrderPageLocators.FINAL_ORDER_BUTTON).click()

    @allure.step("Подтверждение данных заказа")
    def click_agree_with_order_button(self):
        self.find_element(OrderPageLocators.AGREE_WITH_ORDER).click()

    @allure.step("Проверка успешности оформления заказа")
    def check_status(self):
        try:
            self.find_element(OrderPageLocators.CHECK_STATUS)
            return True
        except NoSuchElementException:
            return False


    @allure.step("Переход на главную страницу Яндекса через логотип")
    def click_yandex_logo(self):
        self.find_element(OrderPageLocators.YANDEX_LOGO).click()
        WebDriverWait(self.driver, 10).until(lambda driver: len(driver.window_handles) > 1)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        WebDriverWait(self.driver, 10).until(EC.url_to_be(ConfigUrl.get_yandex_dzen_url()))

        return self.driver.current_url

    @allure.step("Переход на главную страницу Самоката через логотип")
    def click_scooter_logo(self):
        return self.click_if_element_clickable(OrderPageLocators.SCOOTER_LOGO)

    @allure.step("Проверка кликабельности логотипа 'Самокат'")
    def is_scooter_logo_clickable(self):
        return self.click_if_element_clickable(OrderPageLocators.CHECK_IF_CLICKABLE_SCOOTER)









