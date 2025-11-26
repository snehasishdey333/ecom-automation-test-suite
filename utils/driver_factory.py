# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# from pages.cart_page import CartPage
# from pages.checkout_page import CheckoutPage
# from pages.final import FinalPage
# from pages.login_page import LoginPage
# from pages.products_page import ProductPage
#
#
# # def create_driver():
#
# options=Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
# driver.get("https://www.saucedemo.com/")
# driver.implicitly_wait(5)
# # yield driver
#
# login_page = LoginPage(driver)
# login_page.login("standard_user", "secret_sauce")
#
# products_page = ProductPage(driver)
# products_page.add_product_to_cart()
# products_page.check_cart()
#
# cart_page = CartPage(driver)
# cart_page.proceed_to_checkout_page()
#
# checkout_page = CheckoutPage(driver)
# checkout_page.click_checkout("john","cena","735204")
#
# final_page = FinalPage(driver)
# final_page.press_finish_btn()
#
# driver.quit()
#
# # create_driver()
#
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.final import FinalPage
from pages.login_page import LoginPage
from pages.products_page import ProductPage


# def run_test():
#     options = Options()
#     options.add_experimental_option("detach", True)
#     options.add_experimental_option("prefs", {
#         "credentials_enable_service": False,
#         "profile.password_manager_enabled": False
#     })
#
#     options.add_argument("--disable-features=PasswordLeakDetection,PasswordManagerUI")
#
#     driver = webdriver.Chrome(options=options)
#     time.sleep(2)
#     driver.get("https://www.saucedemo.com/")
#     time.sleep(2)
#     driver.implicitly_wait(5)
#
#     login_page = LoginPage(driver)
#     login_page.login("standard_user", "secret_sauce")
#     time.sleep(2)
#
#     products_page = ProductPage(driver)
#     products_page.add_product_to_cart()
#     products_page.check_cart()
#     time.sleep(2)
#
#     cart_page = CartPage(driver)
#     cart_page.proceed_to_checkout_page()
#     time.sleep(2)
#
#     checkout_page = CheckoutPage(driver)
#     checkout_page.click_checkout("john", "cena", "735204")
#     time.sleep(2)
#
#     final_page = FinalPage(driver)
#     final_page.press_finish_btn()
#     time.sleep(2)
#
#     # driver.quit()
#
#
# if __name__ == "__main__":
#     run_test()

@pytest.fixture
def driver():
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
    })

    options.add_argument("--disable-features=PasswordLeakDetection,PasswordManagerUI")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()