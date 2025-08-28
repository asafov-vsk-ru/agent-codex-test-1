import pytest
import allure

from tests.base_test import BaseTest


@allure.epic("Clients")
@allure.feature("Clients search")
class TestClientsSearch(BaseTest):

    @pytest.mark.regression
    @allure.id("052")
    @allure.title("052. Search clients and check results")
    @allure.description("Opens clients page, fills search form and verifies that search returns at least one record")
    @allure.tag("E2E", "UI", "Positive")
    def test_search_clients(self):
        page = self.browser.new_page()
        url = "https://stage-frontend-arm-ui.apps.stg-okd-lan.vsk.ru/clients"
        page.goto(url)
        if "clients" not in page.url():
            page.wait_for_url("**/clients", timeout=120000)
        page.get_by_label("ФИО").fill("Тест Тестов")
        page.get_by_label("Год рождения").fill("2000")
        page.get_by_placeholder("Выберите статус").click()
        page.get_by_role("option").first().click()
        page.get_by_role("button", name="Поиск").click()
        rows = page.locator("tbody tr[tuitr]")
        assert rows.count() > 0
