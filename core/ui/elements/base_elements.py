import allure
from playwright.sync_api import Locator, Page, expect
from abc import ABC, abstractmethod


class BaseElement(ABC):
    def __init__(self, page: Page, locator: str, name: str) -> None:
        self.page = page
        self.locator = locator
        self.name = name

    @property
    @abstractmethod
    def type_of(self) -> str:
        return 'component'

    def get_locator(self, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        return self.page.locator(locator)

    def should_be_visible(self, **kwargs) -> None:
        with allure.step(f'Checking that {self.type_of} "{self.name}" is visible'):
            locator = self.get_locator(**kwargs)
            expect(locator).to_be_visible()

    def should_be_enable(self, **kwargs) -> None:
        with allure.step(''):
            locator = self.get_locator(**kwargs)
            expect(locator).to_be_visible()
