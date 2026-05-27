from appium.webdriver.common.appiumby import AppiumBy
from pages.BasePage import BasePage

class ButtonsPage(BasePage):
    _TOGGLE_BUTTON = (AppiumBy.ID, "io.appium.android.apis:id/button_toggle")

    def __init__(self, driver):
        super().__init__(driver)

    def is_visible(self):
        return super().is_visible(*self._TOGGLE_BUTTON)

    def get_toggle_text(self):
        return self.get_text(*self._TOGGLE_BUTTON)

    def tap_toggle_button(self):
        self.tap(*self._TOGGLE_BUTTON)
        return self

    def go_back(self):
        self.back()
        from pages.ViewsPage import ViewsPage
        return ViewsPage(self.driver)
