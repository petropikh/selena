from test_selenium_10.step.main_page import main_page_open, click_on_item, click_buy, click_close_item, check_items_in_cart
from test_selenium_10.configs.items_xpath import items_xpaths

def add_item(driver, wait):
    try:
        main_page_open(driver)
        item_counter = 0
        for path in items_xpaths:
            click_on_item(driver, wait, str(path))
            click_buy(driver, wait)
            click_close_item(driver, wait)
            item_counter += 1
            check_items_in_cart(driver, wait, str(item_counter))
    except:
        raise
        driver.quit()