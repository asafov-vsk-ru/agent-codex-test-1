import os
import allure

from typing import List
from confluent_kafka import Consumer, Producer, KafkaError, KafkaException
from confluent_kafka.cimpl import TopicPartition
from core.utils.config_helper import ApplicationConfig
from core.utils.config_helper import logger
from core.utils.kafka_helper import KafkaUtils


class KafkaClient:
    __consumer: Consumer = None
    __producer: Producer = None
    __consumer_properties: dict = None
    __producer_properties: dict = None
    host: str = None

    def __init__(self, host: str, username: str, config: ApplicationConfig):
        self.host = host
        self.__producer_properties = KafkaUtils.get_producer_properties(config)
        self.__consumer_properties = KafkaUtils.get_consumer_properties(config)
        self.__producer_properties["bootstrap.servers"] = host
        self.__producer_properties["sasl.username"] = username
        self.__producer_properties["sasl.password"] = os.environ["KAFKA_PASSWORD"]
        self.__consumer_properties["bootstrap.servers"] = host
        self.__consumer_properties["sasl.username"] = username
        self.__consumer_properties["sasl.password"] = os.environ["KAFKA_PASSWORD"]

    @allure.step("Инициализация консьюмера кафки")
    def init_consumer(self, properties: dict = None) -> Consumer:
        if self.__consumer is None:
            if properties is None:
                properties = self.__producer_properties
            self.__consumer = Consumer(properties)
        return self.__consumer

    @allure.step("Инициализация продьюсера кафки")
    def init_producer(self, properties: dict = None) -> Producer:
        if self.__producer is None:
            if properties is None:
                properties = self.__producer_properties
            self.__producer = Producer(properties)
        return self.__producer

    @allure.step("Отправка сообщения в топик кафки")
    def send_message(self, topic: str, key: str, message: str):
        self.__producer.produce(topic, key=key, value=message, callback=KafkaUtils.delivery_report)
        self.__producer.poll(1)
        self.__producer.flush()
        self.__producer.close()

    @allure.step("Чтение сообщения из топика кафки")
    def read_message(self, topics: List[str], count: int = 1) -> str:
        try:
            self.__consumer.subscribe(topics)
            while count > 0:
                message = self.__consumer.poll(timeout=1.0)
                if message is None:
                    count = count - 1
                    continue
                elif message.error():
                    if message.error().code() == KafkaError.PARTITION_EOF:
                        logger.error('%% %s [%d] reached end at offset %d\n' %
                                     (message.topic(), message.partition(), message.offset()))
                        print("%% %s [%d] reached end at offset %d\n" %
                              (message.topic(), message.partition(), message.offset()))
                    elif message.error():
                        raise KafkaException(message.error())
                else:
                    return message
        finally:
            self.__consumer.close()

    @allure.step("Подписка на конкретную партицию")
    def subscribe_topic_partition(self, topic_partition: str, partition_number: int = 0):
        self.__consumer.assign([TopicPartition(topic_partition, partition_number)])

    @allure.step("Смеремещение к определенному смещению в партиции")
    def seek_topic_partition(self, topic_partition: str, partition_number: int = 0, count: int = 10):
        self.__consumer.seek(TopicPartition(topic_partition, partition_number, count))
