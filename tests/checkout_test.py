import allure
import pytest

from pages.address_details_page import AddressDetailsPage
from pages.cart_page import CartPage
from pages.order_details_page import OrderDetailsPage
from pages.product_list_page import ProductListPage
from pages.product_page import ProductPage
from utils.excel_reader import ExcelReader


@pytest.mark.usefixtures("setup")
class TestCheckout:

    @pytest.mark.parametrize("product", ExcelReader.get_products_data(2))
    @allure.title("Checkout test with validate price")
    def test_checkout_product(self, product):
        product_list_page = ProductListPage(self.driver)
        product_list_page.open_products_list_page()
        product_list_page.validate_product_actual_price(product.Product, product.ExpectedPrice)
        product_list_page.open_product(product.Product)
        product_page = ProductPage(self.driver)
        product_page.add_product_to_cart()
        product_page.view_cart()
        cart_page = CartPage(self.driver)
        cart_page.open_address_details_page()
        address_details_page = AddressDetailsPage(self.driver)
        address_details_page.fill_address_details("lorem ipsum comments")
        address_details_page.click_order_button_without_ex()
        order_details_page = OrderDetailsPage(self.driver)
        order_notice = order_details_page.get_order_notice()
        expected_notice_msg = "Thank you. Your order has been received."

        assert order_notice.strip() == expected_notice_msg.strip(), f"Expected text '{order_notice}' isn't equal to '{expected_notice_msg}'"

        product_notice = order_details_page.get_product_name()
        assert product.Product.strip() in product_notice.strip(), f"Expected text '{product.Product}' not found in '{product_notice}'"
