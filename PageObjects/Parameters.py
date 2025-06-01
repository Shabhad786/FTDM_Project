import time

from selenium.webdriver.common.by import By
import random
import string

class Create_ParameterCategory:
    Expand_Navigation_By_XPATH = "//div[@class='bar-icon ng-star-inserted']"
    Select_AssetManagment_By_XPATH = "//span[@class='fa fa-angle-down']"
    Select_Parameters_By_XPATH = "//span[@title='Parameters']"
    Select_ParameterCategory_By_ID = "parameter_category_tab"
    Create_ParameterCategory_By_CSS_SELECTOR = "button[id='addnew']"
    Input_ParameterCategoryName_By_ID = "param_category_name"
    Input_ParameterCategorydesc_By_ID = "param_desc"
    Click_SubCategory_ImputField_By_ID ="sub_category"
    SubCategory_By_Xpath = "//div[contains(@class,'ng-option')]/span[text()='Add New']"
    Input_SubCategory_By_CSS_SELECTOR="input[placeholder='Enter Sub-category Name']"
    Save_ParameterCategory_By_ID = "param_category_save"
    Search_Filter_By_CSS_SELECTOR = "input[aria-label='Tag Category Name Filter Input']"
    Click_Edit_By_ID = "action_edit_0"
    Update_name_By_ID = "param_category_name"
    Delete_parameterCategory_By_ID = "action_delete_0"
    Confirm_Delete_By_ID = "btn_confirm_delete"
    Clone_By_ID="action_clone_0"
    Download_parameterCategory_By_ID = "download"
    Select_ParameterGroup_By_ID="parameter_group_tab"
    Create_ParameterGroup_By_CSS_SELECTOR = "button[id='addnew']"
    Input_ParamGroupName_By_Xpath= "//input[@placeholder='Parameter Group Name']"
    Input_Description_By_CSS_SELECTOR="textarea[placeholder='Description..']"
    Save_ParameterGroup_By_CSS_SELECTOR="button[class='btn btn-primary ng-star-inserted']"
    Search_Filter_By_CSS_SELECTOR="input[class='ag-input-field-input ag-text-field-input']"
    Edit_ParameterGroup_By_ID="action_edit_0"
    Edit_ParameterGroupName_By_CSS_SELECTOR= "input[formcontrolname='tag_group_name']"
    Save_ParameterGroup_By_CSS_SELECTOR="button[class='btn btn-primary ng-star-inserted']"
    Search_Filter_By_CSS_SELECTOR="input[class='ag-input-field-input ag-text-field-input']"
    Click_Subgroup_ImputField_CSS_Selector= "ng-select[placeholder='Select Parameter category..']"
    ParameterGroup_By_Xpath = "//div[contains(@class,'ng-option')]/span[text()='NewParamCat12']"
    Click_Paramgroup_Edit_By_ID = "action_edit_0"
    Delete_parameterGroup_By_ID = "action_delete_0"
    Confirm_Delete_By_ID = "btn_confirm_delete"
    Select_Parameter_By_ID = "parameter_tab"
    Create_Parameter_By_ID = "addnew"
    Input_Param_name_By_ID = "param_name"
    Input_Param_desc_By_ID = "param_desc"
    Click_tag_type_By_ID = "system_tag_type"
    Select_tag_type_By_Xpath = "//div[contains(@class,'ng-option')]/span[text()='Raw']"
    Click_data_type_By_ID = "data_type"
    select_data_type_By_Xpath = "//div[contains(@class,'ng-option')]/span[text()='Double']"
    Save_Param_name_By_ID = "param_saveP"
    Search_Param_name_By_CSS_SELECTOR = "input[class='ag-input-field-input ag-text-field-input']"
    Edit_Param_name_By_ID = "action_edit_0"
    Delete_parameter_By_ID = "action_delete_0"
    Confirm_Delete_By_ID = "btn_confirm_delete"
    Upload_Parameters="upload"
    File_Upload="(//input[@id='fileBlock'])[1]"
    Preview_File="//button[contains(text(),'Preview')]"
    Save_File="(//button[contains(text(),'Save')])[1]"


     # driver.get_screenshot_as_png()

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def expand_navigation(self):
        # Updated the find_element method to use the new syntax
        self.driver.find_element(By.XPATH, self.Expand_Navigation_By_XPATH).click()
        self.driver.find_element(By.XPATH, self.Select_AssetManagment_By_XPATH).click()
        self.driver.find_element(By.XPATH, self.Select_Parameters_By_XPATH).click()
        time.sleep(5)


    def create_parameter_Category(self):
        # Using the updated syntax for element interaction
        self.driver.find_element(By.ID, self.Select_ParameterCategory_By_ID).click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, self.Create_ParameterCategory_By_CSS_SELECTOR).click()
        time.sleep(5)
        random_text = "Parameter_Cat_" + ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        print("Generated random text:", random_text)  # <-- This makes it visible
        self.driver.find_element(By.ID, self.Input_ParameterCategoryName_By_ID).send_keys(random_text)
        self.driver.find_element(By.ID, self.Input_ParameterCategorydesc_By_ID).send_keys(random_text)
        self.driver.find_element(By.ID,self.Click_SubCategory_ImputField_By_ID).click()
        self.driver.find_element(By.XPATH,self.SubCategory_By_Xpath).click()
        self.driver.find_element(By.CSS_SELECTOR,self.Input_SubCategory_By_CSS_SELECTOR).send_keys(random_text)
        self.driver.find_element(By.ID, self.Save_ParameterCategory_By_ID).click()
        time.sleep(5)
        return random_text

    def Edit_parameter_Category(self, search_text):
        # Updated to use the correct syntax
        search_field = self.driver.find_element(By.CSS_SELECTOR, self.Search_Filter_By_CSS_SELECTOR)
        search_field.send_keys(search_text)
        time.sleep(5)
        self.driver.find_element(By.ID, self.Click_Edit_By_ID).click()
        time.sleep(5)
        self.driver.find_element(By.ID, self.Update_name_By_ID).send_keys(1)
        self.driver.find_element(By.ID, self.Save_ParameterCategory_By_ID).click()
        time.sleep(5)

    def Clone_Parameter_Category(self,search_text):
        search_field = self.driver.find_element(By.CSS_SELECTOR, self.Search_Filter_By_CSS_SELECTOR)
        search_field.send_keys(search_text)
        time.sleep(5)
        self.driver.find_element(By.ID,self.Clone_By_ID).click()
        time.sleep(5)
        self.driver.find_element(By.ID, self.Update_name_By_ID).send_keys(2)
        self.driver.find_element(By.ID, self.Save_ParameterCategory_By_ID).click()
        time.sleep(5)

    def delete_parameter_Category(self,search_text):
        # Updated to use the correct syntax
        self.driver.find_element(By.CSS_SELECTOR, self.Search_Filter_By_CSS_SELECTOR).send_keys(search_text)
        time.sleep(5)
        self.driver.find_element(By.ID, self.Delete_parameterCategory_By_ID).click()
        self.driver.find_element(By.ID, self.Confirm_Delete_By_ID).click()
        time.sleep(3)
        self.driver.refresh()
        self.driver.find_element(By.CSS_SELECTOR, self.Search_Filter_By_CSS_SELECTOR).send_keys(search_text)
        time.sleep(3)

    def download_parameter_Category(self):
        # Updated to use the correct syntax
        self.driver.find_element(By.ID, self.Download_parameterCategory_By_ID).click()
        time.sleep(10)

    def create_parameter_Group(self):
        self.driver.find_element(By.ID, self.Select_ParameterGroup_By_ID).click()
        time.sleep(5)
        random_text = "Parameter_Grp_" + ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        print("Generated random text:", random_text)  # <-- This makes it visible
        # Using the updated syntax for element interaction
        self.driver.find_element(By.CSS_SELECTOR, self.Create_ParameterGroup_By_CSS_SELECTOR).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.Input_ParamGroupName_By_Xpath).send_keys(random_text)
        self.driver.find_element(By.CSS_SELECTOR, self.Input_Description_By_CSS_SELECTOR).send_keys(random_text)
        # self.driver.find_element(By.CSS_SELECTOR, self.Click_SubCategory_ImputField_By_ID).click()
        # self.driver.find_element(By.XPATH, self.ParameterGroup_By_Xpath).click()
        self.driver.find_element(By.CSS_SELECTOR,self.Save_ParameterGroup_By_CSS_SELECTOR).click()

        time.sleep(5)
        return random_text

    def Edit_parameter_Group(self, search_text):
        self.driver.find_element(By.CSS_SELECTOR, self.Search_Filter_By_CSS_SELECTOR).send_keys(search_text)
        time.sleep(5)
        self.driver.find_element(By.ID, self.Click_Paramgroup_Edit_By_ID).click()
        self.driver.find_element(By.XPATH, self.Input_ParamGroupName_By_Xpath).send_keys(1)
        self.driver.find_element(By.CSS_SELECTOR,self.Save_ParameterGroup_By_CSS_SELECTOR).click()
        time.sleep(5)

    def Clone_Parameter_Group(self, search_text):
     self.driver.find_element(By.CSS_SELECTOR, self.Search_Filter_By_CSS_SELECTOR).send_keys(search_text)
     time.sleep(5)
     self.driver.find_element(By.ID,self.Clone_By_ID).click()
     time.sleep(5)
     self.driver.find_element(By.XPATH, self.Input_ParamGroupName_By_Xpath).send_keys(2)
     self.driver.find_element(By.CSS_SELECTOR,self.Save_ParameterGroup_By_CSS_SELECTOR).click()
     time.sleep(5)

    def delete_parameter_Group(self,search_text):
    # Updated to use the correct syntax
     self.driver.find_element(By.CSS_SELECTOR, self.Search_Filter_By_CSS_SELECTOR).send_keys(search_text)
     time.sleep(5)
     self.driver.find_element(By.ID, self.Delete_parameterGroup_By_ID).click()
     time.sleep(5)
     self.driver.find_element(By.ID, self.Confirm_Delete_By_ID).click()
     time.sleep(3)
     self.driver.refresh()
     self.driver.find_element(By.CSS_SELECTOR, self.Search_Filter_By_CSS_SELECTOR).send_keys(search_text)
     time.sleep(3)

    def download_parameter_Group(self):
    # Updated to use the correct syntax
     self.driver.find_element(By.ID, self.Download_parameterCategory_By_ID).click()
     time.sleep(10)


       #Create parameter

    def create_parameter(self):
      self.driver.find_element(By.ID,self.Select_Parameter_By_ID).click()
      time.sleep(5)
      # Using the updated syntax for element interaction
      self.driver.find_element(By.ID, self.Create_Parameter_By_ID).click()
      time.sleep(5)
      random_text = "Parameter_Name_" + ''.join(random.choices(string.ascii_letters + string.digits, k=6))
      print("Generated random text:", random_text)  # <-- This makes it visible
      self.driver.find_element(By.ID, self.Input_Param_name_By_ID).send_keys(random_text)
      self.driver.find_element(By.ID, self.Input_Param_desc_By_ID).send_keys(random_text)
      self.driver.find_element(By.ID, self.Click_tag_type_By_ID).click()
      time.sleep(2)
      self.driver.find_element(By.XPATH, self.Select_tag_type_By_Xpath).click()
      time.sleep(2)
      self.driver.find_element(By.ID, self.Click_data_type_By_ID).click()
      self.driver.find_element(By.XPATH, self.select_data_type_By_Xpath).click()
      self.driver.find_element(By.ID, self.Save_Param_name_By_ID).click()
      self.driver.find_element(By.ID, self.Save_Param_name_By_ID).click()
      time.sleep(5)
      return random_text

    def Edit_parameter(self, search_text):
      self.driver.find_element(By.CSS_SELECTOR, self.Search_Filter_By_CSS_SELECTOR).send_keys(search_text)
      time.sleep(7)
      self.driver.find_element(By.ID, self.Edit_Param_name_By_ID).click()
      time.sleep(3)
      self.driver.find_element(By.ID, self.Input_Param_name_By_ID).send_keys(1)
      self.driver.find_element(By.ID, self.Save_Param_name_By_ID).click()
      time.sleep(3)
      self.driver.find_element(By.ID, self.Save_Param_name_By_ID).click()
      time.sleep(5)

    def Clone_Parameter(self, search_text):
      self.driver.find_element(By.CSS_SELECTOR, self.Search_Filter_By_CSS_SELECTOR).send_keys(search_text)
      time.sleep(5)
      self.driver.find_element(By.ID, self.Clone_By_ID).click()
      time.sleep(5)
      self.driver.find_element(By.ID, self.Input_Param_name_By_ID).send_keys(2)
      self.driver.find_element(By.ID, self.Save_Param_name_By_ID).click()
      time.sleep(3)
      self.driver.find_element(By.ID, self.Save_Param_name_By_ID).click()
      time.sleep(5)

    def delete_parameter(self,search_text):
      # Updated to use the correct syntax
      self.driver.find_element(By.CSS_SELECTOR, self.Search_Filter_By_CSS_SELECTOR).send_keys(search_text)
      time.sleep(5)
      self.driver.find_element(By.ID, self.Delete_parameter_By_ID).click()
      self.driver.find_element(By.ID, self.Confirm_Delete_By_ID).click()
      self.driver.refresh()
      time.sleep(3)
      self.driver.find_element(By.CSS_SELECTOR, self.Search_Filter_By_CSS_SELECTOR).send_keys(search_text)
      time.sleep(5)

    def download_parameter(self):
    # Updated to use the correct syntax
     self.driver.find_element(By.ID,self.Upload_Parameters).click()
     time.sleep(3)
     file=self.driver.find_element(By.XPATH, self.File_Upload)
     time.sleep(4)
     path=r"C:\Users\mahammad.shaik\Python\Scripts\FTDM_Project\TestData\Parameter Upload.csv"
     file.send_keys(path)
     self.driver.find_element(By.XPATH, self.Preview_File).click()
     self.driver.find_element(By.XPATH,self.Save_File).click()
     time.sleep(5)
     self.driver.find_element(By.ID, self.Download_parameterCategory_By_ID).click()
     time.sleep(5)


    # Units Page






    Select_Units_By_XPATH = "//span[@title='Parameters']"
    Create_UnitGroup="button[id='addnew']"
    Group_Name="input[formcontrolname='unit_group_name']"
    Group_Description="input[formcontrolname='description']"

