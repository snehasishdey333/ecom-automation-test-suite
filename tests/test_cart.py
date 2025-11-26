from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.products_page import ProductPage


def test_proceed_to_checkout_page(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    products_page = ProductPage(driver)
    products_page.add_product_to_cart()
    products_page.check_cart()
    cart_page= CartPage(driver)
    cart_page.proceed_to_checkout_page()