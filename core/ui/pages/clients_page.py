from core.ui.pages.base_page import BasePage
from core.ui.module.clients_search_form import ClientsSearchForm


class ClientsPage(BasePage):
    _url: str = "https://stage-frontend-arm-ui.apps.stg-okd-lan.vsk.ru/clients"
    _title: str = "ВСК"

    def __init__(self, page):
        super().__init__(page)
        self.search_form = ClientsSearchForm(page)

    def search_clients(self, fio: str, birth_year: str) -> None:
        self.search_form.search(fio, birth_year)

    def should_have_results(self) -> None:
        self.search_form.results_table.should_have_records()
