from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, 'username')
        self.password = (By.ID, 'password')
        self.login_btn = (By.XPATH, "//button[@type='submit']")

    def set_username(self, name):
        self.driver.find_element(*self.username).send_keys(name)

    def set_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()

    def check_login(self, login_msg):
        return self.driver.find_element(By.CLASS_NAME, login_msg).is_displayed()
