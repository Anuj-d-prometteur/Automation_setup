*** Settings ***
Library    SeleniumLibrary
Library    test.py
Library    firstcase
Library    firstcase.py

*** Variables ***
${BROWSER}    chrome
${URL}        https://wizzy-web-app.vercel.app/auth/login


*** Test Cases ***
Verify URL:
    [Setup]    Open Browser    ${URL}    ${BROWSER}
    Log    Browser opened successfully and navigated to the URL.
    ${current_url}=    Get Location
    Should Be Equal As Strings    ${current_url}    ${URL}    URL does not match the expected value.
    [Teardown]    Close Browser

Loginwith_vaild cridential:
    [Setup]     Open Browser    ${URL}   ${BROWSER}
    Log    valid cridential
    ${message}   login_adminAccount
    #Log    ${message}
    [Teardown]    Close Browser
    