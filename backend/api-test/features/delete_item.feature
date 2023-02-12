
Feature: Delete item from cart
    As a user I can delete item from the cart

    Scenario: Delete item from cart
        When I give the username and item name
        Then the item should get deleted from the cart
        Then api status code should be 200
        Then api response content type should be application/json
