*** Settings ***
Library    ../CodeWars/CodeWars221109.py
Library    ../CodeWars/CodeWars221110.py
Library    ../CodeWars/CodeWars221111.py
Library    ../CodeWars/CodeWars221112.py


*** Variables ***
${value1}     3
${value2}     6

*** Test Cases ***
CodeWars1109
    ${result}    Text TransitionBy List    sdfsd
    Text TransitionBy String    Text
CodeWars1110
    ${result}    Main    words
    Smash    words
    Smash 2    words
    Smash 3    words
    Smash 4    words
CodeWars1111
    ${x}    Convert To Integer    5
    ${n}    Convert To Integer    10
    ${result}    CodeWars1111.Question 1    ${x}    ${n}
    Log    ${result}
    Log    message
    ${x}    Convert To Integer    ${value1}
    ${n}    Convert To Integer    ${value2}
    Count By    ${x}    ${n}   
    ${result}    Count By2    ${x}    ${n}