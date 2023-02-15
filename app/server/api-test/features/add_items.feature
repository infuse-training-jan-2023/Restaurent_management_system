
Feature: Add items new to the database
    As a Admin I can add new item into database

    Scenario: Add items new to the database
        When I add new items
        Then the items should get saved into database
        Then api status code should be 200
        Then api response content type should be application/json
