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
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  aaaaa123
    Set Password Confirmation  aaaaa123
    Submit Register Credentials
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  nalle
    Set Password  nalle1
    Set Password Confirmation  nalle1
    Submit Register Credentials
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  valle
    Set Password  vallevalle
    Set Password Confirmation  vallevalle
    Submit Register Credentials
    Register Should Fail With Message  Password must contain at least one number

Register With Nonmatching Password And Password Confirmation
    Set Username  julle
    Set Password  julle123
    Set Password Confirmation  julle456
    Submit Register Credentials
    Register Should Fail With Message  Password and password confirmation do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle321
    Set Password Confirmation  kalle321
    Submit Register Credentials
    Register Should Fail With Message  User with username kalle already exists

Login After Successful Registration
    Set Username  tiuhti
    Set Password  tiuhti987
    Set Password Confirmation  tiuhti987
    Submit Register Credentials
    Register Should Succeed
    Click Link  Continue to main page
    Log Out From App
    Login Page Should Be Open
    Set Username  tiuhti
    Set Password  tiuhti987
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  viuhti
    Set Password  viuhti007
    Set Password Confirmation  viuhti700
    Submit Register Credentials
    Register Should Fail With Message  Password and password confirmation do not match
    Go To Login Page
    Login Page Should Be Open
    Set Username  viuhti
    Set Password  viuhti007
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Register Credentials
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

Log Out From App
    Click Button  Logout

Submit Login Credentials
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}


*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User    kalle    kalle123
    Go To Register Page
