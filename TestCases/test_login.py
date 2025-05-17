import time
import pytest
from selenium import webdriver
import logging
from PageObjects.LoginPage import LoginPage  # Ensure this import is correct
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class TestLogin:
    Ftdm_URL = ReadConfig.getApplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger=LogGen.loggen()

    def test_Homepage(self, setup):
        self.driver = setup
        self.driver.get(self.Ftdm_URL)
        self.driver.maximize_window()
        time.sleep(10)  # Wait for page to load (consider using WebDriverWait instead of sleep)
        self.driver.save_screenshot(".\\Screenshots\\"+"test_Homepage.png")
        time.sleep(10)
        self.driver.close()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.Ftdm_URL)
        self.driver.maximize_window()
        time.sleep(10)
        self.LP = LoginPage(self.driver)  # Create LoginPage object

        # Set username and password
        self.LP.setUserName(self.username)
        time.sleep(2)  # Optional: Wait if necessary, consider WebDriverWait instead
        self.LP.setPassword(self.password)
        time.sleep(2)  # Optional: Wait if necessary, consider WebDriverWait instead

        # Click login button
        self.LP.clickLogin()
        time.sleep(10)  # Optional: Wait for login process to finish
        self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
        time.sleep(5)
        self.driver.close()

