from core.ui.module.base_module import BaseModule
from core.ui.elements.text_input import TextInput
from core.ui.elements.button import Button
from core.ui.elements.table import Table


class ClientsSearchForm(BaseModule):
    def __init__(self, page):
        super().__init__(page, "Clients search form")
        self.fio_input = TextInput(page, "ФИО", "ФИО")
        self.birth_year_input = TextInput(page, "Год рождения", "Год рождения")
        self.search_button = Button(page, "Поиск", "Поиск")
        self.results_table = Table(page, "tbody tr[tuitr]", "Search results")

    def search(self, fio: str, birth_year: str) -> None:
        self.fio_input.fill(fio)
        self.birth_year_input.fill(birth_year)
        self.search_button.click()
