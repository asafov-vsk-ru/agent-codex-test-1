import allure
from core.ui.elements.base_elements import BaseElement


class Table(BaseElement):
    @property
    def type_of(self) -> str:
        return "table"

    def should_have_records(self, **kwargs) -> None:
        with allure.step(f'Check {self.type_of} "{self.name}" has records'):
            locator = self.get_locator(**kwargs)
            locator.first.wait_for(timeout=5000)
            assert locator.count() > 0, f"{self.type_of} '{self.name}' has no records"
