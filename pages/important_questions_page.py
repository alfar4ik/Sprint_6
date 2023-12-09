import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from conftest import driver_init


class ImportantQuestionsLocators:
    COST_AND_PAYMENT_QUESTION = (By.XPATH, "//div[@id='accordion__heading-0']")
    MULTIPLE_SCOOTERS_QUESTION = (By.XPATH, "//div[@id='accordion__heading-1']")
    RENTAL_TIME_CALCULATION_QUESTION = (By.XPATH, "//div[@id='accordion__heading-2']")
    ORDER_FOR_TODAY_QUESTION = (By.XPATH, "//div[@id='accordion__heading-3']")
    EXTEND_OR_RETURN_EARLY_QUESTION = (By.XPATH, "//div[@id='accordion__heading-4']")
    CHARGER_INCLUDED_QUESTION = (By.XPATH, "//div[@id='accordion__heading-5']")
    CANCEL_ORDER_QUESTION = (By.XPATH, "//div[@id='accordion__heading-6']")
    DELIVERY_OUTSIDE_MKAD_QUESTION = (By.XPATH, "//div[@id='accordion__heading-7']")


class ExpectedTexts:
    COST_AND_PAYMENT = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    MULTIPLE_SCOOTERS = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    RENTAL_TIME_CALCULATION = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру."
    ORDER_FOR_TODAY = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    EXTEND_OR_RETURN_EARLY = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    CHARGER_INCLUDED = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    CANCEL_ORDER = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим."
    DELIVERY_OUTSIDE_MKAD = "Да, обязательно. Всем самокатов! И Москве, и Московской области."


