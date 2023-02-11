Feature: Order food
    As a user I can order an food

    Scenario: Order food
    When I order a food
    Then order should get placed
    Then the api status code should be 200
    Then the api response content type should be json
