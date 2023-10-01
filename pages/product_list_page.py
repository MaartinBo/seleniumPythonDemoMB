import logging

import allure
from selenium.webdriver.common.by import By

import locators.locators


class ProductListPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        # we don't really need to do this in that way, but this way makes it easier to see which locators are used in that
        # pageobject, or we can assume that all locators in locators files are used, and we can reference directly in out methods to these locators,
        self.product_price_xpath = locators.locators.ProductListPage.product_price_xpath
        self.product_button_xpath = locators.locators.ProductListPage.product_button_xpath

    @allure.step("Opening products list page")
    def open_products_list_page(self):
        self.logger.info("Opening Products List Page")
        self.driver.get("https://mb-qa.eu/shop/")

    @allure.step("Opening product")
    def open_product(self, product):
        self.logger.info((f"Opening product - {product}"))
        product = self.product_price_xpath.format(product)
        product_button = self.driver.find_element(By.XPATH, product)
        product_button.click()
        self.logger.info((f"Opening product - {product} done"))

    @allure.step("Validate product '[1]' actual price with expected price from Excel")
    def validate_product_actual_price(self, product, ExpectedPrice):
        self.logger.info((f"Validate product - {product} actual price with expected price from excel"))

        xpath = self.product_price_xpath.format(product)

        product_price_elements = self.driver.find_elements(By.XPATH, xpath)

        formatted_expected_price_value = "{:.2f}".format(ExpectedPrice)
        # change the expected price from Excel to float .00

        if len(product_price_elements) > 1:
            # Handle the case when there are multiple matching elements
            # If there are multiple elements, the product has a discount, so the second element is the actual price
            product_price_element = product_price_elements[1]
            actual_price = product_price_element.text
            actual_price_trimmed = actual_price.replace('$', '')
            print(actual_price_trimmed)

            assert actual_price_trimmed == formatted_expected_price_value, f"Actual price: {actual_price_trimmed} , Expected price: {formatted_expected_price_value}"

        elif len(product_price_elements) == 1:
            # Handle the case when there is a single matching element
            product_price_element = product_price_elements[0]
            actual_price = product_price_element.text

            # Remove the currency symbol and any extra characters
            actual_price_trimmed = actual_price.replace('$', '')
            print(actual_price_trimmed)

            assert actual_price_trimmed == formatted_expected_price_value, f"Actual price: {actual_price_trimmed}, Expected price: {formatted_expected_price_value}"
        else:
            print("No matching element found with the price of Product Name")

        self.logger.info((f"Validate product - {product} actual price with expected price from excel done"))

