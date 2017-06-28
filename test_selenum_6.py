from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import os

def test_my_first():
    #driver = webdriver.Safari()
    driver = webdriver.Chrome('/Users/petro/Downloads/chromedriver')
    driver.implicitly_wait(5)

    driver.maximize_window()

    driver.get('http://127.0.0.1/litecart//admin')
    login_filed = driver.find_element_by_name('username')
    login_filed.send_keys('admin')
    password_field = driver.find_element_by_name('password')
    password_field.send_keys('admin')
    password_field.send_keys(Keys.RETURN)

    catalog = driver.find_elements_by_xpath('//*[@id="app-"]/a')
    catalog[1].click()

    add_new = driver.find_element_by_css_selector('#main > ul > li:nth-child(3) > a')
    add_new.click()

    enable = driver.find_element_by_class_name('btn-default')
    enable.click()

    category = driver.find_elements_by_name('categories[]')
    category[0].click()
    category[1].click()

    code = driver.find_element_by_name('code')
    code.send_keys('12345')

    name = driver.find_element_by_name('name[en]')
    name.send_keys('some new item')

    sku = driver.find_element_by_name('sku')
    sku.send_keys('12345')

    gtin = driver.find_element_by_name('gtin')
    gtin.send_keys('12345')

    taric = driver.find_element_by_name('taric')
    taric.send_keys('12345')

    quantity = driver.find_element_by_name('quantity')
    quantity.send_keys('2')

    group = driver.find_element_by_name('product_groups[]')
    group.click()

    valid = driver.find_element_by_name('date_valid_from')
    valid.send_keys('5152017')

    valid_to = driver.find_element_by_name('date_valid_to')
    valid_to.send_keys('5252018')

    weight = driver.find_element_by_name('weight')
    weight.send_keys('2')

    width = driver.find_element_by_name('dim_x')
    width.send_keys('11')

    height = driver.find_element_by_name('dim_y')
    height.send_keys('15')

    length = driver.find_element_by_name('dim_z')
    length.send_keys('25')

    image = driver.find_element_by_name('new_images[]')
    image.send_keys(os.path.abspath(os.curdir) + '/car.jpg')

    information = driver.find_element_by_xpath('//*[@id="main"]/form/div/ul/li[2]/a')
    information.click()

    key = driver.find_element_by_name('keywords')
    key.send_keys('some keywords here')

    description = driver.find_element_by_name('short_description[en]')
    description.send_keys('there are short description')

    desc = driver.find_element_by_xpath('//*[@id="tab-information"]/div[4]/div/div/div/div[2]')
    desc.send_keys('there are full description')

    attr = driver.find_element_by_name('attributes[en]')
    attr.send_keys('there are attributes')

    title = driver.find_element_by_name('head_title[en]')
    title.send_keys('title here')

    meta = driver.find_element_by_name('meta_description[en]')
    meta.send_keys('meta descr here')

    prices = driver.find_element_by_xpath('//*[@id="main"]/form/div/ul/li[3]/a')
    prices.click()

    price = driver.find_element_by_name('purchase_price')
    price.send_keys('25')

    currency = driver.find_element_by_name('purchase_price_currency_code')
    currency.send_keys('Euros')

    price_usd = driver.find_element_by_name('prices[USD]')
    price_usd.send_keys('30')

    price_eur = driver.find_element_by_name('prices[EUR]')
    price_eur.send_keys('28')

    tax = driver.find_element_by_name('gross_prices[USD]')
    tax.send_keys('30')

    save = driver.find_element_by_name('save')
    save.click()

    check = driver.find_element_by_link_text('some new item')
    check.click()

    time.sleep(2)
    driver.quit()
