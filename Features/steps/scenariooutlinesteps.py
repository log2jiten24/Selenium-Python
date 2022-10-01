from behave import *


@when('I Open HRM LoginPage')
def step_impl(context):
    print('Open the HRM Page')


@when('Enter Username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    print('Login successfully with diff parameters : ' + user + " " + pwd)


@when('Click on Login Button')
def step_impl(context):
    print('User clicks on login button')


@then(u'User navigates to Dashboard Page')
def step_impl(context):
    print('User navigates to Dashboard Page')
