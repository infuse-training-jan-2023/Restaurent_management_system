
Feature: Delete item from cart
    As a user I can delete item from the cart

    Scenario: Delete item from cart
        When I give the username and item name
        Then the item should get deleted from the cart
        Then api status code should be 200
        Then api response content type should be application/json

    Scenario: Delete invalid item from cart
        When I give the username and item name which is not there in cart
        Then api status code should be 200
        Then api response content type should be application/json

    Scenario: change method Delete item from cart
        When I give the username and item name and change method
        Then api status code should be 405
        Then api response content type should be application/json
