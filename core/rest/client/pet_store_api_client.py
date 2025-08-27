from core.rest.client.api_client import ApiClient
from core.rest.methods.pet_api_methods import PetApiMethods
from core.rest.methods.store_api_methods import StoreApiMethods
from core.rest.methods.user_api_methods import UserApiMethods


class PetStoreApiClient(ApiClient):
    pet_api_methods: PetApiMethods = None
    store_api_methods: StoreApiMethods = None
    user_api_methods: UserApiMethods = None

    def __init__(self, host: str):
        super().__init__(host)
        self.pet_api_methods = PetApiMethods(self.base_host)
        self.store_api_methods = StoreApiMethods(self.base_host)
        self.user_api_methods = UserApiMethods(self.base_host)
