*** Settings ***
Library    SeleniumLibrary
Library    BuiltIn

*** Variables ***
${BROWSER}    chrome
${url}    10.184.30.32
${Seconds}    5s

*** Test Cases ***
LoginTest
    Open Browser    http://${url}   ${BROWSER}
    Set Window Size    1920     1080
<<<<<<< HEAD:Robot/testcase1.robot
=======
    Click Element    id:details-button
    Click Element    id:proceed-link
>>>>>>> d26a11260edeb6829d56320cb5c96edd8623d0e4:Robot/BMC_Login.robot
    Set Selenium Timeout    ${Seconds}
    Sleep    2s
    Input Text    id:usrName    ADMIN
    Input Password    id:pwd    ADMIN
    Click Button    id:login_word
    Sleep    ${Seconds}
    Capture Page Screenshot
    Close Browser

*** Keywords ***

