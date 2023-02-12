Feature: Add table
    As a admin i can Add a table

    Scenario: Add table
        When I add a table
        Then table should be added
        Then api status code should be 200
        Then api response content type should be application/json

    