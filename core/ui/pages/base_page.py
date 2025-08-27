import re
import allure
from abc import ABC
from playwright.sync_api import Page, Response, expect


class BasePage(ABC):
    _url: str = None
    _title: str = None

    def __init__(self, page: Page):
        self._page = page

    def open(self, **kwargs) -> Response | None:
        with allure.step(f'Открываем страницу {self._url}'):
            page = self._page.goto(self._url, **kwargs)
        expect(page).to_have_title(re.compile(self._title))
        return page

    def refresh(self, **kwargs) -> Response | None:
        with allure.step(f'Обновляем страницу {self._url}'):
            page = self._page.reload(**kwargs)
        return page

    def get_title(self) -> str:
        return self._page.title()

    def get_page_header(self):
        page = self._page.get_by_
        return self._page.locator('')

    def get_page_body_content(self):
        return self._page.locator('')

    def get_page_footer(self):
        return self._page.locator('')
