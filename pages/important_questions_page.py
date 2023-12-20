import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ImportantQuestionsLocators:
    COST_AND_PAYMENT_QUESTION = (By.XPATH, "//div[@id='accordion__heading-0']")
    MULTIPLE_SCOOTERS_QUESTION = (By.XPATH, "//div[@id='accordion__heading-1']")
    RENTAL_TIME_CALCULATION_QUESTION = (By.XPATH, "//div[@id='accordion__heading-2']")
    ORDER_FOR_TODAY_QUESTION = (By.XPATH, "//div[@id='accordion__heading-3']")
    EXTEND_OR_RETURN_EARLY_QUESTION = (By.XPATH, "//div[@id='accordion__heading-4']")
    CHARGER_INCLUDED_QUESTION = (By.XPATH, "//div[@id='accordion__heading-5']")
    CANCEL_ORDER_QUESTION = (By.XPATH, "//div[@id='accordion__heading-6']")
    DELIVERY_OUTSIDE_MKAD_QUESTION = (By.XPATH, "//div[@id='accordion__heading-7']")
    QUESTION_LOCATOR_TEMPLATE = "//div[@id='accordion__heading-{}']"
    ANSWER_TEXT_TEMPLATE = "//*[contains(text(), '{}')]"


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

    @allure.step("Проверка наличия элемента на странице 'Важные вопросы'")
    def __check_page(self):
        self.scroll_to_element(ImportantQuestionsLocators.COST_AND_PAYMENT_QUESTION)

    @allure.step("Клик по вопросу и проверка соответствующего текста ответа")
    def click_important_question_and_verify_text(self, question_locator, expected_text):
        self.scroll_to_element(question_locator)
        self.wait_for_element_to_be_clickable(question_locator)
        self.find_element(question_locator).click()
        answer_locator = (By.XPATH, ImportantQuestionsLocators.ANSWER_TEXT_TEMPLATE.format(expected_text))
        return self.is_element_present(*answer_locator)







