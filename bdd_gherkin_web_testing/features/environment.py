from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_all(context):
    option = Options()
    option.add_argument("--headless")
    context.driver = webdriver.Chrome(options=option)


def after_all(context):
    context.driver.quit()
