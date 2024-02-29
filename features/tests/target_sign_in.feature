Feature: Target sign in test scenarios

  Scenario: User can access sign in page
    Given Target site is launched
    When Sign In option is clicked
    And Sign In is clicked from right side nav menu
    Then Sign In page opened

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Target site is launched
    When Sign In option is clicked
    And Sign In is clicked from right side nav menu
    And Sign In page opened
    And Store original window
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window and switch back to original