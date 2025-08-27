import allure
import pytest

from tests.base_test import BaseTest


@allure.epic("")
@allure.feature("")
class TestGrpc(BaseTest):

    @pytest.mark.regression
    @allure.id("011")
    @allure.title("011. ")
    @allure.description("")
    @allure.tag("Smoke", "Functional", "Positive")
    def test_create_(self):
        services = self.grpc_client.get_all_services_names()
        srv = self.grpc_client.get_service_by_name(service_name=services[0])
        pass

    @pytest.mark.regression
    @allure.id("012")
    @allure.title("012. ")
    @allure.description("")
    @allure.tag("Functional", "Positive")
    def test_get_(self):
        pass
