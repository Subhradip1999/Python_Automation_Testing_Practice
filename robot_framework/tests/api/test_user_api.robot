*** Settings ***
Library     RequestsLibrary
Resource    ../../resources/veriables.robot
Resource    ../../resources/keywords/api_keywords.robot

*** Test Cases ***
Verify User API Returns 200
    Get User Details