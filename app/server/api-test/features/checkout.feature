
Feature: Checkout cart
    As a user I can delete item from the cart

    Scenario: Checkout cart
        When I click on checkout
        Then the items get saved into orders history
        Then api status code should be 200
        Then api response content type should be application/json
