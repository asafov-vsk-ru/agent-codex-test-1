from core.utils.config_helper import ApplicationConfig, logger


class KafkaUtils:

    @classmethod
    def get_consumer_properties(cls, app_config: ApplicationConfig):
        properties = {
            "security.protocol": app_config.kafka_security_protocol,
            "sasl.mechanism": app_config.kafka_sasl_mechanism,
            "group.id": app_config.kafka_consumer_group_id,
            "enable.auto.commit": False,
            "enable.auto.offset.store": True,
            "auto.offset.reset": "smallest"
        }
        return properties

    @classmethod
    def get_producer_properties(cls, app_config: ApplicationConfig):
        properties = {
            "security.protocol": app_config.kafka_security_protocol,
            "sasl.mechanism": app_config.kafka_sasl_mechanism,
            "client.id": app_config.kafka_consumer_group_id,
            "enable.auto.commit": True,
            "auto.commit.interval.ms": 1000
        }
        return properties

    @classmethod
    def delivery_report(cls, error, message):
        if error is not None:
            logger.error(f"Ошибка доставки сообщения: {error}")
            print(f"Ошибка доставки сообщения: {error}")
        else:
            logger.info(f"Сообщение доставлено {message.topic()} [{message.partition()}]")
            print(f"Сообщение доставлено {message.topic()} [{message.partition()}]")
