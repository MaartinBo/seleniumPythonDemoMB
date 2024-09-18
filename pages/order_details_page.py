import logging

import locators.locators


class OrderDetailsPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.order_notice = locators.locators.OrderDetailsPage.order_notice
        self.product_name = locators.locators.OrderDetailsPage.product_name

    def get_product_name(self):
        product = self.driver.find_element(*self.product_name)
        product_text = product.get_attribute("textContent")
        return product_text

    def get_order_notice(self):
        notice = self.driver.find_element(*self.order_notice)
        notice_text = notice.get_attribute("textContent")
        return notice_text
