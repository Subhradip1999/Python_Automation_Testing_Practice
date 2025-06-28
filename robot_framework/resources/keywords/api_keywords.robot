
*** Keywords ***
Get User Details
    Create Session      api     ${API_URL}
    ${response}=    Get Request     api     /
    Status Should Be    200     ${response}