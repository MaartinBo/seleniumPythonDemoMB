from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class DriverFactory:
    @staticmethod
    def get_driver(browser):
        if browser == "chrome":
            options = Options()
            options.add_argument("--headless")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            return webdriver.Chrome(
                service=Service(ChromeDriverManager().install()), options=options
            )
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.headless = True
            return webdriver.Firefox(
                service=Service(GeckoDriverManager().install()), options=options
            )
        raise Exception("Provide valid driver name")
