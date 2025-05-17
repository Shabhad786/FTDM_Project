import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver=webdriver.Chrome()

driver.get("https://www.tutorialspoint.com/selenium/practice/upload-download.php")
time.sleep(5)

driver.find_element(By.CSS_SELECTOR,"input[id='uploadFile']").click()
time.sleep(5)
