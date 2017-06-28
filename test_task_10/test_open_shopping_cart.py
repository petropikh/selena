import time

def test_open_cart(driver):
    cart_menu = driver.find_element_by_class_name('quantity')
    cart_menu.click()
    time.sleep(2)