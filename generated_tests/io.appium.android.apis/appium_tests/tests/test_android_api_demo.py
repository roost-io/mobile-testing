import pytest
import os
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_views_navigation_and_toggle_button(driver):
    wait = WebDriverWait(driver, 15)

    print("Step 1: Launch the ApiDemos application")
    # App is launched automatically by the fixture session initialization
    
    print("Step 2: Tap on 'Views' to access the list of UI element demonstrations")
    views_element = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Views")')
        )
    )
    views_element.click()

    print("Step 3: Tap on 'Buttons' option in the Views menu")
    buttons_element = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Buttons")')
        )
    )
    buttons_element.click()

    print("Step 4: Interact with and toggle the state of the Toggle Button")
    # Find the toggle button using its ID (highest confidence from Step 4 selectors list)
    toggle_button = wait.until(
        EC.presence_of_element_located(
            (AppiumBy.ID, "io.appium.android.apis:id/button_toggle")
        )
    )
    
    # Verify initial state is "OFF"
    initial_text = toggle_button.text
    print(f"Initial button state is: {initial_text}")
    assert initial_text == "OFF", f"Expected button state to be 'OFF' initially, but got '{initial_text}'"
    
    # Tap to toggle state
    toggle_button.click()
    
    # Verify state changes to "ON"
    updated_text = toggle_button.text
    print(f"Updated button state is: {updated_text}")
    assert updated_text == "ON", f"Expected button state to be 'ON' after tap, but got '{updated_text}'"

    print("Step 5: Navigate back to the Views list")
    driver.back()
    
    # Verify we are back on the Views menu by checking for "Buttons" element availability
    wait.until(
        EC.presence_of_element_located(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Buttons")')
        )
    )

    print("Step 6: Navigate back to the main menu screen of ApiDemos")
    driver.back()
    
    # Verify we are back on the main screen by checking for "Views" element availability
    wait.until(
        EC.presence_of_element_located(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Views")')
        )
    )
    print("Test workflow executed successfully!")
