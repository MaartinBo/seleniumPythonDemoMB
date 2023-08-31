import allure
from selenium.webdriver import Keys
import logging

import locators.locators


class MyAccountPage:
    def __init__(self,driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        # we don't really need to do this in that way, but this way makes it easier to see which locators are used in that
        # pageobject, or we can assume that all locators in locators files are used, and we can reference directly in out methods to these locators,
        self.username_input = locators.locators.MyAccountPage.username_input
        self.password_input = locators.locators.MyAccountPage.password_input
        self.reg_email_input = locators.locators.MyAccountPage.reg_email_input
        self.reg_password_input = locators.locators.MyAccountPage.reg_password
        self.logout_link = locators.locators.MyAccountPage.logout_link
        self.error_msg = locators.locators.MyAccountPage.error_msg

    @allure.step("Login with the username - {1} and password")
    def log_in(self, username, password):
        self.logger.info(f"Log in with the username - {username} and password ")
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.password_input).send_keys(Keys.ENTER)

    @allure.step("Opening myAccountPage")
    def open_page(self):
        self.logger.info("Opening myAccountPage")
        self.driver.get("http://seleniumdemo.com/?page_id=7")

    @allure.step("Creating account with the email - {1} and password ")
    def create_account(self, email, password):
        self.logger.info(f"Creating account with the email - {email} and password")
        self.driver.find_element(*self.reg_email_input).send_keys(email)
        self.driver.find_element(*self.reg_password_input).send_keys(password)
        self.driver.find_element(*self.reg_password_input).send_keys(Keys.ENTER)

    @allure.step("Checking that logout link is displayed")
    def is_logout_link_displayed(self):
        self.logger.info("Checking that logout link is displayed")
        return self.driver.find_element(*self.logout_link).is_displayed()

    @allure.step("Getting error message")
    def get_error_msg(self):
        self.logger.info("Getting error message")
        return self.driver.find_element(*self.error_msg).text