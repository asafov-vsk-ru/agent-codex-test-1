import requests
import allure

from core.rest.config.api_endpoints import ApiEndpoints
from core.rest.config.content_type import ContentType
from core.rest.methods.api_methods import ApiMethods
from core.rest.models.api_response_model import ApiResponse
from core.rest.models.pet_model import Pet, PetStatus
from core.rest.models.tag_model import Tag
from typing import BinaryIO, List


class PetApiMethods(ApiMethods):

    def __init__(self, host: str):
        super().__init__(host)

    # POST /pet/{petId}/uploadImage
    @allure.step("Upload image for pet by id")
    def upload_pet_image(self, pet_id: int, additional_metadata: str, file: BinaryIO) -> ApiResponse:
        response = self.validate_response(
            response=requests.post(
                url=ApiEndpoints.UPLOAD_PET_IMAGE.format(host=self.host, pet_id=pet_id),
                headers={"accept": ContentType.FORM, "Content-Type": ContentType.FORM},
                params={"additionalMetadata": additional_metadata, "file": file},
            )
        )
        return ApiResponse.model_validate_json(response.text)

    # POST /pet
    @allure.step("Create pet")
    def create_pet(self, body: Pet) -> ApiResponse:
        response = self.validate_response(
            response=requests.post(
                url=ApiEndpoints.CREATE_PET.format(host=self.host),
                headers={"accept": ContentType.JSON, "Content-Type": ContentType.JSON},
                data=f"{body.model_dump_json()}",
            )
        )
        return ApiResponse.model_validate_json(response.text)

    # PUT /pet
    @allure.step("Update existing pet")
    def update_existing_pet(self, body: Pet) -> ApiResponse:
        response = self.validate_response(
            response=requests.put(
                url=ApiEndpoints.UPDATE_EXISTING_PET.format(host=self.host),
                headers={"accept": ContentType.JSON, "Content-Type": ContentType.JSON},
                data=f"{body.model_dump_json()}",
            )
        )
        return ApiResponse.model_validate_json(response.text)

    # GET /pet/findByStatus
    @allure.step("Find pet by status")
    def upload_pet_image(self, statuses: List[PetStatus]) -> ApiResponse:
        response = self.validate_response(
            response=requests.get(
                url=ApiEndpoints.FIND_PET_BY_STATUS.format(host=self.host),
                params={"status": statuses},
            )
        )
        return ApiResponse.model_validate_json(response.text)

    # GET /pet/findByTags
    @allure.step("Find pet by tags")
    def upload_pet_image(self, tags: List[Tag]) -> ApiResponse:
        response = self.validate_response(
            response=requests.get(
                url=ApiEndpoints.FIND_PET_BY_TAGS.format(host=self.host),
                params={"tag": tags},
            )
        )
        return ApiResponse.model_validate_json(response.text)

    # GET /pet/{petId}
    @allure.step("Get pet by id")
    def get_pet_by_id(self, pet_id: int) -> ApiResponse:
        response = self.validate_response(
            response=requests.get(
                url=ApiEndpoints.GET_PET_BY_ID.format(host=self.host, pet_id=pet_id),
            )
        )
        return ApiResponse.model_validate_json(response.text)

    # POST /pet/{petId}
    @allure.step("Update pet in store")
    def update_pet_in_store(self, pet_id: int, name: str, status: PetStatus) -> ApiResponse:
        response = self.validate_response(
            response=requests.get(
                url=ApiEndpoints.UPDATE_PET_IN_STORE.format(host=self.host, pet_id=pet_id),
                headers={"accept": ContentType.FORM, "Content-Type": ContentType.FORM},
                params={"name": name, "status": status},
            )
        )
        return ApiResponse.model_validate_json(response.text)

    # DELETE /pet/{petId}
    @allure.step("Delete pet by id")
    def delete_pet(self, api_key: str, pet_id: int) -> ApiResponse:
        response = self.validate_response(
            response=requests.delete(
                url=ApiEndpoints.DELETE_PET.format(host=self.host, pet_id=pet_id),
                headers={"api_key": api_key},
            )
        )
        return ApiResponse.model_validate_json(response.text)
