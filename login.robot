

*** Settings ***
Library    SeleniumLibrary
Library    ../TestScripts/firstcase.py


*** Variables ***
${URL}    https://dev.d3jbs5bk23dxtb.amplifyapp.com/
${BROWSER}    chrome
${USERNAME}    your_username
${modules}    firstcase.py

*** Test Cases ***
Login_with_valid_otp

    Open_window
    firstcase.verify the login with invaild Otp

*** Keywords ***
Open_window
    Open Browser    https://dev.d3jbs5bk23dxtb.amplifyapp.com/     chrome
    Maximize Browser window
