from pages.login_page import LoginPage
from pages.products_page import ProductPage


def test_add_product_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user","secret_sauce")
    products_page = ProductPage(driver)
    products_page.add_product_to_cart()


def test_check_cart(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    products_page = ProductPage(driver)
    products_page.add_product_to_cart()
    products_page.check_cart()