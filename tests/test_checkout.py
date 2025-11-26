from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.products_page import ProductPage


def test_click_checkout(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    products_page = ProductPage(driver)
    products_page.add_product_to_cart()
    products_page.check_cart()
    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout_page()
    checkout_page = CheckoutPage(driver)
    checkout_page.click_checkout("Snehasish",'Dey',"735204")