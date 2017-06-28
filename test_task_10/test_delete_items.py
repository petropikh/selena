import time

def test_delete_items(driver):
    table_body_xpath = '//*[@id="box-checkout-cart"]/div/table/tbody'
    table_body = driver.find_element_by_xpath(table_body_xpath)
    elements_in_table = table_body.find_elements_by_class_name('item')

    for i in elements_in_table:
        time.sleep(2)
        driver.find_element_by_name('remove_cart_item').click()
        #print(i)
