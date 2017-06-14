from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def test_my_first():
    #driver = webdriver.Safari()
    #driver = webdriver.Firefox()
    driver = webdriver.Chrome('/Users/petro/Downloads/chromedriver')

    #wait = WebDriverWait(driver, 10)

    driver.get('http://127.0.0.1/litecart/admin/')
    login_filed = driver.find_element_by_name('username')
    login_filed.send_keys('admin')
    password_field = driver.find_element_by_name('password')
    password_field.send_keys('admin')
    login_button = driver.find_element_by_xpath('//*[@id="box-login"]/form/div[2]/button')
    login_button.click()

    appearance_menu = WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#app- > a > span.name')))
    appearance_menu = driver.find_element_by_css_selector('#app- > a > span.name')
    appearance_menu.click()


    logotype = WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#doc-logotype > a > span')))
    logotype = driver.find_element_by_css_selector('#doc-logotype > a > span')
    logotype.click()

    #driver.get('http://127.0.0.1/litecart/admin/')
    #HERE SLENIUM CLICKS ON FIRST MENU(I DO NOT KNOW WHY)
    catalog = WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#app- > a > span.name')))
    catalog = driver.find_element_by_css_selector('#app- > a > span.name')
    catalog.click()

    prod_group = WebDriverWait(driver, 5).until(ec.element_to_be_clickable(By.CSS_SELECTOR, '#doc-product_groups > a > span'))
    prod_group = driver.find_element_by_css_selector('#doc-product_groups > a > span')
    prod_group.click()

    time.sleep(2)
    driver.quit()
