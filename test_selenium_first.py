from selenium import webdriver
import time

def test_my_first():
    driver = webdriver.Safari()
    #driver = webdriver.Firefox()
    #driver = webdriver.Chrome()

    driver.get('https://google.com')
    time.sleep(2)
    driver.quit()
