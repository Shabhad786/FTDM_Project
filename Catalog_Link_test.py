import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://qa.catalog.unifytwin.com/#/p/login")
driver.maximize_window()
driver.find_element(By.ID,"loginUserID").send_keys("CatalogAdmin")
driver.find_element(By.ID,"loginPassword").send_keys("DMPCCatAdm#v1@090")
driver.find_element(By.ID,"login_in_to_portal").click()
# copied_text = pyperclip.paste()
time.sleep(10)
driver.find_element(By.XPATH,"//button[@id='catalog_create_button']").click()
driver.find_element(By.XPATH,"//input[@placeholder='Enter Catalog Name']").send_keys("Catalog_New1")
driver.find_element(By.ID,"catalog_save").click()
time.sleep(5)
driver.find_element(By.ID,"ag-8112-input").send_keys("Catalog_New1")
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/ut-webapp-root/global-catalog-app-pages/global-catalog-app-list-catalog/div/div/div/div[2]/kl-ag-grid-server/ag-grid-angular/div/div[2]/div[2]/div[3]/div[2]/div/div/div[13]/div[4]/div/span/kl-template-renderer/span[2]").click()
time.sleep(20)
driver.find_element(By.ID,"global_catalog_token").click()

time.sleep(5)

driver.switch_to.new_window("new window")
time.sleep(20)
driver.get("https://qa.unifytwin.com/#/p/login")
time.sleep(5)
driver.find_element(By.ID,"loginUserID").send_keys("Admin")
driver.find_element(By.ID,"loginPassword").send_keys("iLens@123")
driver.find_element(By.ID,"login_in_to_portal").click()
time.sleep(15)
driver.find_element(By.XPATH, "//*[@id=\"project-selection-category\"]/li/div[1]/span[1]/span/label").click()
driver.find_element(By.XPATH,"//*[@id='new_project_dropdown_menu']/a[2]").click()
time.sleep(10)
driver.find_element(By.XPATH,"//input[@class='ag-input-field-input ag-text-field-input']").send_keys("Admin")
driver.find_element(By.XPATH,"(//button[@id='action_edit_5'])[2]").click()
time.sleep(10)
driver.find_element(By.XPATH,"//*[@id='print__screen']/kl-pages/kl-new-project/div[1]/div/div[1]/div/div/div[3]/h5/span[2]").click()
driver.find_element(By.ID,"catalog_url").send_keys("https://qa.catalog.unifytwin.com")
paste_field1=driver.find_element(By.ID,"catalog_access_token")
paste_field1.click()
paste_field1.send_keys(Keys.CONTROL, 'v')
time.sleep(5)
driver.find_element(By.ID,"param_saveP").click()
driver.find_element(By.ID,"new_project_creation").click()
driver.switch_to.window(windows[0])
driver.de

# driver.find_element(By.XPATH,"//label[@class='text-white mb-1 overflow-text project-name mt-2 ng-star-inserted']").click()
time.sleep(15)