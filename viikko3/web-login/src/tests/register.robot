*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  ville
    Set Password  ville123
    Set Password Confirmation  ville123
    Submit Credentials

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  aaaaa123
    Set Password Confirmation  aaaaa123
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  nalle
    Set Password  nalle1
    Set Password Confirmation  nalle1
    Submit Credentials
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  valle
    Set Password  vallevalle
    Set Password Confirmation  vallevalle
    Submit Credentials
    Register Should Fail With Message  Password must contain at least one number

Register With Nonmatching Password And Password Confirmation
    Set Username  julle
    Set Password  julle123
    Set Password Confirmation  julle456
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle321
    Set Password Confirmation  kalle321
    Submit Credentials
    Register Should Fail With Message  User with username kalle already exists


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}


*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User    kalle    kalle123
    Go To Register Page
