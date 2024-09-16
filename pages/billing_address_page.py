import logging

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.select import Select

from locators.locators import BillingAddressLocators


class BillingAddressPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        # we don't really need to do this in that way, but this way makes it easier to see which locators are used in that
        # pageobject, or we can assume that all locators in locators files are used, and we can reference directly in out methods to these locators,
        self.first_name_input = BillingAddressLocators.first_name_input
        self.last_name_input = BillingAddressLocators.last_name_input
        self.addresses_link = BillingAddressLocators.addresses_link
        self.edit_link = BillingAddressLocators.edit_link
        self.country_select = BillingAddressLocators.country_select
        self.addresses_input = BillingAddressLocators.address_input
        self.postcode_input = BillingAddressLocators.postcode_input
        self.city_input = BillingAddressLocators.city_input
        self.phone_input = BillingAddressLocators.phone_input
        self.save_address_button = BillingAddressLocators.save_address_button
        self.msg_div = BillingAddressLocators.message_div

    @allure.step("Opening edit billing address")
    def open_edit_billing_address(self):
        self.logger.info("Opening edit billing page")
        self.driver.find_element(*self.addresses_link).click()
        self.driver.find_element(*self.edit_link).click()
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Opening edit billing address",
            attachment_type=AttachmentType.PNG,
        )
        self.logger.info("Opening edit billing page done")

    @allure.step("Setting personal data, first-name: '{1}' and last-name: {2}")
    def set_personal_data(self, first_name, last_name):
        self.logger.info(
            f"Setting first name - {first_name} and last name - {last_name}"
        )
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.logger.info(
            f"Setting first name - {first_name} and last name - {last_name} done"
        )

    @allure.step("Selecting country - '{1}'")
    def select_country(self, country):
        self.logger.info(f"Selecting country - {country}")
        select = Select(self.driver.find_element(*self.country_select))
        select.select_by_visible_text(country)
        self.logger.info(f"Selecting country - {country} done")

    @allure.step("Setting address, street - '{1} , postcode - {2} , city - {3} ")
    def set_address(self, street, postcode, city):
        self.logger.info(
            f"Setting street - {street} postcode - {postcode} city - {city}"
        )
        self.driver.find_element(*self.addresses_input).send_keys(street)
        self.driver.find_element(*self.postcode_input).send_keys(postcode)
        self.driver.find_element(*self.city_input).send_keys(city)
        self.logger.info(
            f"Setting street - {street} postcode - {postcode} city - {city} done"
        )

    @allure.step("Selecting phone number - '{1}'")
    def set_phone_number(self, number):
        self.logger.info(f"Setting phone number - {number}")
        self.driver.find_element(*self.phone_input).send_keys(number)
        self.logger.info(f"Setting phone number - {number} done")

    @allure.step("Clicking save address button")
    def save_address(self):
        self.logger.info("Clicking save address button")
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            self.driver.find_element(*self.save_address_button),
        )
        self.driver.find_element(*self.save_address_button).click()
        self.logger.info("Clicking save address button done")

    @allure.step("Getting message text")
    def get_message_text(self):
        self.logger.info("Getting message text")
        return self.driver.find_element(*self.msg_div).text
