import os

from faker import Faker
from core.database.database_client import DataBaseClient
from core.grpc.grpc_client import GrpcClient
from core.kafka.kafka_client import KafkaClient
from core.utils.browser_helper import BrowserFactory
from core.utils.config_helper import ConfigFactory, EnvironmentConfig, ApplicationConfig
from core.rest.client.pet_store_api_client import PetStoreApiClient
from playwright.sync_api import Browser


class BaseTest:
    env_config: EnvironmentConfig = None
    app_config: ApplicationConfig = None
    faker: Faker = None
    pet_store: PetStoreApiClient = None
    kafka: KafkaClient = None
    grpc: GrpcClient = None
    database: DataBaseClient = None
    browser: Browser = None

    def setup_method(self):
        self.env_config = ConfigFactory().load(f"{os.environ['ENVIRONMENT']}-env.json")
        self.app_config = ConfigFactory().load(f"application.properties")
        self.faker = Faker()
        self.pet_store = PetStoreApiClient(host=self.env_config.rest_json_service_host)
        self.kafka = KafkaClient(host=self.env_config.kafka_host, username="test", config=self.app_config)
        self.grpc = GrpcClient(host=self.env_config.grpc_service_host)
        # self.database = DataBaseClient(host=self.env_config.data_base_host, username="test")
        self.browser = BrowserFactory(config=self.app_config).get_browser()
