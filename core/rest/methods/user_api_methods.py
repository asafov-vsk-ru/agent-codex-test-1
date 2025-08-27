import json
import requests
import allure

from typing import List
from core.rest.config.api_endpoints import ApiEndpoints
from core.rest.config.content_type import ContentType
from core.rest.methods.api_methods import ApiMethods
from core.rest.models.api_response_model import ApiResponse
from core.rest.models.user_model import User


class UserApiMethods(ApiMethods):

    def __init__(self, host: str):
        super().__init__(host)

    # POST /user/createWithList
    @allure.step("Create users with list")
    def create_users_with_list(self, body: List[User]) -> ApiResponse:
        response = self.validate_response(
            response=requests.post(
                url=ApiEndpoints.CREATE_USERS_WITH_LIST.format(host=self.host),
                headers={"accept": ContentType.JSON, "Content-Type": ContentType.JSON},
                data=json.dumps(f"{body}"),
            )
        )
        return ApiResponse.model_validate_json(response.text)

    # GET /user/{username}
    @allure.step("Get user by name")
    def get_user_by_name(self, username: str) -> ApiResponse:
        response = self.validate_response(
            response=requests.get(
                url=ApiEndpoints.GET_USER_BY_NAME.format(host=self.host, user_name=username),
            )
        )
        return ApiResponse.model_validate_json(response.text)

    # PUT /user/{username}
    @allure.step("Update user by name")
    def update_user(self, username: str, body: User) -> ApiResponse:
        response = self.validate_response(
            response=requests.put(
                url=ApiEndpoints.UPDATE_USER.format(host=self.host, user_name=username),
                headers={"accept": ContentType.JSON, "Content-Type": ContentType.JSON},
                data=f"{body.model_dump_json()}",
            )
        )
        return ApiResponse.model_validate_json(response.text)

    # DELETE /user/{username}
    @allure.step("Delete user by name")
    def delete_user(self, username: str) -> ApiResponse:
        response = self.validate_response(
            response=requests.delete(
                url=ApiEndpoints.DELETE_USER.format(host=self.host, user_name=username),
            )
        )
        return ApiResponse.model_validate_json(response.text)

    # GET /user/login
    @allure.step("Login for user")
    def login_user(self, username: str, password: str) -> ApiResponse:
        response = self.validate_response(
            response=requests.get(
                url=ApiEndpoints.LOGIN_USER.format(host=self.host),
                params={"username": username, "password": password},
            )
        )
        return ApiResponse.model_validate_json(response.text)

    # GET /user/logout
    @allure.step("Logout for user")
    def logout_user(self) -> ApiResponse:
        response = self.validate_response(
            response=requests.get(
                url=ApiEndpoints.LOGOUT_USER.format(host=self.host),
            )
        )
        return ApiResponse.model_validate_json(response.text)

    # POST /user/createWithArray
    @allure.step("Create users with array")
    def create_users_with_array(self, body: List[User]) -> ApiResponse:
        response = self.validate_response(
            response=requests.post(
                url=ApiEndpoints.CREATE_USERS_WITH_ARRAY.format(host=self.host),
                headers={"accept": ContentType.JSON, "Content-Type": ContentType.JSON},
                data=json.dumps(f"{body}"),
            )
        )
        return ApiResponse.model_validate_json(response.text)

    # POST /user
    @allure.step("Create user")
    def create_user(self, body: User) -> ApiResponse:
        response = self.validate_response(
            response=requests.post(
                url=ApiEndpoints.CREATE_USER.format(host=self.host),
                headers={"accept": ContentType.JSON, "Content-Type": ContentType.JSON},
                data=f"{body.model_dump_json()}",
            )
        )
        return ApiResponse.model_validate_json(response.text)