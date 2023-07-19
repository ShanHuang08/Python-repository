*** Settings ***
Library    SeleniumLibrary
Library    BuiltIn
Library    ../dict.py
Library    robot_run.py
Library    ../test0630.py
# Library    /Users/Stephenhuang/Python/test

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
Test Case
    ${result}    Lists To Dict    key_list    key2_list    value_list

Run Method
    ${result}    Test SUT Type
    ${result}    Test Keyword
*** Keywords ***

