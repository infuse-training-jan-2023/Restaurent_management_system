Feature: Add table
    As a user I can book a table

    Scenario: Add table
        When I book a table
        Then booking should be added to database
        Then api status code should be 200
        Then api response content type should be application/json

    Scenario: Add table with invalid request
        When I book a table with invalid request method
        Then booking should be added to database
        Then api status code should be 405
        Then api response content type should be application/json
