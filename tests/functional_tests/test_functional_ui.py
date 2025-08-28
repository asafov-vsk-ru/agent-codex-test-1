import pytest
import allure

from core.ui.pages.vsk_clients_main_page import VskMainPage
from tests.base_test import BaseTest


@allure.epic("Main page")
@allure.feature("Main page - open page")
class TestMainPage(BaseTest):

    @pytest.mark.regression
    @allure.id("041")
    @allure.title("041. Open main page")
    @allure.description("This test open main web page")
    @allure.tag("Smoke", "Functional", "Positive")
    def test_main_page(self):
        main_page = VskMainPage(self.browser.new_page())
        main_page.open()
