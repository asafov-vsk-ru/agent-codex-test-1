import os

import allure
import sqlalchemy
from sqlalchemy import Connection, Engine


class DataBaseClient:
    engine: Engine = None
    connection: Connection = None

    def __init__(self, host: str, username: str):
        uri = self.__get_uri(host, username)
        self.engine = sqlalchemy.create_engine(uri)

    def __get_uri(self, host: str, username: str) -> str:
        password = os.environ["DB_PASSWORD"]
        if host.__contains__("postgresql"):
            provider = "postgresql+psycopg2"
        elif host.__contains__("mysql"):
            provider = "mysql+pymysql"
        else:
            raise ConnectionError("Данное соединение не поддерживается!")
        return f"{provider}://{username}:{password}@{host}"

    @allure.step("Открываем соединение с базой данных")
    def connect(self) -> Connection:
        if self.connection is None:
            self.connection = self.engine.connect()
        return self.connection

    @allure.step("Закрываем соединение")
    def disconnect(self):
        self.connection.close()
