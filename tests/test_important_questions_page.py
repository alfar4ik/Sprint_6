import allure
import pytest
from pages.important_questions_page import ImportantQuestionsPage, ImportantQuestionsLocators, ExpectedTexts




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
    @allure.title("Тест кликабельности вопросов и соответствия текста ответов в разделе 'Важные вопросы'")
    @allure.description("Проверяем, что при клике на каждый вопрос в разделе отображается соответствующий текст ответа")
    def test_click_on_question(self, driver_init, question_locator, expected_text):
        driver_init.get("https://qa-scooter.praktikum-services.ru")
        important_questions_tab = ImportantQuestionsPage(driver_init)
        is_text_present = important_questions_tab.click_important_question_and_verify_text(question_locator, expected_text)
        assert is_text_present, f"Ожидаемый текст '{expected_text}' не был найден после клика на вопрос."





