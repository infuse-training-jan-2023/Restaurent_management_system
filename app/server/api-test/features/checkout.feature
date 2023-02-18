
Feature: Checkout cart
    As a user I can delete item from the cart

    Scenario: Checkout cart
        When I click on checkout
        Then the items get saved into orders history
        Then api status code should be 200
        Then api response content type should be application/json

    Scenario: Invalid Checkout cart
        When user try to checkout before adding items into cart
        Then api status code should be 200
        Then api response content type should be application/json

    Scenario: Invalid Checkout method
        When user tries to change checkout method
        Then api status code should be 405
        Then api response content type should be application/json
