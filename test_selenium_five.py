from selenium import webdriver
import time

def test_five():
    #driver = webdriver.Safari()
    #driver = webdriver.Firefox('/Users/petro/Downloads/geckodriver')
    driver = webdriver.Chrome('/Users/petro/Downloads/chromedriver')
    driver.implicitly_wait(5)

    driver.get('http://localhost/litecart')
    main_name = driver.find_element_by_class_name('name').text
    main_price_regular = driver.find_element_by_class_name('regular-price').text
    main_price_regular_strike_color = driver.find_element_by_class_name('regular-price').value_of_css_property('text-decoration')
    main_price_discount = driver.find_element_by_class_name('campaign-price').text
    main_price_discount_color = driver.find_element_by_class_name('campaign-price').value_of_css_property('color')
    main_price_discount_bold = driver.find_element_by_class_name('campaign-price').value_of_css_property('font-weight')

    item = driver.find_element_by_xpath('//*[@id="box-campaign-products"]/div/div/div/a')
    item.click()

    item_name = driver.find_element_by_tag_name('h1').text
    item_price_regular = driver.find_element_by_class_name('regular-price').text
    item_price_regular_strike_color = driver.find_element_by_class_name('regular-price').value_of_css_property('text-decoration')
    item_price_discount = driver.find_element_by_class_name('campaign-price').text
    item_price_discount_color = driver.find_element_by_class_name('campaign-price').value_of_css_property('color')
    item_price_discount_bold = driver.find_element_by_class_name('campaign-price').value_of_css_property('font-weight')

    assert main_name == item_name
    assert main_price_regular == item_price_regular
    assert main_price_discount == item_price_discount
    assert main_price_regular_strike_color == item_price_regular_strike_color == 'line-through solid rgb(51, 51, 51)'
    assert item_price_discount_color == main_price_discount_color == 'rgba(204, 0, 0, 1)'
    assert main_price_discount_bold == item_price_discount_bold == 'bold'

    print('Color is ' + item_price_discount_bold)

    time.sleep(2)
    driver.quit()