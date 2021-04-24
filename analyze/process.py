import time
from selenium import webdriver, common
from selenium.common.exceptions import WebDriverException


class AnalyzeScreenshot:

    def __init__(self):
        pass

    @staticmethod
    def screenshot(url, file_name, timestamp):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--enable-popup-blocking")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument('--allow-running-insecure-content')
        options.headless = True
        print("headless set")
        driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
        print("getting url")
        time.sleep(1)
        try:
            driver.get(url)
        except WebDriverException:
            print("page down")
            pass

        print("url gotten")
        time.sleep(6)
        driver.execute_script("return window.stop")     # Pause the page loading
        try:
            driver.find_element_by_name('//button[text()="Sí"]').click()
            #driver.find_element_by_xpath('//*[@id="age-gate"]/button[2]').click()
        except common.exceptions.NoSuchElementException:
            pass
            print("Can not click age validation")

        try:
            driver.find_element_by_class_name('accept-cookies-button').click()
        except common.exceptions.NoSuchElementException:
            pass

        total_height = driver.execute_script("return document.body.scrollHeight")
        print(f'total height of page is {total_height}')
        print("setting")
        driver.set_window_size(1920, total_height)
        print("setted")
        time.sleep(4)
        print("take screenshot")
        if file_name == '':

            driver.save_screenshot(f"screenshots/home_{timestamp}.png")
        else:
            driver.save_screenshot(f"screenshots/{file_name}_{timestamp}.png")

