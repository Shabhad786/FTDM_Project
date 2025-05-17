import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--force-device-scale-factor=1")  # Correct way

# Launch browser
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Generate a random material name
random_text = "Material_Add_" + ''.join(random.choices(string.ascii_letters + string.digits, k=6))
random_text1 = "Material_Add_" + ''.join(random.choices(string.ascii_letters + string.digits, k=6))


# Start automation
driver.get("https://qa.unifytwin.com/#/p/login")
time.sleep(15)

# Login
driver.find_element(By.ID, "loginUserID").send_keys("changer")
driver.find_element(By.ID, "loginPassword").send_keys("Changer@123")
driver.find_element(By.ID, "login_in_to_portal").click()
time.sleep(10)

# Navigation steps
driver.find_element(By.XPATH, "//*[@id='print__screen']/kl-pages/kl-left-side-bar/div/ul/div[1]/div/div").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='print__screen']/kl-pages/kl-left-side-bar/div/ul/div[2]/li[1]/div/div[2]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='print__screen']/kl-pages/kl-left-side-bar/div/ul/div[2]/ul/li[3]/div/span").click()
time.sleep(5)

# Add new material
driver.find_element(By.CSS_SELECTOR, "button[id='addnew']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Material Name']").send_keys(random_text)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Material Code']").send_keys(random_text)
driver.find_element(By.ID, "dfm_left_submit_action").click()
time.sleep(5)

# Search and edit
driver.find_element(By.CSS_SELECTOR, "input[aria-label='Material Name Filter Input']").send_keys(random_text)
time.sleep(5)
driver.find_element(By.ID, "action_edit_0").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Material Name']").send_keys("1")
time.sleep(2)
driver.find_element(By.ID, "dfm_left_submit_action").click()
time.sleep(5)

# Search updated name and delete
driver.find_element(By.CSS_SELECTOR, "input[aria-label='Material Name Filter Input']").send_keys(random_text + "1")
time.sleep(3)
driver.find_element(By.ID, "action_delete_0").click()
time.sleep(2)
driver.find_element(By.ID, "btn_confirm_delete").click()
time.sleep(5)

# Download
driver.find_element(By.ID, "download").click()
