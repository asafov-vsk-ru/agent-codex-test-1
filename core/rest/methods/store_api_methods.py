import requests
import allure

from core.rest.config.api_endpoints import ApiEndpoints
from core.rest.config.content_type import ContentType
from core.rest.methods.api_methods import ApiMethods
from core.rest.models.api_response_model import ApiResponse
from core.rest.models.order_model import Order


class StoreApiMethods(ApiMethods):

    def __init__(self, host: str):
        super().__init__(host)

    # GET /store/inventory
    @allure.step("Get store inventory")
    def store_inventory(self) -> ApiResponse:
        response = self.validate_response(
            response=requests.get(
                url=ApiEndpoints.STORE_INVENTORY.format(host=self.host),
            )
        )
        return ApiResponse.model_validate_json(response.text)

    # POST /store/order
    @allure.step("Create store order")
    def create_store_order(self, body: Order) -> ApiResponse:
        response = self.validate_response(
            response=requests.post(
                url=ApiEndpoints.CREATE_STORE_ORDER.format(host=self.host),
                headers={"accept": ContentType.JSON, "Content-Type": ContentType.JSON},
                data=f"{body.model_dump_json()}",
            )
        )
        return ApiResponse.model_validate_json(response.text)

    # GET /store/order/{orderId}
    @allure.step("Get store order by id")
    def get_order_by_id(self, order_id: int) -> ApiResponse:
        response = self.validate_response(
            response=requests.get(
                url=ApiEndpoints.GET_ORDER_BY_ID.format(host=self.host, order_id=order_id),
            )
        )
        return ApiResponse.model_validate_json(response.text)

    # DELETE /store/order/{orderId}
    @allure.step("Delete store order by id")
    def delete_order(self, order_id: int) -> ApiResponse:
        response = self.validate_response(
            response=requests.delete(
                url=ApiEndpoints.DELETE_ORDER.format(host=self.host, order_id=order_id),
            )
        )
        return ApiResponse.model_validate_json(response.text)
