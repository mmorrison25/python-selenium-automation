# Created by madisonmorrison at 2/1/24
Feature: Target.com test scenarios

  Scenario: User can view the cart
    Given Target site is launched
    When Cart icon is clicked
    Then Your cart is empty message shown

  Scenario: User can access sign in page
    Given Target site is launched
    When Sign In option is clicked
    When Sign In is clicked from right side nav menu
    Then Sign In form opened