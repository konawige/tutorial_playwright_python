Feature: As a user,  wat to be able to log in and access the account page

  Scenario: Ensure we can access the login page
    Given the login page is open
    Then the page contains the title Login


  Scenario: Given a user, when i fill login form with valid credentials,
  i can access account page when i submit the form
    Given the login page is open
    When i fill "username" on Login page with value "Willy"
    And i fill "password" on Login page with value "password"
    And i click "submit" button on the login page
    Then the next page is "Account" page
    And the welcome text on Account page contains the value "Willy"


  Scenario: Given a user, when i fill login form with invalid credentials,
  i stay on login page and a error message is displayed
    Given the login page is open
    When i fill "username" on Login page with value "Willy"
    And i fill "password" on Login page with value "pass"
    And i click "submit" button on the login page
    Then the next page is "Login" page
    And the error message on login page is visible

  Scenario: Given a user, when i click on forgot password button,
  i am redirected to a new form
    Given the login page is open
    When i click "forgot password" button on the login page
    Then the next page is "reset password" page
    And the text message on reset password page is visible