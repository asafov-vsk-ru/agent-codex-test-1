import pytest
import allure

from tests.base_test import BaseTest


@allure.epic("E2E")
@allure.feature("E2E tests")
class TestMainPage(BaseTest):

    @pytest.mark.regression
    @allure.id("051")
    @allure.title("051. E2E test")
    @allure.description("Description for E2E test")
    @allure.tag("E2E", "Functional", "Positive")
    def test_e2e(self):
        pass
