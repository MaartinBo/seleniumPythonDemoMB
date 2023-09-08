import logging

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

import locators.locators
from Models.customer import Customer


class AddressDetailsPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        # we don't really need to do this in that way, but this way makes it easier to see which locators are used in that
        # pageobject, or we can assume that all locators in locators files are used, and we can reference directly in out methods to these locators,
        self.first_name_input = locators.locators.AddressDetailsPage.first_name_input
        self.last_name_input = locators.locators.AddressDetailsPage.last_name_input
        self.company_name_input = locators.locators.AddressDetailsPage.company_name_input
        self.billing_country_select = locators.locators.AddressDetailsPage.billing_country_select
        self.billing_address_input = locators.locators.AddressDetailsPage.billing_address_input
        self.billing_post_code_input = locators.locators.AddressDetailsPage.billing_post_code_input
        self.billing_city_input = locators.locators.AddressDetailsPage.billing_city_input
        self.billing_phone_input = locators.locators.AddressDetailsPage.billing_phone_input
        self.billing_email_input = locators.locators.AddressDetailsPage.billing_email_input
        self.order_comments_input = locators.locators.AddressDetailsPage.order_comments_input

        self.place_order_button = locators.locators.AddressDetailsPage.place_order_button

    @allure.step("Opening address details page ")
    def click_order_button_without_ex(self):
        self.logger.info("Clicking order button")

        try:
            # Wait for the place order button to be clickable
            place_order_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.driver.find_element(*self.place_order_button))
            )
            place_order_button.click()
        except Exception as ex:
            # Handle any exceptions here (e.g., StaleElementReferenceException)
            self.logger.error("Error while clicking order button:", ex)

        self.logger.info("Clicking order button done")

    @allure.step("Filling all of the address details ")
    def fill_address_details(self, comments):
        self.logger.info("Filling all of the address details")
        customer = Customer()
        self.driver.find_element(*self.first_name_input).send_keys(customer.first_name)
        self.driver.find_element(*self.last_name_input).send_keys(customer.last_name)
        self.driver.find_element(*self.company_name_input).send_keys(customer.company_name)

        # Locate the billing country dropdown element
        billing_country_dropdown = self.driver.find_element(*self.billing_country_select)

        # Create a Select object for the dropdown
        select = Select(billing_country_dropdown)

        # Select the option by visible text
        select.select_by_visible_text(customer.country)

        self.driver.find_element(*self.billing_address_input).send_keys(f"{customer.street} {customer.flat_number}")

        self.driver.find_element(*self.billing_post_code_input).send_keys(customer.zip_code)
        self.driver.find_element(*self.billing_city_input).send_keys(customer.city)
        self.driver.find_element(*self.billing_phone_input).send_keys(customer.phone)
        self.driver.find_element(*self.billing_email_input).send_keys(customer.email)
        self.driver.find_element(*self.order_comments_input).send_keys(comments)

        self.logger.info("Filling all of the address details done")
