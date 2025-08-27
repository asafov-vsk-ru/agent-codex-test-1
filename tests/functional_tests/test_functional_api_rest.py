import allure
import pytest

from core.rest.models.user_model import User
from tests.base_test import BaseTest


@allure.epic("User service")
@allure.feature("User service - CRUD operations")
class TestUsers(BaseTest):

    @pytest.mark.regression
    @allure.id("031")
    @allure.title("031. Check is user creating")
    @allure.description("This test create user with POST method")
    @allure.tag("Smoke", "Functional", "Positive")
    def test_create_user(self):
        # user = User()
        # user.user_name = None
        # result = self.pet_store_client.user_api_methods.create_user(user)
        # assert result.message is not None, "User is not created!"
        print(self.env_config.kafka_host)
        print(self.app_config)

    @pytest.mark.regression
    @allure.id("032")
    @allure.title("032. Check is user existing")
    @allure.description("This test find user by \'username\' with GET method")
    @allure.tag("Functional", "Positive")
    def test_get_user(self):
        pass

    @pytest.mark.regression
    @allure.id("033")
    @allure.title("033. Check is user updating")
    @allure.description("This test update user with PUT method")
    @allure.tag("Functional", "Positive")
    def test_update_user(self):
        pass

    @pytest.mark.regression
    @allure.id("034")
    @allure.title("034. Check is user deleting")
    @allure.description("This test remove existing user with DELETE method")
    @allure.tag("Functional", "Positive")
    def test_delete_user(self):
        pass
