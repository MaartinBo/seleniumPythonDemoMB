import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:
    @staticmethod
    def get_driver(browser):
        if browser == "chrome":
            options = ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-infobars")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-browser-side-navigation")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            return webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()), options=options
            )
        if browser == "firefox":
            options = FirefoxOptions()
            options.add_argument("-headless")
            service = FirefoxService(
                GeckoDriverManager().install(), log_output=os.devnull  # ignore firefox logs
            )
            return webdriver.Firefox(service=service, options=options)

        raise Exception("Provide valid driver name")
