import os

import allure
import grpc

from grpc_reflection.v1alpha.proto_reflection_descriptor_database import ProtoReflectionDescriptorDatabase
from google.protobuf.descriptor_pool import DescriptorPool
from enum import Enum
from typing import List
from core.utils.config_helper import logger


class CredentialType(Enum):
    NONE = 0
    TOKEN = 1
    CERTIFICATE = 2


class GrpcClient:
    host = None
    reflection = None
    channel = None
    options = None
    __credential = None
    __token = None
    __certificate = None

    def __init__(self, host: str, reflection: bool = True):
        self.host = host
        self.reflection = reflection

    @allure.step("Получаем список всех gRPC сервисов")
    def get_all_services_names(self) -> List[str]:
        reflection_db = ProtoReflectionDescriptorDatabase(self.get_channel())
        return list(reflection_db.get_services())

    @allure.step("Получаем конкретный сервис по имени")
    def get_service_by_name(self, service_name: str):
        reflection_db = ProtoReflectionDescriptorDatabase(self.get_channel())
        desc_pool = DescriptorPool(reflection_db)
        return desc_pool.FindServiceByName(service_name)

    @allure.step("Создаем gRPC канал")
    def get_channel(self) -> grpc.Channel:
        try:
            secure_type: CredentialType = self.__get_credential_type()
            if secure_type == CredentialType.NONE:
                self.channel = grpc.insecure_channel(self.host, self.options)
            elif secure_type == CredentialType.TOKEN:
                access = grpc.access_token_call_credentials(self.__token)
                self.__credential = grpc.composite_channel_credentials(access)
                self.channel = grpc.secure_channel(self.host, self.__credential, self.options)
            else:
                self.__credential = grpc.ssl_channel_credentials(self.__certificate)
                self.channel = grpc.secure_channel(self.host, self.__credential, self.options)
            return self.channel
        except BaseException:
            logger.error("Ошибка создания gRPC соединения, проверьте параметры!")
            print("Ошибка создания gRPC соединения, проверьте параметры!")

    def __get_credential_type(self):
        grpc_token = os.environ["GRPC_TOKEN"]
        certificate_path = os.environ["GRPC_CERTIFICATE"]
        if grpc_token is None and certificate_path is None:
            return grpc.insecure_channel(self.host)
        elif certificate_path is None:
            return CredentialType.TOKEN
        else:
            return CredentialType.CERTIFICATE
