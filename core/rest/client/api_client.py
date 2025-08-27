from abc import ABC


class ApiClient(ABC):
    base_host = None

    def __init__(self, base_host: str):
        self.base_host = base_host
