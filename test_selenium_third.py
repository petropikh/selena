from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def test_my_first():
    #driver = webdriver.Safari()
    #driver = webdriver.Firefox('/Users/petro/Downloads/geckodriver')
    driver = webdriver.Chrome('/Users/petro/Downloads/chromedriver')

    wait = WebDriverWait(driver, 5)

    driver.get('http://127.0.0.1/litecart/admin/')
    login_filed = driver.find_element_by_name('username')
    login_filed.send_keys('admin')
    password_field = driver.find_element_by_name('password')
    password_field.send_keys('admin')
    login_button = driver.find_element_by_xpath('//*[@id="box-login"]/form/div[2]/button')
    login_button.click()

    counter_menu = 1
    while True:
        try:
            el_menu = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="box-apps-menu"]/li['+str(counter_menu)+']')))
            menu = driver.find_element_by_xpath('//*[@id="box-apps-menu"]/li['+str(counter_menu)+']')
            menu.click()
            #time.sleep(1)
            #conuntet_submenu can start from 2 because first submenu loaded by default
            counter_submenu = 1
            while True:
                try:
                    submenu = driver.find_element_by_xpath('//*[@id="box-apps-menu"]/li['+str(counter_menu)+']/ul/li['+str(counter_submenu)+']')
                    submenu.click()
                    #time.sleep(1)
                    counter_submenu = counter_submenu + 1
                except:
                    break
            counter_menu = counter_menu + 1
        except:
            break

    time.sleep(2)
    driver.quit()
