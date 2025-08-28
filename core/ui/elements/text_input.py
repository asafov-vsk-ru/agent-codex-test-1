import allure
from playwright.sync_api import Locator

from core.ui.elements.base_elements import BaseElement


class TextInput(BaseElement):
    @property
    def type_of(self) -> str:
        return "input field"

    def get_locator(self, **kwargs) -> Locator:
        return self.page.get_by_label(self.locator, exact=True)

    def fill(self, value: str, **kwargs) -> None:
        with allure.step(f'Fill {self.type_of} "{self.name}" with "{value}"'):
            locator = self.get_locator(**kwargs)
            locator.fill(value)
