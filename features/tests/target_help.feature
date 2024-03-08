Feature: Target Help page tests

  Scenario: User can select a topic from Help dropdown
    Given Open Help page for Returns
    Then Verify Returns page is opened
    When Select Delivery & Pickup option
    Then Delivery & Pickup page is displayed