from selenium.webdriver.common.by import By


class FinalPage:
    def __init__(self,driver):
        self.driver = driver
    FINISH_BTN=(By.ID,'finish')

    def press_finish_btn(self):
        self.driver.find_element(*self.FINISH_BTN).click()