from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def main_page_open(driver):
    try:
        driver.get('http://127.0.0.1/litecart/')
        driver.find_element_by_xpath('//*[@id="content"]/ul/li[2]/a').click()
    except:
        raise
        driver.quit()

def click_on_item(driver, wait, path):
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, path)))
        driver.find_element_by_xpath(path).click()
    except:
        raise
        driver.quit()

def click_buy(driver, wait):
    try:
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-success')))
        driver.find_element_by_class_name('btn-success').click()
    except:
        raise
        driver.quit()

def click_close_item(driver, wait):
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/button')))
        driver.find_element_by_xpath('/html/body/div[2]/div/button').click()
    except:
        raise
        driver.quit()

def check_items_in_cart(driver, wait, expected_items):
    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'quantity')))
        cart = driver.find_element_by_class_name('quantity')
        assert cart.text == expected_items
        print('\n Text from assert ' + str(cart.text))
    except:
        raise
        driver.quit()