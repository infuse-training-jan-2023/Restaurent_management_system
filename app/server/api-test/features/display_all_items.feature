
Feature: Display all items
    As a Admin I can get all the item from the database

    Scenario: Display all items
        When I fetch the items
        Then I get all the itemes from database
        Then api status code should be 200
        Then api response content type should be application/json
