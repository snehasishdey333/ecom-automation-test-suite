from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    FIRST_NAME = (By.ID,'first-name')
    LAST_NAME = (By.ID, 'last-name')
    ZIP = (By.ID, 'postal-code')
    CONTINUE_BTN=(By.ID, 'continue')

    def click_checkout(self,f_name,l_name,zip_code):
        self.driver.find_element(*self.FIRST_NAME).send_keys(f_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(l_name)
        self.driver.find_element(*self.ZIP).send_keys(zip_code)
        # self.driver.find_element(*self.CONTINUE_BTN).click()
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BTN)).click()

        # self.driver.find_element(*self.USERNAME).send_keys(username)
        # self.driver.find_element(*self.PASSWORD).send_keys(password)
        # self.driver.find_element(*self.LOGIN_BTN).click()