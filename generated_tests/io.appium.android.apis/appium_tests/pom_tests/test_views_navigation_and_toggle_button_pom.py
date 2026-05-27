import pytest
from pages.MainPage import MainPage

def test_views_navigation_and_toggle_button(driver):
    print("Step 1: Launch the ApiDemos application and initialize main page")
    main_page = MainPage(driver)
    assert main_page.is_visible(), "Main menu screen containing API demos list should be visible"

    print("Step 2: Tap on 'Views' to access the list of UI element demonstrations")
    views_page = main_page.tap_views()
    assert views_page.is_visible(), "Views submenu list should be displayed"

    print("Step 3: Tap on 'Buttons' option in the Views menu")
    buttons_page = views_page.tap_buttons()
    assert buttons_page.is_visible(), "Buttons view containing interactive buttons should be visible"

    # Get initial toggle button text
    initial_state = buttons_page.get_toggle_text()
    print(f"Initial toggle state: {initial_state}")
    assert initial_state == "OFF", "Initially, the Toggle button state should be OFF"

    print("Step 4: Tap on the Toggle Button to change state")
    buttons_page.tap_toggle_button()
    
    # Verify state transition
    new_state = buttons_page.get_toggle_text()
    print(f"Updated toggle state: {new_state}")
    assert new_state == "ON", "Toggle button state should transition from OFF to ON"

    print("Step 5: Navigate back to the Views list")
    views_page = buttons_page.go_back()
    assert views_page.is_visible(), "Views submenu list should be displayed after backing out"

    print("Step 6: Navigate back to the main menu screen of ApiDemos")
    main_page = views_page.go_back_to_main()
    assert main_page.is_visible(), "Main API demos screen containing primary list should be visible"
