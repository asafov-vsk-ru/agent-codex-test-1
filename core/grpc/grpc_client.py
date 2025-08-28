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
    __certificate_path = None

    def __init__(self, host: str, reflection: bool = True, token: str | None = None, certificate_path: str | None = None):
        self.host = host
        self.reflection = reflection
        self.__token = token
        self.__certificate_path = certificate_path

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
        grpc_token = self.__token
        certificate_path = self.__certificate_path
        if not grpc_token and not certificate_path:
            return CredentialType.NONE
        elif not certificate_path:
            return CredentialType.TOKEN
        else:
            try:
                with open(certificate_path, "rb") as cert:
                    self.__certificate = cert.read()
            except (OSError, TypeError):
                self.__certificate = None
            return CredentialType.CERTIFICATE
