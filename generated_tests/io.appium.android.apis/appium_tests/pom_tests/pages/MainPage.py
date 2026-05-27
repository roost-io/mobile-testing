from appium.webdriver.common.appiumby import AppiumBy
from pages.BasePage import BasePage

class MainPage(BasePage):
    _VIEWS_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Views")')

    def __init__(self, driver):
        super().__init__(driver)

    def is_visible(self):
        return super().is_visible(*self._VIEWS_BUTTON)

    def tap_views(self):
        self.tap(*self._VIEWS_BUTTON)
        from pages.ViewsPage import ViewsPage
        return ViewsPage(self.driver)
