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
    Set Window Size    800     600
    Set Selenium Timeout    ${Seconds}
    Sleep    ${Seconds}
    Close Browser

*** Keywords ***

