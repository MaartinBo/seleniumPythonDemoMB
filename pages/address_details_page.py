import logging
import time

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

import locators.locators
from models.customer import Customer


# pylint: disable=too-many-instance-attributes
class AddressDetailsPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
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

        max_retries = 2  # Set the maximum number of retry attempts
        retry_count = 0

        while retry_count < max_retries:
            try:
                # Wait for the place order button to be clickable
                place_order_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.driver.find_element(*self.place_order_button))
                )
                place_order_button.click()
                break  # If successful, exit the loop
            except Exception as ex:
                # Handle any exceptions here (e.g., StaleElementReferenceException)
                self.logger.info(
                    "Exception while clicking order button (Attempt %d): %s", retry_count + 1, ex
                )
                retry_count += 1
                if retry_count < max_retries:
                    # Wait for a short time before the next retry
                    time.sleep(2)

        if retry_count == max_retries:
            self.logger.error("Failed to click order button after %d attempts", max_retries)
        else:
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

        select = Select(billing_country_dropdown)
        select.select_by_visible_text(customer.country)

        self.driver.find_element(*self.billing_address_input).send_keys(
            f"{customer.street} {customer.flat_number}"
        )

        self.driver.find_element(*self.billing_post_code_input).send_keys(customer.zip_code)
        self.driver.find_element(*self.billing_city_input).send_keys(customer.city)
        self.driver.find_element(*self.billing_phone_input).send_keys(customer.phone)
        self.driver.find_element(*self.billing_email_input).send_keys(customer.email)
        self.driver.find_element(*self.order_comments_input).send_keys(comments)

        self.logger.info("Filling all of the address details done")
