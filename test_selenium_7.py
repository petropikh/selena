
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_my_first():
    driver = webdriver.Firefox()
    #driver.implicitly_wait(5)
    driver.maximize_window()
    wait = WebDriverWait(driver, 5)

    driver.get('http://127.0.0.1/litecart/')

    choose_popular = driver.find_element_by_xpath('//*[@id="content"]/ul/li[2]/a')
    choose_popular.click()

    def add_item_to_cart(path):
        wait.until(EC.element_to_be_clickable((By.XPATH, path)))
        choose_duck = driver.find_element_by_xpath(path)
        choose_duck.click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-success')))
        add_to_cart = driver.find_element_by_class_name('btn-success')
        add_to_cart.click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/button')))
        close = driver.find_element_by_xpath('/html/body/div[2]/div/button')
        close.click()

    def check_items_in_cart(expected_items):
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'quantity')))
        cart = driver.find_element_by_class_name('quantity')
        assert cart.text == expected_items
        print('Text from assert ' + str(cart.text))

    items_xpath = ['//*[@id="box-popular-products"]/div/div[1]/div/a/div[1]/img',
    '//*[@id="box-popular-products"]/div/div[2]/div/a/div[1]/img',
    '//*[@id="box-popular-products"]/div/div[3]/div/a/div[1]/img']


    item_counter = 0
    for i in items_xpath:
        add_item_to_cart(str(i))
        item_counter += 1
        check_items_in_cart(str(item_counter))

    cart_menu = driver.find_element_by_class_name('quantity')
    cart_menu.click()


    table_body_xpath = '//*[@id="box-checkout-cart"]/div/table/tbody'
    wait.until(EC.element_to_be_clickable((By.XPATH, table_body_xpath)))

    table_body = driver.find_element_by_xpath(table_body_xpath)
    elements_in_table = table_body.find_elements_by_class_name('item')

    for y in elements_in_table:
        wait.until(EC.element_to_be_clickable((By.NAME, 'remove_cart_item')))
        driver.find_element_by_name('remove_cart_item').click()

    driver.quit()
