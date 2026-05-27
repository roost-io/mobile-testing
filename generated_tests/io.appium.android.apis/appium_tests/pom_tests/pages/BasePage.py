from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=10):
        return WebDriverWait(self.driver, timeout)

    def find(self, by, value, timeout=10):
        return self.wait(timeout).until(EC.presence_of_element_located((by, value)))

    def tap(self, by, value, timeout=10):
        element = self.wait(timeout).until(EC.element_to_be_clickable((by, value)))
        element.click()
        return self

    def type_text(self, by, value, text, timeout=10):
        element = self.find(by, value, timeout)
        element.clear()
        element.send_keys(text)
        return self

    def is_visible(self, by, value, timeout=5):
        try:
            self.wait(timeout).until(EC.visibility_of_element_located((by, value)))
            return True
        except Exception:
            return False

    def get_text(self, by, value, timeout=10):
        element = self.find(by, value, timeout)
        return element.text

    def back(self):
        self.driver.back()
        return self
