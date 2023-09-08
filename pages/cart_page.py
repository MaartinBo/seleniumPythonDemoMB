import logging

import allure

import locators.locators


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        # we don't really need to do this in that way, but this way makes it easier to see which locators are used in that
        # pageobject, or we can assume that all locators in locators files are used, and we can reference directly in out methods to these locators,
        self.proceed_to_checkout_button = locators.locators.CartPage.proceed_to_checkout_button

    @allure.step("Opening address details page ")
    def open_address_details_page(self):
        self.logger.info("Opening address details page")
        self.driver.find_element(*self.proceed_to_checkout_button).click()
        self.logger.info("Opening address details page done")

