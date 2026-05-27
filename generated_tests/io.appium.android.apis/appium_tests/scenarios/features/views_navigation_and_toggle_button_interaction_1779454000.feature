@android @critical @views @buttons
Feature: Views Navigation and Toggle Button Interaction

  As an app developer,
  I want to verify that UI buttons, particularly Toggle Buttons, successfully register click events and change state,
  So that user input works reliably within the ApiDemos application.

  Background:
    Given I am on the homepage 'io.appium.android.apis'
    Then the main API list should be visible on the screen
    And the list item 'Views' should be visible

  @e2e_business_workflow
  Scenario: Verify navigation to Buttons view and toggle state transition
    When I tap on the 'Views' list item
    Then the 'Views' submenu screen should be displayed
    And the list item 'Buttons' should be visible

    When I tap on the 'Buttons' list item
    Then the 'Buttons' view screen should be displayed
    And the toggle button with ID 'io.appium.android.apis:id/button_toggle' should display the text 'OFF'

    When I tap the toggle button with ID 'io.appium.android.apis:id/button_toggle'
    Then the toggle button with ID 'io.appium.android.apis:id/button_toggle' should display the text 'ON'

    When I press the system back button
    Then the 'Views' submenu screen should be displayed

    When I press the system back button
    Then the main API list should be visible on the screen

  @edge_case
  Scenario: Verify toggle button state behavior upon navigating away and returning
    When I tap on the 'Views' list item
    And I tap on the 'Buttons' list item
    Then the toggle button with ID 'io.appium.android.apis:id/button_toggle' should display the text 'OFF'

    When I tap the toggle button with ID 'io.appium.android.apis:id/button_toggle'
    Then the toggle button with ID 'io.appium.android.apis:id/button_toggle' should display the text 'ON'

    When I press the system back button
    And I tap on the 'Buttons' list item
    Then the toggle button with ID 'io.appium.android.apis:id/button_toggle' should display the default text 'OFF'