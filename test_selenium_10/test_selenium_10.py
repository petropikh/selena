from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from test_selenium_10.methods.add_item_to_cart import add_item
from test_selenium_10.methods.open_cart_menu import open_cart
from test_selenium_10.methods.remove_items import rm_items
import time

def test_10():
    driver = webdriver.Firefox()
    driver.maximize_window()
    wait = WebDriverWait(driver, 5)

    add_item(driver, wait)
    open_cart(driver)
    rm_items(driver, wait)

    time.sleep(2)
    driver.quit()