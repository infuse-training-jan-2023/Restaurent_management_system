Feature: Order history
    As a user I can get order deatils

    Scenario: Order history
    When I check order history
    Then I should get all the order history
    Then the api status code should be 200
    Then the api response content type should be json
