from behave import given, when, then
from selenium import webdriver

@given('User Launches Chrome Browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="F:\\Python\Selenium-Python\\drivers\\chromedriver_win32\\chromedriver.exe")
    #context.driver = webdriver.Chrome()


@when('Open Orange HRM HomePage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@then('verify that logo present on homepage')
def step_impl(context):
    status = context.driver.find_element_by_xpath("(//div[@id = 'app']//img)[1]").is_displayed()
    assert status is True


@then('Close the Browser')
def step_impl(context):
    context.driver.close()


