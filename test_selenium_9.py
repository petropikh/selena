from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os

def test_my_first():

    class ScreenshotListener(AbstractEventListener):
        def on_exception(self, exception, driver):
            print(driver.get_log("browser"))
            screenshot_name = "exception_{}.png".format(time.strftime("%H_%M_%S"))
            driver.get_screenshot_as_file(os.path.abspath(os.curdir) + screenshot_name)
            print("Screenshot saved as '%s'" % screenshot_name)
        def before_find(self, by, value, driver):
            print(driver.get_log("browser"))
            print('DEBUG BEFORE')
            print(by, value)

        def after_find(self, by, value, driver):
            print('DEBUG AFTER')
            print(driver.get_log("browser"))
            print(by, value)

    driver = EventFiringWebDriver(webdriver.Chrome('/Users/petro/Downloads/chromedriver'), ScreenshotListener())
    driver.implicitly_wait(5)

    driver.get('http://127.0.0.1/litecart/admin/')
    login_field = driver.find_element_by_name('usernamee')
    login_field.send_keys('admin')
    password_field = driver.find_element_by_name('password')
    password_field.send_keys('admin')
    login_button = driver.find_element_by_xpath('//*[@id="box-login"]/form/div[2]/button')
    login_button.click()

    i = 0
    len_menu = len(driver.find_elements_by_xpath(".//*[@id='box-apps-menu']/li"))

    while i < len_menu:
        i += 1
        xpath = ".//*[@id='box-apps-menu']/li[{}]".format(i)
        driver.find_element_by_xpath(xpath).click()
        assert len(driver.find_elements_by_tag_name('h1')) != 0

        len_submenu = len(driver.find_elements_by_xpath(".//*[@id='box-apps-menu']/li[{}]/ul/li".format(i)))

        x = 0
        while x < len_submenu:
            x += 1
            try:
                driver.find_element_by_xpath('//*[@id="box-apps-menu"]/li[' + str(i) + ']/ul/li[' + str(x) + ']').click()
                assert len(driver.find_elements_by_tag_name('h1')) != 0
            except:
                pass

    driver.quit()
