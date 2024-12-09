from selenium.webdriver.common.by import By


class Registration_Page_Class:
    text_name_id = "name"
    text_confirm_password_id = "password-confirm"

    def __init__(self, driver):
        self.driver = driver

    def Enter_Name(self, name):
        self.driver.find_element(By.ID, self.text_name_id).send_keys(name)

    def Enter_Confirm_Password(self, password):
        self.driver.find_element(By.ID, self.text_confirm_password_id).send_keys(password)


