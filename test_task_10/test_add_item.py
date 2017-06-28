import time

def test_add_item(driver):
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