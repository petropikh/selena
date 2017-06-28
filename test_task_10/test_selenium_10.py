import time
from selenium import webdriver
from test_task_10 import test_add_item, test_delete_items, test_open_shopping_cart

def test_my_first():

    driver = webdriver.Chrome('/Users/petro/Downloads/chromedriver')
    driver.implicitly_wait(5)
    driver.maximize_window()

    driver.get('http://127.0.0.1/litecart/')

    test_add_item.test_add_item(driver)
    test_open_shopping_cart.test_open_cart(driver)
    test_delete_items.test_delete_items(driver)

    time.sleep(5)
    driver.quit()