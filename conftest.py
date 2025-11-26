import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    # options = Options()
    # options.add_experimental_option("detach", True)
    # options.add_experimental_option("prefs", {
    #     "credentials_enable_service": False,
    #     "profile.password_manager_enabled": False
    # })
    #
    # options.add_argument("--disable-features=PasswordLeakDetection,PasswordManagerUI")
    #
    # driver = webdriver.Chrome(options=options)
    # driver.get("https://www.saucedemo.com/")
    # yield driver
    # driver.quit()
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
