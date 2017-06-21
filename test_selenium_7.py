from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def test_my_first():
    #driver = webdriver.Safari()
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    #wait = WebDriverWait(driver, 5)
    driver.maximize_window()

    driver.get('http://127.0.0.1/litecart/')

    counter = 1

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

    remove = driver.find_elements_by_class_name('btn-danger')
    for i in remove:
        time.sleep(3)
        print(str(i))
        i.click()


    time.sleep(2)
    driver.quit()
