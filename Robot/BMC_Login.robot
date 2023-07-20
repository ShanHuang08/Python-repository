*** Settings ***
Library    SeleniumLibrary
Library    BuiltIn
Library    ../dict.py
# Library    ../test0630.py
Library    testrun.py

*** Variables ***
${BROWSER}    chrome
${url}    10.184.30.32
${Seconds}    5s

*** Test Cases ***
# LoginTest
#     Open Browser    http://${url}   ${BROWSER}
#     Set Window Size    1920     1080
#     Click Element    id:details-button
#     Click Element    id:proceed-link
#     Set Selenium Timeout    ${Seconds}
#     Sleep    2s
#     Input Text    id:usrName    ADMIN
#     Input Password    id:pwd    ADMIN
#     Click Button    id:login_word
#     Sleep    ${Seconds}
#     Capture Page Screenshot
#     Close Browser
TestCase2
    ${result}    Testlog
    ${result}    This is a new keyword

Custom
    ${result}    MyLibrary0630
*** Keywords ***

