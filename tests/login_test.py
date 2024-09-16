import allure
import pytest

from pages.my_account_page_unregistered import MyAccountPage

pytestmark = [pytest.mark.login, pytest.mark.smoke]


@pytest.mark.usefixtures("setup")
class TestLogIn:
    driver = None

    @allure.title("Test for log in that passed")
    def test_log_in_passed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("test-qa-orginal@gmail.com", "#@!Test123#@!")
        assert my_account_page.is_logout_link_displayed()

    @allure.title("Test for log in that failed")
    def test_log_in_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("test-qa-orginal@gmail.com", "test")

        assert (
            "The password you entered for the email address test-qa-orginal@gmail.com is incorrect"
            in my_account_page.get_error_msg()
        )
