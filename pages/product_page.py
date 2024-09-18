import logging

import allure

import locators.locators


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.add_to_cart_button = locators.locators.ProductPage.add_to_cart_button
        self.view_cart_button = locators.locators.ProductPage.view_cart_button

    @allure.step("Adding product to cart ")
    def add_product_to_cart(self):
        self.logger.info("Adding product to cart")
        self.driver.find_element(*self.add_to_cart_button).click()
        self.logger.info("Adding product to cart done")

    @allure.step("Go to view cart ")
    def view_cart(self):
        self.logger.info("Going to view cart page")
        self.driver.find_element(*self.view_cart_button).click()
        self.logger.info("Going to view cart page done")
