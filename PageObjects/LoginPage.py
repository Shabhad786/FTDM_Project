from selenium.webdriver.common.by import By  # Import the By class
from selenium.webdriver.common.keys import Keys  # Optional for key actions

class LoginPage:
    textbox_username_id = "loginUserID"
    textbox_password_id = "loginPassword"
    button_login_id = "login_in_to_portal"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        # Locate username field and clear it, then input username
        # self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        # Locate password field and clear it, then input password
        # self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        # Click the login button
        self.driver.find_element(By.ID, self.button_login_id).click()
