import allure
import pytest

from core.rest.models.user_model import User
from tests.base_test import BaseTest


@allure.epic("Kafka")
@allure.feature("Kafka - Read/Write operations")
class TestKafka(BaseTest):

    @pytest.mark.regression
    @allure.id("021")
    @allure.title("021. Kafka - write operation")
    @allure.description("This test send message in topic kafka")
    @allure.tag("Smoke", "Functional", "Positive")
    def test_send_message(self):
        topic = "Test topic"
        key = "Test key"
        message = "Test message"
        self.kafka_client.send_message(topic=topic, key=key, message=message)

    @pytest.mark.regression
    @allure.id("022")
    @allure.title("022. Kafka - read operation")
    @allure.description("This test read message from topic kafka")
    @allure.tag("Functional", "Positive")
    def test_read_message(self):
        pass
