*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing Special Character
    Set Username  peter
    Set Password  kalle#abc
    Set Password Confirmation  kalle#abc
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing Only Lowercase Letters
    Set Username  matti
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Click  button >> text=Register
    Register Fail With Message  Password must contain at least one number or special character

Register With Password Containing Only Uppercase And Lowercase Letters
    Set Username  ville
    Set Password  KalleKalle
    Set Password Confirmation  KalleKalle
    Click  button >> text=Register
    Register Fail With Message  Password must contain at least one number or special character

Register With Too Short Username And Valid Password
    Set Username  ab
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Fail With Message  Username must be at least 3 characters     

Register With Valid Username And Too Short Password
    Set Username  peter
    Set Password  kal123
    Set Password Confirmation  kal123
    Click  button >> text=Register
    Register Fail With Message  Password must be at least 8 characters     

Register With Username That Is Already In Use
    ${username} =  Set Variable  kalle
    Create User  ${username}  kalle123
    Set Username  ${username}
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Fail With Message  User with username ${username} already exists

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Set Password Confirmation
    [Arguments]  ${password}
    Fill Secret  id=password_confirmation  $password

Reset Application Create User And Go To Register Page
    Reset Application
    Go To Register Page
