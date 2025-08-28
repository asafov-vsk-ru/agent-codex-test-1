from abc import ABC
from playwright.sync_api import Page


class BaseModule(ABC):
    """Base class for page modules."""

    def __init__(self, page: Page, name: str) -> None:
        self.page = page
        self.name = name
