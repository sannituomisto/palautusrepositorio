*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go to Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username  sanni
    Set Password  sanni123
    Set Passwordconf    sanni123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  sa
    Set Password  sanni123
    Set Passwordconf    sanni123
    Submit Credentials
    Register Should Fail With Message    Username too short

Register With Long Enough Username Containing Something Else Than Letters And Valid Password
    Set Username  sanni1
    Set Password  sanni123
    Set Passwordconf    sanni123
    Submit Credentials
    Register Should Fail With Message    Username must contain only letters a-z

Register With Valid Username And Too Short Password
    Set Username  sanni
    Set Password  sanni1
    Set Passwordconf    sanni1
    Submit Credentials
    Register Should Fail With Message    Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Set Username  sanni
    Set Password  sannijee
    Set Passwordconf    sannijee
    Submit Credentials
    Register Should Fail With Message    Password must not contain only letters


Register With Nonmatching Password And Password Confirmation
    Set Username  sanni
    Set Password  sanni123
    Set Passwordconf    sanni1234
    Submit Credentials
    Register Should Fail With Message    Password and password confirmation are not matching

Login After Successful Registration
    Set Username  sanni
    Set Password  sanni123
    Set Passwordconf    sanni123
    Submit Credentials
    Register Should Succeed
    Click Link  Continue to main page
    Main Page Should Be Open
    Click Button    Logout
    Login Page Should Be Open
    Set Username  sanni
    Set Password  sanni123
    Click Button    Login
    Main Page Should Be Open



Login After Failed Registration
    Set Username  sa
    Set Password  sanni123
    Set Passwordconf    sanni123
    Submit Credentials
    Register Should Fail With Message    Username too short
    Click Link    Login
    Set Username  sa
    Set Password  sanni123
    Click Button    Login
    Login Should Fail With Message    Invalid username or password




*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Passwordconf
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register



Create User And Go to Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open