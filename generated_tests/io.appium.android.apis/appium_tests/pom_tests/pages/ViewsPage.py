from appium.webdriver.common.appiumby import AppiumBy
from pages.BasePage import BasePage

class ViewsPage(BasePage):
    _BUTTONS_OPTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Buttons")')

    def __init__(self, driver):
        super().__init__(driver)

    def is_visible(self):
        return super().is_visible(*self._BUTTONS_OPTION)

    def tap_buttons(self):
        self.tap(*self._BUTTONS_OPTION)
        from pages.ButtonsPage import ButtonsPage
        return ButtonsPage(self.driver)

    def go_back_to_main(self):
        self.back()
        from pages.MainPage import MainPage
        return MainPage(self.driver)
