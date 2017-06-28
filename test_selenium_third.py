from selenium import webdriver

def test_my_first():
    #driver = webdriver.Safari()
    #driver = webdriver.Firefox('/Users/petro/Downloads/geckodriver')
    driver = webdriver.Chrome('/Users/petro/Downloads/chromedriver')
    driver.implicitly_wait(5)

    driver.get('http://127.0.0.1/litecart/admin/')
    login_field = driver.find_element_by_name('username')
    login_field.send_keys('admin')
    password_field = driver.find_element_by_name('password')
    password_field.send_keys('admin')
    login_button = driver.find_element_by_xpath('//*[@id="box-login"]/form/div[2]/button')
    login_button.click()

    i = 0
    len_menu = len(driver.find_elements_by_xpath(".//*[@id='box-apps-menu']/li"))

    while i < len_menu:
        driver.implicitly_wait(0)
        i += 1
        xpath = ".//*[@id='box-apps-menu']/li[{}]".format(i)
        driver.find_element_by_xpath(xpath).click()
        assert len(driver.find_elements_by_tag_name('h1')) != 0

        len_submenu = len(driver.find_elements_by_xpath(".//*[@id='box-apps-menu']/li[{}]/ul/li".format(i)))
        driver.implicitly_wait(5)

        x = 0
        while x < len_submenu:
            x += 1
            print('DEBUG :' + str(len_submenu))
            try:
                driver.find_element_by_xpath('//*[@id="box-apps-menu"]/li[' + str(i) + ']/ul/li[' + str(x) + ']').click()
                assert len(driver.find_elements_by_tag_name('h1')) != 0
            except:
                pass

    driver.quit()
