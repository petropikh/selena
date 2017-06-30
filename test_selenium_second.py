from selenium import webdriver

def test_my_first():
    driver = webdriver.Safari()
    #driver = webdriver.Firefox()
    #driver = webdriver.Chrome()


    driver.get('http://127.0.0.1:8000/admin/')
    login_filed = driver.find_element_by_name('username')
    login_filed.send_keys('admin')
    password_field = driver.find_element_by_name('password')
    password_field.send_keys('admin')
    login_button = driver.find_element_by_class_name('btn btn-default')
    login_button.click()

    driver.quit()
