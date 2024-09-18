import logging

import allure
from selenium.webdriver.common.by import By

import locators.locators


class ProductListPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.product_price_xpath = locators.locators.ProductListPage.product_price_xpath
        self.product_button_xpath = locators.locators.ProductListPage.product_button_xpath

    @allure.step("Opening products list page")
    def open_products_list_page(self):
        self.logger.info("Opening Products List Page")
        self.driver.get("https://mb-qa.eu/shop/")

    @allure.step("Opening product")
    def open_product(self, product):
        self.logger.info("Opening product - %s", product)
        product_xpath = self.product_price_xpath.format(product)
        product_button = self.driver.find_element(By.XPATH, product_xpath)
        product_button.click()
        self.logger.info("Opening product - %s done", product)

    @allure.step("Validate product '[1]' actual price with expected price from Excel")
    def validate_product_actual_price(self, product, ExpectedPrice):
        self.logger.info(
            "Validate product - %s actual price with expected price from excel", product
        )

        xpath = self.product_price_xpath.format(product)
        product_price_elements = self.driver.find_elements(By.XPATH, xpath)

        formatted_expected_price_value = f"{ExpectedPrice:.2f}"
        # change the expected price from Excel to float .00

        if len(product_price_elements) > 1:
            product_price_element = product_price_elements[1]
            actual_price = product_price_element.text
            actual_price_trimmed = actual_price.replace("$", "")
            print(actual_price_trimmed)

            assert actual_price_trimmed == formatted_expected_price_value, (
                f"Actual price: {actual_price_trimmed} , "
                f"Expected price: {formatted_expected_price_value}"
            )

        elif len(product_price_elements) == 1:
            product_price_element = product_price_elements[0]
            actual_price = product_price_element.text

            actual_price_trimmed = actual_price.replace("$", "")
            print(actual_price_trimmed)

            assert actual_price_trimmed == formatted_expected_price_value, (
                f"Actual price: {actual_price_trimmed}, "
                f"Expected price: {formatted_expected_price_value}"
            )
        else:
            print("No matching element found with the price of Product Name")

        self.logger.info(
            "Validate product - %s actual price with expected price from excel done", product
        )
