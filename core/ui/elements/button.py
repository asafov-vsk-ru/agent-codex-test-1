import allure
from playwright.sync_api import Locator

from core.ui.elements.base_elements import BaseElement


class Button(BaseElement):
    @property
    def type_of(self) -> str:
        return "button"

    def get_locator(self, **kwargs) -> Locator:
        return self.page.get_by_role("button", name=self.locator, exact=True)

    def click(self, **kwargs) -> None:
        with allure.step(f'Click {self.type_of} "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.click()
