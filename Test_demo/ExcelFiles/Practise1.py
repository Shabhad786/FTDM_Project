import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
chrome_options=Options()
chrome_options.add_argument("--force-device-scale-factor='100%'")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.find_element(By.ID,"name").send_keys("Shabhad Peddadevara")
driver.find_element(By.ID,"email").send_keys("shabhad@gmail.com")
driver.find_element(By.XPATH, "//*[@id='gender']").click()
driver.find_element(By.XPATH,"//input[@placeholder='Enter Mobile Number']").send_keys("726577185781")
driver.find_element(By.ID,"dob").send_keys("26-01-1519")
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Enter Subject']").send_keys("maths")
driver.find_element(By.XPATH, "//input[@type='checkbox' and @value='Music']").click()


time.sleep(20)