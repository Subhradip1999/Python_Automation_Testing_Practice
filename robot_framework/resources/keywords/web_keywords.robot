*** Keywords ***
Login To Application
    [Arguments]     ${username}     ${password}
    Input Text      id=username     ${username}
    Input Text      id=password     ${password}
    Click Button    class=radius
    Page Should Contain Element     xpath=//div[@class='flash success']