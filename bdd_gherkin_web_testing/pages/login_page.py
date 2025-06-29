from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import BASE_URL


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, 'username')
        self.password = (By.ID, 'password')
        self.login_button = (By.CSS_SELECTOR, 'button[type="submit"]')
        self.flash_msg = (By.ID, 'flash')

    def load(self, url=BASE_URL):
        self.driver.get(url)

    def login(self, username, password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_flash_message(self, timeout=5):
        wait = WebDriverWait(self.driver, timeout=timeout)
        element = wait.until(EC.presence_of_element_located(self.flash_msg))
        return element.text
