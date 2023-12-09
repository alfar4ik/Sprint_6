import pytest
from pages.base_page import BasePage
from pages.important_questions_page import ImportantQuestionsPage, ImportantQuestionsLocators, ExpectedTexts
from conftest import driver_init

class TestImportantQuestions:

    @pytest.mark.parametrize(
        "question_locator, expected_text",
        [
            (ImportantQuestionsLocators.COST_AND_PAYMENT_QUESTION, ExpectedTexts.COST_AND_PAYMENT),
            (ImportantQuestionsLocators.MULTIPLE_SCOOTERS_QUESTION, ExpectedTexts.MULTIPLE_SCOOTERS),
            (ImportantQuestionsLocators.RENTAL_TIME_CALCULATION_QUESTION, ExpectedTexts.RENTAL_TIME_CALCULATION),
            (ImportantQuestionsLocators.ORDER_FOR_TODAY_QUESTION, ExpectedTexts.ORDER_FOR_TODAY),
            (ImportantQuestionsLocators.EXTEND_OR_RETURN_EARLY_QUESTION, ExpectedTexts.EXTEND_OR_RETURN_EARLY),
            (ImportantQuestionsLocators.CHARGER_INCLUDED_QUESTION, ExpectedTexts.CHARGER_INCLUDED),
            (ImportantQuestionsLocators.CANCEL_ORDER_QUESTION, ExpectedTexts.CANCEL_ORDER),
            (ImportantQuestionsLocators.DELIVERY_OUTSIDE_MKAD_QUESTION, ExpectedTexts.DELIVERY_OUTSIDE_MKAD),
        ]
    )
    def test_click_on_question(self, driver_init, question_locator, expected_text):
        BasePage(driver_init).open_url("https://qa-scooter.praktikum-services.ru")
        important_questions_tab = ImportantQuestionsPage(driver_init)
        found_element = important_questions_tab.click_question_and_verify_text(question_locator, expected_text)
        assert found_element, "Ожидаемый текст не был найден после клика."





