from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def test_my_first():
    #driver = webdriver.Safari()
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    driver.maximize_window()

    driver.get('http://127.0.0.1/litecart//admin')
    login_filed = driver.find_element_by_name('username')
    login_filed.send_keys('admin')
    password_field = driver.find_element_by_name('password')
    password_field.send_keys('admin')
    password_field.send_keys(Keys.RETURN)

    catalog = driver.find_elements_by_xpath('//*[@id="app-"]/a')
    catalog[2].click()

    add_new = driver.find_element_by_css_selector('#main > ul > li > a')
    add_new.click()

    link = driver.find_elements_by_class_name('fa-external-link')
    for i in link:
        i.click()

    time.sleep(2)
    driver.quit()
