from selenium import webdriver

def test_my_first():
    driver = webdriver.Safari()
    #driver = webdriver.Firefox()
    #driver = webdriver.Chrome()

    driver.get('https://google.com')
    driver.quit()
    
