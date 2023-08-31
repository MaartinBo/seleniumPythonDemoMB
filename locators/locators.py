from selenium.webdriver.common.by import By


class BillingAddressLocators:
    reg_email_input = (By.ID, "reg_email")
    reg_password_input = (By.ID, "reg_password")
    addresses_link = (By.LINK_TEXT, "Addresses")
    edit_link = (By.LINK_TEXT, "Edit")
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
    logout_link = (By.LINK_TEXT, "Logout")


    #
    #
    # driver.find_element(By.XPATH, "//span[text()='My account']").click()
    #
    #
    # driver.get("http://seleniumdemo.com/?page_id=7")
    # driver.find_element(By.ID, "reg_email").send_keys("testeroprogramowaniapython@gmail.com")
    # driver.find_element(By.ID, "reg_password").send_keys("testeroprogramowaniapython")
    # driver.find_element(By.ID, "reg_password").send_keys(Keys.ENTER)
    # msg = "An account is already registered with your email address. Please log in."
    # assert msg in driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']//li").text