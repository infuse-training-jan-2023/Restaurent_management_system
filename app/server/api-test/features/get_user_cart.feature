
Feature: Get items from cart
    As a user I can get items from the cart

    Scenario: Get items from cart
        When I give the username
        Then I should get all the items in the cart
        Then api status code should be 200
        Then api response content type should be application/json

    Scenario: Get empty cart of user
        When I give the username with empty
        Then api status code should be 200
        Then api response content type should be application/json

    Scenario: Invalid request Get items from cart
        When I give the username with inavlid method
        Then api status code should be 405
        Then api response content type should be application/json
