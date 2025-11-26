from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    BACKPACK_PRODUCT_ADD_TO_CART_BUTTON=(By.ID,"add-to-cart-sauce-labs-backpack")
    CART_BUTTON=(By.ID,"shopping_cart_container")

    def add_product_to_cart(self):
        # self.driver.find_element(*self.BACKPACK_PRODUCT_ADD_TO_CART_BUTTON).click()
        self.wait.until(EC.element_to_be_clickable(self.BACKPACK_PRODUCT_ADD_TO_CART_BUTTON)).click()

    def check_cart(self):
        # self.driver.find_element(*self.CART_BUTTON).click()
        self.wait.until(EC.element_to_be_clickable(self.CART_BUTTON)).click()