class ImportantQuestionsPage(BasePage):
    def __init__(self, driver_init):
        super().__init__(driver_init)
        self.__check_page()


    def __check_page(self):
        self.scroll_to_element(ImportantQuestionsLocators.COST_AND_PAYMENT_QUESTION)

    @allure.title("Проверка вопроса о стоимости и оплате")
    @allure.description("Проверка отображения и содержания вопроса о стоимости и оплате")
    @allure.step("Нажать на вопрос 'Стоимость и оплата'")
    def click_cost_and_payment_question(self):
        self.scroll_to_element(ImportantQuestionsLocators.COST_AND_PAYMENT_QUESTION)
        self.wait_for_element_to_be_clickable(ImportantQuestionsLocators.COST_AND_PAYMENT_QUESTION)
        self.find_element(ImportantQuestionsLocators.COST_AND_PAYMENT_QUESTION).click()
        expected_text_xpath = f"//*[contains(text(), '{ExpectedTexts.COST_AND_PAYMENT}')]"
        return self.is_element_present(By.XPATH, expected_text_xpath)

    @allure.title("Проверка вопроса о возможности аренды нескольких самокатов")
    @allure.description("Проверка отображения и содержания вопроса о возможности аренды нескольких самокатов")
    @allure.step("Нажать на вопрос 'Возможно ли арендовать несколько самокатов?'")
    def click_multipe_scooters_question(self):
        self.scroll_to_element(ImportantQuestionsLocators.MULTIPLE_SCOOTERS_QUESTION)
        self.wait_for_element_to_be_clickable(ImportantQuestionsLocators.MULTIPLE_SCOOTERS_QUESTION)
        self.find_element(ImportantQuestionsLocators.MULTIPLE_SCOOTERS_QUESTION).click()
        expected_text_xpath = f"//*[contains(text(), '{ExpectedTexts.MULTIPLE_SCOOTERS}')]"
        return self.driver.find_element(By.XPATH, expected_text_xpath)

    @allure.title("Проверка вопроса о расчете времени аренды")
    @allure.description("Проверка отображения и содержания вопроса о расчете времени аренды")
    @allure.step("Нажать на вопрос 'Расчет времени аренды'")
    def click_rental_time_calculation_question(self):
        self.scroll_to_element(ImportantQuestionsLocators.RENTAL_TIME_CALCULATION_QUESTION)
        self.wait_for_element_to_be_clickable(ImportantQuestionsLocators.RENTAL_TIME_CALCULATION_QUESTION)
        self.find_element(ImportantQuestionsLocators.RENTAL_TIME_CALCULATION_QUESTION).click()
        expected_text_xpath = f"//*[contains(text(), '{ExpectedTexts.RENTAL_TIME_CALCULATION}')]"
        return self.driver.find_element(By.XPATH, expected_text_xpath)

    @allure.title("Проверка вопроса о заказе на сегодня")
    @allure.description("Проверка отображения и содержания вопроса о заказе на сегодня")
    @allure.step("Нажать на вопрос 'Заказ на сегодня'")
    def click_order_for_today_question(self):
        self.scroll_to_element(ImportantQuestionsLocators.ORDER_FOR_TODAY_QUESTION)
        self.wait_for_element_to_be_clickable(ImportantQuestionsLocators.ORDER_FOR_TODAY_QUESTION)
        self.find_element(ImportantQuestionsLocators.ORDER_FOR_TODAY_QUESTION).click()
        expected_text_xpath = f"//*[contains(text(), '{ExpectedTexts.ORDER_FOR_TODAY}')]"
        return self.driver.find_element(By.XPATH, expected_text_xpath)

    @allure.title("Проверка вопроса о продлении или завершении аренды")
    @allure.description("Проверка отображения и содержания вопроса о продлении или завершении аренды")
    @allure.step("Нажать на вопрос 'Продление или завершение аренды'")
    def click_extend_or_return_early_question(self):
        self.scroll_to_element(ImportantQuestionsLocators.EXTEND_OR_RETURN_EARLY_QUESTION)
        self.wait_for_element_to_be_clickable(ImportantQuestionsLocators.EXTEND_OR_RETURN_EARLY_QUESTION)
        self.find_element(ImportantQuestionsLocators.EXTEND_OR_RETURN_EARLY_QUESTION).click()
        expected_text_xpath = f"//*[contains(text(), '{ExpectedTexts.EXTEND_OR_RETURN_EARLY}')]"
        return self.driver.find_element(By.XPATH, expected_text_xpath)

    @allure.title("Проверка вопроса о наличии зарядки ")
    @allure.description("Проверка отображения и содержания вопроса о наличии зарядки ")
    @allure.step("Нажать на вопрос 'Наличие зарядки'")
    def click_charger_included_question(self):
        self.scroll_to_element(ImportantQuestionsLocators.CHARGER_INCLUDED_QUESTION)
        self.wait_for_element_to_be_clickable(ImportantQuestionsLocators.CHARGER_INCLUDED_QUESTION)
        self.find_element(ImportantQuestionsLocators.CHARGER_INCLUDED_QUESTION).click()
        expected_text_xpath = f"//*[contains(text(), '{ExpectedTexts.CHARGER_INCLUDED}')]"
        return self.driver.find_element(By.XPATH, expected_text_xpath)

    @allure.title("Проверка вопроса об отмене заказа")
    @allure.description("Проверка отображения и содержания вопроса об отмене заказа")
    @allure.step("Нажать на вопрос 'Отмена заказа'")
    def click_cancel_order_question(self):
        self.scroll_to_element(ImportantQuestionsLocators.CANCEL_ORDER_QUESTION)
        self.wait_for_element_to_be_clickable(ImportantQuestionsLocators.CANCEL_ORDER_QUESTION)
        self.find_element(ImportantQuestionsLocators.CANCEL_ORDER_QUESTION).click()
        expected_text_xpath = f"//*[contains(text(), '{ExpectedTexts.CANCEL_ORDER}')]"
        return self.driver.find_element(By.XPATH, expected_text_xpath)

    @allure.title("Проверка вопроса о доставке за пределы МКАД")
    @allure.description("Проверка отображения и содержания вопроса о доставке за пределы МКАД")
    @allure.step("Нажать на вопрос 'Доставка за пределы МКАД'")
    def click_delivery_outside_mkad_question(self):
        self.scroll_to_element(ImportantQuestionsLocators.DELIVERY_OUTSIDE_MKAD_QUESTION)
        self.wait_for_element_to_be_clickable(ImportantQuestionsLocators.DELIVERY_OUTSIDE_MKAD_QUESTION)
        self.find_element(ImportantQuestionsLocators.DELIVERY_OUTSIDE_MKAD_QUESTION).click()
        expected_text_xpath = f"//*[contains(text(), '{ExpectedTexts.DELIVERY_OUTSIDE_MKAD}')]"
        return self.driver.find_element(By.XPATH, expected_text_xpath)






