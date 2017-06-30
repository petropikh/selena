from test_selenium_10.step.cart_page import open_cart_menu

def open_cart(driver):
    try:
        open_cart_menu(driver)
    except:
        raise
        driver.quit()