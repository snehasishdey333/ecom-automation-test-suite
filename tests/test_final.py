from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.final import FinalPage
from pages.login_page import LoginPage
from pages.products_page import ProductPage
from tests.test_cart import test_proceed_to_checkout_page
from tests.test_checkout import test_click_checkout


def test_press_finish_btn(driver):
    test_click_checkout(driver)
    final_page = FinalPage(driver)
    final_page.press_finish_btn()