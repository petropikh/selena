from selenium import webdriver
import time

def test_my_first():

    driver = webdriver.Chrome('/Users/petro/Downloads/chromedriver')
    driver.implicitly_wait(5)
    driver.maximize_window()

    driver.get('http://127.0.0.1/litecart/')

    choose_popular = driver.find_element_by_xpath('//*[@id="content"]/ul/li[2]/a')
    choose_popular.click()

    choose_duck = driver.find_element_by_xpath('//*[@id="box-popular-products"]/div/div[1]/div/a/div[1]/img')
    choose_duck.click()
    add_to_cart = driver.find_element_by_class_name('btn-success')
    add_to_cart.click()
    time.sleep(2)
    close = driver.find_element_by_xpath('/html/body/div[2]/div/button')
    close.click()
    cart = driver.find_element_by_class_name('quantity')
    assert cart.text == '1'
    print('Text ' + str(cart.text))

    choose_duck = driver.find_element_by_xpath('//*[@id="box-popular-products"]/div/div[2]/div/a/div[1]/img')
    choose_duck.click()
    add_to_cart = driver.find_element_by_class_name('btn-success')
    add_to_cart.click()
    time.sleep(2)
    close = driver.find_element_by_xpath('/html/body/div[2]/div/button')
    close.click()

    cart = driver.find_element_by_class_name('quantity')
    assert cart.text == '2'
    print('Text ' + str(cart.text))

    choose_duck = driver.find_element_by_xpath('//*[@id="box-popular-products"]/div/div[3]/div/a/div[1]/img')
    choose_duck.click()
    add_to_cart = driver.find_element_by_class_name('btn-success')
    add_to_cart.click()
    time.sleep(2)
    close = driver.find_element_by_xpath('/html/body/div[2]/div/button')
    close.click()

    cart = driver.find_element_by_class_name('quantity')
    assert cart.text == '3'
    print('Text ' + str(cart.text))

    cart_menu = driver.find_element_by_class_name('quantity')
    cart_menu.click()

    table_body_xpath = '//*[@id="box-checkout-cart"]/div/table/tbody'

    table_body = driver.find_element_by_xpath(table_body_xpath)
    elements_in_table = table_body.find_elements_by_class_name('item')

    for i in elements_in_table:
        time.sleep(2)
        driver.find_element_by_name('remove_cart_item').click()
        #print(i)


    time.sleep(5)
    driver.quit()
