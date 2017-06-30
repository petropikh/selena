from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def find_elements_in_cart(driver, wait):
    try:
        table_body_xpath = '//*[@id="box-checkout-cart"]/div/table/tbody'
        wait.until(EC.element_to_be_clickable((By.XPATH, table_body_xpath)))
        table_body = driver.find_element_by_xpath(table_body_xpath)
        elements_in_table = table_body.find_elements_by_class_name('item')
        return elements_in_table
    except:
        raise
        driver.quit()

def open_cart_menu(driver):
    try:
        driver.find_element_by_class_name('quantity').click()
    except:
        raise
        driver.quit()