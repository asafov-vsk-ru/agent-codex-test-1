import os
import allure

from playwright.sync_api import BrowserType, sync_playwright, Playwright, Browser, ViewportSize
from core.utils.config_helper import ApplicationConfig


class BrowserFactory:

    def __init__(self, config: ApplicationConfig):
        self.__config = config

    def __get_browser_type(self, playwright: Playwright) -> BrowserType:
        browser = os.environ["BROWSER"]
        if browser == "Chrome":
            browser_type = playwright.chromium
        elif browser == "Firefox":
            browser_type = playwright.firefox
        else:
            browser_type = playwright.webkit
        return browser_type

    @allure.step("Настраиваем браузер")
    def get_browser(self) -> Browser:
        options: dict = {"PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD": "1",
                         "PLAYWRIGHT_BROWSERS_PATH": "$HOME/pw-browsers",
                         "NODE_TLS_REJECT_UNAUTHORIZED": "0"}
        if self.__config.browser_download:
            if self.__config.browser_download_host is not None:
                options.update({"PLAYWRIGHT_DOWNLOAD_HOST": self.__config.browser_download_host})
                options.update({"PLAYWRIGHT_DOWNLOAD_CONNECTION_TIMEOUT": f"{self.__config.browser_download_timeout}"})
                options.update({"PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD": "0"})
            else:
                raise ArithmeticError("Не заполнен файл application.config!")
        if self.__config.browser_tls_unauthorized:
            options.update({"NODE_TLS_REJECT_UNAUTHORIZED": "1"})
        browser_type: BrowserType = self.__get_browser_type(sync_playwright().start())
        browser = browser_type.launch(env=options,
                                      headless=self.__config.browser_headless)
        screen = ViewportSize({"width": self.__config.browser_width, "height": self.__config.browser_height})
        context = browser.new_context(screen=screen,
                                      locale=self.__config.browser_locale,
                                      is_mobile=self.__config.browser_mobile_enable)
        return context.browser
