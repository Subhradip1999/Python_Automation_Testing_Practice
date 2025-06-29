import time
from behave import given, when, then
from pages.login_page import LoginPage


@given("the login page is open")
def step_open_login_page(context):
    context.page = LoginPage(driver=context.driver)
    context.page.load()


@when("the user logs in with username '{username}' and password '{password}'")
def step_login_with_cred(context, username, password):
    context.page.login(username=username, password=password)


@then("the user should see the secure area")
def step_verify_success_login(context):
    time.sleep(1)
    msg = context.page.get_flash_message()
    assert "You logged into a secure area!" in msg


@then("an error message is shown")
def step_verify_failure_login(context):
    time.sleep(1)
    msg = context.page.get_flash_message()
    assert "Your username is invalid!" in msg or "Your password is invalid!" in msg
