
Feature: Add items to cart
    As a user I can add items to the cart

    Scenario: Add items to cart
        When I add items to cart
        Then items should be added to cart
        Then api status code should be 200
        Then api response content type should be application/json
