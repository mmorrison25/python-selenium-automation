Feature: Target cart test scenarios

  Scenario: User can view the cart
    Given Target site is launched
    When Cart icon is clicked
    Then Your cart is empty message shown

  Scenario: User can add an item to the cart
    Given Target site is launched
    When Search for bedding
    When Item is added to cart
    Then Item is displayed in the cart