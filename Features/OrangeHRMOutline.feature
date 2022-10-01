Feature: To test different login credentials
 Scenario Outline: To test with different types of credentials
    Given Launch Chrome Browser
    When  I Open HRM LoginPage
    And   Enter Username "<username>" and password "<password>"
    And   Click on Login Button
    Then  User navigates to Dashboard Page

    Examples:
    |username | password |
    | admin   | admin123 |
    | admin   | admin 234|
