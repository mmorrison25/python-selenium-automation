Feature: Target cart test scenarios

  Scenario: User can view the cart
    Given Target site is launched
    When Cart icon is clicked
    Then Verify "Your cart is empty" message shown

  Scenario: User can add an item to the cart
    Given Target site is launched
    When Search for bedding
    And Add to cart button is clicked
    Then Verify item is displayed in the cart