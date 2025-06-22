from pytest_tutorial.pages.login_page import LoginPage
from pytest_tutorial.utils.config import URLS
import pytest


@pytest.mark.parametrize('username, password', [('tomsmith', 'SuperSecretPassword!'), ('suman', '123')])
def test_valid_login(setup_browser, username, password):
    driver = setup_browser
    driver.get(url=URLS.LOGIN_URL.value)

    login = LoginPage(driver=driver)
    login.set_username(name=username)
    login.set_password(password=password)
    login.click_login()

    # ✅ Add validation/assertion here
    if username == "tomsmith" and password == "SuperSecretPassword!":
        # Expected success — check for secure area
        assert "secure" in driver.current_url.lower()
        assert login.check_login(login_msg="success")
    else:
        # Expected failure — check for error message
        assert "secure" not in driver.current_url.lower()
        assert login.check_login(login_msg="error")
