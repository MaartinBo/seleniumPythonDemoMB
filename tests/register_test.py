import random

import allure
import pytest

from pages.my_account_page_unregistered import MyAccountPage
from utils.generic_utils import generate_random_email_and_password


@pytest.mark.usefixtures("setup")
@pytest.mark.register
class TestCreateAccount:
    @allure.title("Test for create account that failed")
    def test_create_account_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account("test-qa-orginal@gmail.com", "abcCba123321!@#")

        msg = "An account is already registered with your email address. Please log in."
        assert msg in my_account_page.get_error_msg()

    @allure.title("Test for create account that passed")
    def test_create_account_passed(self):
        rand_info = generate_random_email_and_password()
        email = rand_info['email']
        password = rand_info['password']
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, password)

        assert my_account_page.is_logout_link_displayed()
