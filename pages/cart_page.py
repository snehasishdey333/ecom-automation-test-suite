from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self,driver):
        self.driver = driver

    CHECKOUT_BTN=(By.ID,"checkout")
    ITEM_NAME=(By.CLASS_NAME,"inventory_item_name")

    def proceed_to_checkout_page(self):
        self.driver.find_element(*self.CHECKOUT_BTN).click()
