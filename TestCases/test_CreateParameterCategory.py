import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PageObjects.LoginPage import LoginPage  # Ensure this import is correct
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from PageObjects.Create_ParameterCategory import Create_ParameterCategory  # Assuming this class is in PageObjects


class Test_Create_ParameterCategory:
    Ftdm_URL = ReadConfig.getApplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    def test_Create_ParameterCategory(self, setup):
        self.driver = setup
        self.driver.get(self.Ftdm_URL)
        self.driver.maximize_window()

        # Log in
        self.LP = LoginPage(self.driver)
        self.LP.setUserName(self.username)
        self.LP.setPassword(self.password)
        self.LP.clickLogin()


        # Wait until login is complete
        time.sleep(10)  # You can replace this with WebDriverWait

        # Create an instance of Create_ParameterGroup
        self.paramCategory = Create_ParameterCategory(self.driver)

        # Perform actions for creating, searching, deleting, and downloading the parameter group
        self.paramCategory.expand_navigation()

        # Assuming create_parameter_category, search_parameter_category, etc., take some parameters
        param_cat=self.paramCategory.create_parameter_Category()
        self.paramCategory.Edit_parameter_Category(param_cat)
        self.paramCategory.Clone_Parameter_Category(param_cat + "1")
        self.paramCategory.delete_parameter_Category(param_cat + "12")
        self.paramCategory.download_parameter_Category()
        self.logger.info("Test execution completed successfully.")

    def test_Create_Parametergroup(self, setup):
        self.driver = setup
        self.driver.get(self.Ftdm_URL)
        self.driver.maximize_window()

        # Log in
        self.LP = LoginPage(self.driver)
        self.LP.setUserName(self.username)
        self.LP.setPassword(self.password)
        self.LP.clickLogin()

        # Wait until login is complete
        time.sleep(10)  # You can replace this with WebDriverWait

        # Create an instance of Create_ParameterGroup
        self.paramgroup = Create_ParameterCategory(self.driver)

        # Perform actions for creating, searching, deleting, and downloading the parameter group
        self.paramgroup.expand_navigation()

        # Assuming create_parameter_category, search_parameter_category, etc., take some parameters
        Param_Grp=self.paramgroup.create_parameter_Group()
        self.paramgroup.Edit_parameter_Group(Param_Grp)
        self.paramgroup.Clone_Parameter_Group(Param_Grp + "1")
        self.paramgroup.delete_parameter_Group(Param_Grp + "12")
        self.paramgroup.download_parameter_Group()
        self.logger.info("Test execution completed successfully.")
        self.driver.close()

    def test_Create_Parameter(self, setup):
        self.driver = setup
        self.driver.get(self.Ftdm_URL)
        self.driver.maximize_window()

        # Log in
        self.LP = LoginPage(self.driver)
        self.LP.setUserName(self.username)
        self.LP.setPassword(self.password)
        self.LP.clickLogin()

        # Wait until login is complete
        time.sleep(10)  # You can replace this with WebDriverWait

        # Create an instance of Create_ParameterGroup
        self.parameter = Create_ParameterCategory(self.driver)

        # Perform actions for creating, searching, deleting, and downloading the parameter group
        self.parameter.expand_navigation()

        # Assuming create_parameter_category, search_parameter_category, etc., take some parameters

        Param_New=self.parameter.create_parameter()
        self.parameter.Edit_parameter(Param_New)
        self.parameter.Clone_Parameter(Param_New + "1")
        self.parameter.delete_parameter(Param_New + "12")
        self.parameter.download_parameter()
        self.logger.info("Test execution completed successfully.")
        self.driver.close()
