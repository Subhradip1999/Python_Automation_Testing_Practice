from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/login')
driver.find_element(By.ID, 'username').send_keys('tomsmith')
driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')

driver.find_element(By.XPATH, "//button[@type='submit']").click()

driver.save_screenshot('login.png')
