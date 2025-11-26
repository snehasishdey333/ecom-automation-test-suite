from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self,driver):
        self.driver = driver

    BACKPACK_PRODUCT_ADD_TO_CART_BUTTON=(By.ID,"add-to-cart-sauce-labs-backpack")
    CART_BUTTON=(By.ID,"shopping_cart_container")

    def add_product_to_cart(self):
        self.driver.find_element(*self.BACKPACK_PRODUCT_ADD_TO_CART_BUTTON).click()

    def check_cart(self):
        self.driver.find_element(*self.CART_BUTTON).click()