*** Settings ***
Resource  resource.robot
Test Setup   Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials    sanni    sanni123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials    kalle    kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials    sa    sanni123
    Output Should Contain  Username too short

Register With Long Enough Username Containing Something Else Than Letters And Valid Password
    Input Credentials    sanni1    sanni123
    Output Should Contain  Username must contain only letters a-z

Register With Valid Username And Too Short Password
    Input Credentials    sanni    jee
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials    sanni    sannijee
    Output Should Contain  Password must not contain only letters

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command