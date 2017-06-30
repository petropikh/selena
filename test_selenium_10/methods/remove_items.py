from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from test_selenium_10.step.cart_page import find_elements_in_cart

def rm_items(driver, wait):
    try:
        for i in find_elements_in_cart(driver,wait):
            wait.until(EC.element_to_be_clickable((By.NAME, 'remove_cart_item')))
            driver.find_element_by_name('remove_cart_item').click()
    except:
        raise
        driver.quit()