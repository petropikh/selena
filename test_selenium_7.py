from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_my_first():

    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    wait = WebDriverWait(driver, 5)

    driver.get('http://127.0.0.1/litecart/')

    choose_popular = driver.find_element_by_xpath('//*[@id="content"]/ul/li[2]/a')
    choose_popular.click()

    choose_duck = driver.find_element_by_xpath('//*[@id="box-popular-products"]/div/div[1]/div/a/div[1]/img')
    choose_duck.click()
    add_to_cart = driver.find_element_by_class_name('btn-success')
    add_to_cart.click()
    close = driver.find_element_by_xpath('/html/body/div[2]/div/button')
    close.click()
    w1 = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'quantity')))
    cart = driver.find_element_by_class_name('quantity')
    assert cart.text == '1'
    print('Text from case 1 ' + str(cart.text))

    choose_duck = driver.find_element_by_xpath('//*[@id="box-popular-products"]/div/div[2]/div/a/div[1]/img')
    choose_duck.click()
    add_to_cart = driver.find_element_by_class_name('btn-success')
    add_to_cart.click()
    close = driver.find_element_by_xpath('/html/body/div[2]/div/button')
    close.click()
    w2 = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'quantity')))
    cart = driver.find_element_by_class_name('quantity')
    assert cart.text == '2'
    print('Text from case 2 ' + str(cart.text))

    choose_duck = driver.find_element_by_xpath('//*[@id="box-popular-products"]/div/div[3]/div/a/div[1]/img')
    choose_duck.click()
    add_to_cart = driver.find_element_by_class_name('btn-success')
    add_to_cart.click()
    close = driver.find_element_by_xpath('/html/body/div[2]/div/button')
    close.click()
    w3 = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'quantity')))
    cart = driver.find_element_by_class_name('quantity')
    assert cart.text == '3'
    print('Text from case 3 ' + str(cart.text))

    cart_menu = driver.find_element_by_class_name('quantity')
    cart_menu.click()

    table_body_xpath = '//*[@id="box-checkout-cart"]/div/table/tbody'

    table_body = driver.find_element_by_xpath(table_body_xpath)
    elements_in_table = table_body.find_elements_by_class_name('item')

    for i in elements_in_table:
        wait.until(EC.element_to_be_clickable((By.NAME, 'remove_cart_item')))
        driver.find_element_by_name('remove_cart_item').click()
        print(i)


    driver.quit()
