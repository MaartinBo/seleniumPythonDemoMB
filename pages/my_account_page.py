from selenium.webdriver import Keys

import locators.locators


class MyAccountPage:
    def __init__(self,driver):
        # we don't really need to do this in that way, but this way makes it easier to see which locators are used in that
        # pageobject, or we can assume that all locators in locators files are used, and we can reference directly in out methods to these locators,
        self.driver = driver
        self.username_input = locators.locators.MyAccountPage.username_input
        self.password_input = locators.locators.MyAccountPage.password_input
        self.reg_email_input = locators.locators.MyAccountPage.reg_email_input
        self.reg_password_input = locators.locators.MyAccountPage.reg_password
        self.logout_link = locators.locators.MyAccountPage.logout_link
        self.error_msg = locators.locators.MyAccountPage.error_msg

    def log_in(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.password_input).send_keys(Keys.ENTER)

    def open_page(self):
        self.driver.get("http://seleniumdemo.com/?page_id=7")

    def create_account(self, email, password):
        self.driver.find_element(*self.reg_email_input).send_keys(email)
        self.driver.find_element(*self.reg_password_input).send_keys(password)
        self.driver.find_element(*self.reg_password_input).send_keys(Keys.ENTER)

    def is_logout_link_displayed(self):
        return self.driver.find_element(*self.logout_link).is_displayed()

    def get_error_msg(self):
        return self.driver.find_element(*self.error_msg).text