import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://qa.catalog.unifytwin.com/#/p/login")
driver.find_element(By.ID,"loginUserID").send_keys("CatalogAdmin")
driver.find_element(By.ID,"loginPassword").send_keys("DMPCCatAdm#v1@090")
driver.find_element(By.ID,"login_in_to_portal").click()
driver.maximize_window()
#driver.find_element()
time.sleep(10)
# driver.find_element(By.XPATH,"//button[@id='catalog_create_button']").click()
# driver.find_element(By.XPATH,"//input[@placeholder='Enter Catalog Name']").send_keys("Testing_Domiana")
# driver.find_element(By.ID,"catalog_save").click()
Gettext=driver.find_element(By.XPATH,"/html/body/ut-webapp-root/kl-toastr/toaster-container").text
# print(Gettext)
# assert "Workspace Name Already Exist. Kindly use different name".lower() in Gettext.lower()
# driver.find_element(By.XPATH,"/html/body/ut-webapp-root/global-catalog-app-pages/global-catalog-app-list-catalog/div/div/div/div[2]/kl-ag-grid-server/ag-grid-angular/div/div[2]/div[2]/div[3]/div[2]/div/div/div[12]/div[4]/div/span/kl-template-renderer/span[1]").click()
driver.find_element(By.XPATH,"/html/body/ut-webapp-root/global-catalog-app-pages/global-catalog-app-main-side-bar/div/ul/div[1]/div/div/div/span").click()
driver.find_element(By.XPATH,"/html/body/ut-webapp-root/global-catalog-app-pages/global-catalog-app-main-side-bar/div/ul/div[2]/li[1]/div").click()
driver.find_element(By.XPATH,"/html/body/ut-webapp-root/global-catalog-app-pages/global-catalog-app-main-side-bar/div/ul/div[2]/ul/li/div/span").click()
driver.find_element(By.XPATH,"/html/body/ut-webapp-root/global-catalog-app-pages/global-catalog-app-main-side-bar/div/ul/div[2]/li[2]/div/div[2]").click()
driver.find_element(By.ID,"pending_0").click()
driver.find_element(By.ID,"rejected_1").click()
driver.find_element(By.ID,"approved_2").click()
driver.find_element(By.XPATH,"//label[@class='text-white mb-1 overflow-text project-name mt-2 ng-star-inserted']").click()
# driver.find_element(By.XPATH,"//a[@class='class='dropdown-item new-project-dropdown-item d-flex justify-content-between align-items-end ng-star-inserted']").click()
time.sleep(5)
driver.switch_to.new_window("new window")
time.sleep(5)
driver.get("https://qa.unifytwin.com/#/p/login")
time.sleep(20)
driver.find_element(By.ID,"loginUserID").send_keys("Admin")
driver.find_element(By.ID,"loginPassword").send_keys("iLens@123")
driver.find_element(By.ID,"login_in_to_portal").click()
driver.find_element(By.XPATH, "//*[@id=\"project-selection-category\"]/li/div[1]/span[1]/span/label").click()





