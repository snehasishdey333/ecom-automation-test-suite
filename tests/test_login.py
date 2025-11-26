from selenium.webdriver.common.by import By

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.final import FinalPage
from pages.login_page import LoginPage
from pages.products_page import ProductPage


def test_login(driver):
    login_page=LoginPage(driver)
    login_page.login("standard_user","secret_sauce")




