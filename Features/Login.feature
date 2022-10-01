Feature: OrangeHRM Login Feature
  Scenario: Login to HRM Page with valid credentials
    Given Launch Chrome Browser
    When  Open HRM HomePage
    And enters Username as "admin" and Password as "admin123"
    And User clicks on Login Button
    Then User is navigated to the Dashboard Page

Feature: To test different login credentials
 Scenario Outline: Login to HRM Page with valid credentials Scenarios
    Given Launch Chrome Browser
    When  Open HRM HomePage
    And enters Username as "<Username>" and Password as "<Password>"
    And User clicks on Login Button
    Then User is navigated to the Dashboard Page