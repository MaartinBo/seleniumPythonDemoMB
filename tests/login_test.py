import allure
import pytest

from pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestLogIn:

    @allure.title("Test for log in that passed")
    def test_log_in_passed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("testeroprogramowaniapython@gmail.com", "testeroprogramowaniapython")
        assert my_account_page.is_logout_link_displayed()

    @allure.title("Test for log in that failed")
    def test_log_in_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("testeroprogramowaniapython@gmail.com1", "testeroprogramowaniapython")

        assert "ERROR: Incorrect username or password." in my_account_page.get_error_msg()
