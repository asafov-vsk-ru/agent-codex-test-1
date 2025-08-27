import re
import pytest
import allure

from playwright.sync_api import Page, expect
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
        page = self.browser.new_page()
        page.goto("https://www.stage.vsk.ru/klientam")
        assert page.title() == "ВСК"
