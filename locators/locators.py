from selenium.webdriver.common.by import By


class BillingAddressLocators:
    reg_email_input = (By.ID, "reg_email")
    reg_password_input = (By.ID, "reg_password")
    addresses_link = (By.LINK_TEXT, "Addresses")
    edit_link = (By.XPATH, "//a[contains(@href, 'edit-address/billing/')]")
    first_name_input = (By.ID, "billing_first_name")
    last_name_input = (By.ID, "billing_last_name")
    country_select = (By.ID, "billing_country")
    address_input = (By.ID, "billing_address_1")
    postcode_input = (By.ID, "billing_postcode")
    city_input = (By.ID, "billing_city")
    phone_input = (By.ID, "billing_phone")
    save_address_button = (By.XPATH, "//*[text()='Save address']")
    message_div = (By.XPATH, "//div[@class='woocommerce-message']")

class MyAccountPage:
    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    reg_email_input = (By.ID, "reg_email")
    reg_password = (By.ID, "reg_password")
    my_account_link = (By.XPATH, "//span[text()='My account']")
    error_msg = (By.XPATH, "//ul[@class='woocommerce-error']//li")
    logout_link = (By.LINK_TEXT, "Log out")

class ProductListPage:
    product_price_xpath = "//h2[text()='{}']/ancestor::li//span[@class='woocommerce-Price-amount amount']"
    product_button_xpath = "//h2[text()='"'{}'"']"
    product_next_page_button = (By.PARTIAL_LINK_TEXT, "shop/page/{}")


class ProductPage:
    add_to_cart_button = (By.NAME, "add-to-cart")
    view_cart_button = (By.XPATH, "//div[@class='woocommerce-message']//a[text()='View cart']")

class CartPage:
    proceed_to_checkout_button = (By.PARTIAL_LINK_TEXT, "Proceed to checkout")

class AddressDetailsPage:
    first_name_input = (By.ID, "billing_first_name")
    last_name_input = (By.ID, "billing_last_name")
    company_name_input = (By.ID, "billing_company")
    billing_country_select = (By.ID, "billing_country")
    billing_address_input = (By.ID, "billing_address_1")
    billing_post_code_input = (By.ID, "billing_postcode")
    billing_city_input = (By.ID, "billing_city")
    billing_phone_input = (By.ID, "billing_phone")
    billing_email_input = (By.ID, "billing_email")
    order_comments_input = (By.ID, "order_comments")
    place_order_button = (By.ID, "place_order")

class OrderDetailsPage:
    order_notice = (By.XPATH, "//div[@class='woocommerce-order']//p")
    product_name = (By.XPATH, "//td[contains(@class, 'product-name')]")
