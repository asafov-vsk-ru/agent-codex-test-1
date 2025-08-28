import logging
from os import path

import allure

from pathlib import Path
from typing import Optional
from pydantic import BaseModel

logger = logging.getLogger("test_framework")


class EnvironmentConfig(BaseModel):
    data_base_host: Optional[str]
    grpc_service_host: Optional[str]
    rest_json_service_host: Optional[str]
    soap_xml_service_host: Optional[str]
    main_page_url: Optional[str]
    kafka_host: Optional[str]
    kafka_password: Optional[str]


class ApplicationConfig(BaseModel):
    grpc_timeout_keepalive: Optional[int]
    grpc_timeout_idle: Optional[int]
    grpc_retry_enable: Optional[bool]
    grpc_retry_max: Optional[int]
    grpc_security_type: Optional[str]
    rest_retry_enable: Optional[bool]
    rest_timeout: Optional[int]
    rest_log_level: Optional[str]
    rest_url_encoder: Optional[bool]
    kafka_key_serializer: Optional[str]
    kafka_value_serializer: Optional[str]
    kafka_key_deserializer: Optional[str]
    kafka_value_deserializer: Optional[str]
    kafka_consumer_group_id: Optional[str]
    kafka_security_protocol: Optional[str]
    kafka_sasl_mechanism: Optional[str]
    browser_type: Optional[str]
    browser_headless: Optional[bool]
    browser_timeout: Optional[int]
    browser_height: Optional[int]
    browser_width: Optional[int]
    browser_download: Optional[bool]
    browser_locale: Optional[str]
    browser_download_host: Optional[str]
    browser_download_timeout: Optional[int]
    browser_mobile_enable: Optional[bool]
    browser_tls_unauthorized: Optional[bool]


class ConfigFactory:
    environment_path: str = None
    application_path: str = None

    @classmethod
    @allure.step("Читаем настройки модулей и протоколов приложения")
    def load(cls, config_file_name: str) -> EnvironmentConfig | ApplicationConfig:
        if config_file_name.__contains__(".json"):
            return ConfigFactory.__load_environment_config(config_file_name)
        elif config_file_name.__contains__(".properties"):
            return ConfigFactory.__load_application_config(config_file_name)
        else:
            raise NotImplementedError("Метод не реализован!")

    @classmethod
    def __load_environment_config(cls, config_file_name: str = "local-env.json") -> EnvironmentConfig:
        file_path = ConfigFactory.__check_file_path(path.join(ConfigFactory.__check_catalog_path(), config_file_name))
        with open(file_path) as file:
            content = file.read()
        return EnvironmentConfig.model_validate_json(content)

    @classmethod
    def __load_application_config(cls, config_file_name: str = "application.properties") -> ApplicationConfig:
        comment_char: str = '#'
        separate_char: str = '='
        props: dict = {}
        file_path = ConfigFactory.__check_file_path(path.join(ConfigFactory.__check_catalog_path(), config_file_name))
        with open(file_path) as file:
            content = file.readlines()
            for line in content:
                if line.strip() and not line.strip().startswith(comment_char):
                    key_value = line.split(separate_char)
                    value = separate_char.join(key_value[1:]).strip()
                    props[key_value[0].strip().replace('.', '_')] = value
        return ApplicationConfig(**props)

    @classmethod
    def __check_catalog_path(cls) -> str:
        current_dir = Path(__file__).resolve().parents[2] / "resources"
        if current_dir.exists():
            return str(current_dir)
        else:
            raise FileNotFoundError("Директория \"resources\" отсутствует в проекте! Создайте нужный каталог "
                                    "с конфигурационными файлами и запустите приложение заново!")

    @classmethod
    def __check_file_path(cls, file_path) -> str:
        if path.exists(file_path):
            return file_path
        else:
            raise FileNotFoundError(f"Файл {file_path} не обнаружен!")
