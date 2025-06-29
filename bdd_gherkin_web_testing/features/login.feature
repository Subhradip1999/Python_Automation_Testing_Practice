Feature: Login Functionality
    Scenario: Successful login with valid credentials
        Given the login page is open
        When the user logs in with username 'tomsmith' and password 'SuperSecretPassword!'
        Then the user should see the secure area

    Scenario: Unsuccessful login with invalid credentials
        Given the login page is open
        When the user logs in with username 'suman' and password 'Suman_123'
        Then an error message is shown
