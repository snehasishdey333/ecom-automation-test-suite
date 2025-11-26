from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FinalPage:
    def __init__(self,driver):
        self.driver = driver
    FINISH_BTN=(By.ID,'finish')

    def press_finish_btn(self):
        # self.driver.find_element(*self.FINISH_BTN).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FINISH_BTN)
        ).click()