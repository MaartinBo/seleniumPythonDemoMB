import logging

import allure

import locators.locators


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.proceed_to_checkout_button = locators.locators.CartPage.proceed_to_checkout_button

    @allure.step("Opening address details page ")
    def open_address_details_page(self):
        self.logger.info("Opening address details page")
        self.driver.find_element(*self.proceed_to_checkout_button).click()
        self.logger.info("Opening address details page done")
