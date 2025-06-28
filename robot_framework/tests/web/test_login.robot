*** Settings ***
Library     SeleniumLibrary
Resource    ../../resources/veriables.robot
Resource    ../../resources/keywords/web_keywords.robot

*** Test Cases ***
Login Test - Valid User
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Login To Application    ${USERNAME}     ${PASSWORD}
    [Teardown]      Close Browser