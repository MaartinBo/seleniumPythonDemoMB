import logging

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.select import Select

from locators.locators import BillingAddressLocators


class AddressFields:
    def __init__(self, locators):
        self.first_name = locators.first_name_input
        self.last_name = locators.last_name_input
        self.address = locators.address_input
        self.postcode = locators.postcode_input
        self.city = locators.city_input
        self.phone = locators.phone_input


class AddressLinks:
    def __init__(self, locators):
        self.addresses = locators.addresses_link
        self.edit = locators.edit_link


class OtherElements:
    def __init__(self, locators):
        self.country_select = locators.country_select
        self.message_div = locators.message_div
        self.save_button = locators.save_address_button


class BillingAddressPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.fields = AddressFields(BillingAddressLocators)
        self.links = AddressLinks(BillingAddressLocators)
        self.other_elements = OtherElements(BillingAddressLocators)

    @allure.step("Opening edit billing address")
    def open_edit_billing_address(self):
        self.logger.info("Opening edit billing page")
        self.driver.find_element(*self.links.addresses).click()
        self.driver.find_element(*self.links.edit).click()
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Opening edit billing address",
            attachment_type=AttachmentType.PNG,
        )
        self.logger.info("Opening edit billing page done")

    @allure.step("Setting personal data, first-name: '{first_name}' and last-name: '{last_name}'")
    def set_personal_data(self, first_name, last_name):
        self.logger.info("Setting first name - %s and last name - %s", first_name, last_name)
        self.driver.find_element(*self.fields.first_name).send_keys(first_name)
        self.driver.find_element(*self.fields.last_name).send_keys(last_name)
        self.logger.info("Setting personal data done")

    @allure.step("Selecting country - '{country}'")
    def select_country(self, country):
        self.logger.info("Selecting country - %s", country)
        select = Select(self.driver.find_element(*self.other_elements.country_select))
        select.select_by_visible_text(country)
        self.logger.info("Selecting country done")

    @allure.step("Setting address, street - '{street}', postcode - '{postcode}', city - '{city}'")
    def set_address(self, street, postcode, city):
        self.logger.info("Setting street - %s, postcode - %s, city - %s", street, postcode, city)
        self.driver.find_element(*self.fields.address).send_keys(street)
        self.driver.find_element(*self.fields.postcode).send_keys(postcode)
        self.driver.find_element(*self.fields.city).send_keys(city)
        self.logger.info("Setting address done")

    @allure.step("Selecting phone number - '{number}'")
    def set_phone_number(self, number):
        self.logger.info("Setting phone number - %s", number)
        self.driver.find_element(*self.fields.phone).send_keys(number)
        self.logger.info("Setting phone number done")

    @allure.step("Clicking save address button")
    def save_address(self):
        self.logger.info("Clicking save address button")
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            self.driver.find_element(*self.other_elements.save_button),
        )
        self.driver.find_element(*self.other_elements.save_button).click()
        self.logger.info("Clicking save address button done")

    @allure.step("Getting message text")
    def get_message_text(self):
        self.logger.info("Getting message text")
        return self.driver.find_element(*self.other_elements.message_div).text
