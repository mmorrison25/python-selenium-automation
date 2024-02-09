Feature: Target search tests

  Scenario: User can search for bedding on Target
    Given Target site is launched
    When Search for bedding
    Then Search results for bedding are shown

  Scenario: User can search for magic cards on Target
    Given Target site is launched
    When Search for magic cards
    Then Search results for magic cards are shown