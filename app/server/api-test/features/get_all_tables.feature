
Feature: Display all tables
    As a Admin I can view all the tables

    Scenario: Display all items
        When I fetch the tables
        Then all the booking tables are displayed
        Then api status code should be 200
        Then api response content type should be application/json
