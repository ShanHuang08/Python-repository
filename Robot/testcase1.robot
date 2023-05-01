*** Settings ***
Library    SeleniumLibrary
Library    BuiltIn

*** Variables ***
${BROWSER}    chrome
${url}    www.google.com.tw
${Seconds}    5s

*** Test Cases ***
LoginTest
    Open Browser    http://${url}   ${BROWSER}
    Set Selenium Timeout    ${Seconds}
    Sleep    ${Seconds}
    Close Browser

*** Keywords ***

# pip install robotframework
# Version: 6.0.2
# pip install robotframework-SeleniumLibrary
# Version: 6.0.0

# https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html#Set%20Selenium%20Timeout
# https://robotframework.org/robotframework/latest/libraries/BuiltIn.html