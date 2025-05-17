import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options=Options()
chrome_options.add_argument("--force-device-scale-factor='100%'")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get("https://qa.unifytwin.com/#/p/login")
time.sleep(15)

driver.find_element(By.ID,"loginUserID").send_keys("changer")
driver.find_element(By.ID,"loginPassword").send_keys("Changer@123")
driver.find_element(By.ID,"login_in_to_portal").click()
time.sleep(10)

driver.find_element(By.XPATH,"//*[@id='print__screen']/kl-pages/kl-left-side-bar/div/ul/div[1]/div/div").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='print__screen']/kl-pages/kl-left-side-bar/div/ul/div[2]/li[1]/div/div[2]").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='print__screen']/kl-pages/kl-left-side-bar/div/ul/div[2]/ul/li[4]/div/span").click()
time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,"em[class='elm-add-property']").click()
# time.sleep(3)
# driver.find_element(By.CSS_SELECTOR,"input[placeholder='Enter Asset Model Name']").send_keys("WaterModel")
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,"textarea[placeholder='Description']").send_keys("WaterModel")
# time.sleep(2)
# driver.find_element(By.ID,"asset_type").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//div[contains(@class,'ng-option')]/span[text()='Heat Exchanger']").click()
# time.sleep(2)
# driver.find_element(By.ID,"industry_category_id").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//div[contains(@class,'ng-option')]/span[text()='Breverage']").click()
# time.sleep(2)
# driver.find_element(By.ID,"basic_save_proceed_btn").click()
# time.sleep(3)


driver.find_element(By.ID,"search_input").send_keys("WaterModel")
time.sleep(5)
driver.find_element(By.XPATH,"//span[@class='roboto_medium' and text()='WaterModel']").click()
time.sleep(5)
driver.find_element(By.ID,"basic_save_proceed_btn").click()
time.sleep(3)
driver.find_element(By.ID,"addnew").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"ng-select[placeholder='Select Parameter Group']").click()
time.sleep(5)






