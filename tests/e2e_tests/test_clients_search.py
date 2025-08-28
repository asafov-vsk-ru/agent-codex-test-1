import pytest
import allure

from tests.base_test import BaseTest
from core.ui.pages.clients_page import ClientsPage


@allure.epic("Clients")
@allure.feature("Clients search")
class TestClientsSearch(BaseTest):

    @pytest.mark.regression
    @allure.id("052")
    @allure.title("052. Search clients and check results")
    @allure.description("Opens clients page, fills search form and verifies that search returns at least one record")
    @allure.tag("E2E", "UI", "Positive")
    def test_search_clients(self):
        clients_page = ClientsPage(self.browser.new_page())
        clients_page.open()
        clients_page.search_clients("Тест Тестов", "2000")
        clients_page.should_have_results()
