
from behave import *
from selenium import webdriver

@given('Launch Chrome Browser')
def step_impl(context):
    #driver = webdriver.Chrome()
    print('Driver launched')


@when('Open HRM HomePage')
def step_impl(context):
    #context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print('Open HRM Page')

@when('enters Username as "{user}" and Password as "{pwd}"')
def login(context, user, pwd):
    print('Login successfully' + user + " " + pwd)
    #context.driver.find_element_by_name('username').send_keys(user)
    #context.driver.find_element_by_name('password').send_keys(pwd)
    #print('Username is :' + user + "Password is : " + pwd)
    #print(user + " " + pwd)


@when('User clicks on Login Button')
def step_impl(context):
    print('User clicks on login button')
    #context.driver.find_element_by_xpath("//button[@type = 'submit']").click()


@then('User is navigated to the Dashboard Page')
def step_impl(context):
    #context.driver.close()
    print('User navigates to Dashboard Page ')

