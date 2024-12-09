import time

import faker
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.Login_Page import Login_Page_Class
from pageObjects.Registration_Page import Registration_Page_Class


class Test_User_Profile_Class_001:
    """Test cases for the UserProfile class."""
    def test_verify_CredKart_Url_001(self, driver_setup):
        """Test verify_credkart_url method with valid URL."""
        driver = driver_setup
        driver.maximize_window()
        driver.get("https://automation.credence.in/")
        if driver.title == "CredKart":
            print("Test passed: Title matches with expected title")
            driver.save_screenshot(".\\Screenshots\\test_verify_CredKart_Url_001_pass.png")
            assert True
        else:
            driver.save_screenshot(".\\Screenshots\\test_verify_CredKart_Url_001_fail.png")
            print("Test failed: Title does not match with expected title")
            assert False


    def test_CredKart_User_Login_002(self, driver_setup):
        """Test verify_user_login method with valid credentials."""
        self.driver = driver_setup
        self.lp = Login_Page_Class(self.driver)
        self.driver.maximize_window()
        self.driver.get("https://automation.credence.in/login")


        # Enter the username
        # username = driver.find_element(By.ID, "email")
        # username.send_keys("Credencetest@test.com")
        self.lp.Enter_Email("Credencetest@test.com")


        # Enter the password
        # password = driver.find_element(By.ID, "password")
        # password.send_keys("Credence@1234")
        self.lp.Enter_Password("Credence@123")

        # Click the login button
        #driver.find_element(By.CLASS_NAME, "btn").click()
        self.lp.Click_submit_Button()

        # Verify that the user is logged in
        # try:
        #     #MenuButton = driver.find_element(By.CLASS_NAME, "dropdown-toggle")
        #     MenuButton = driver.find_element(By.XPATH, "//a[@class='dropdown-toggle']")
        #     time.sleep(5)  # Wait for the page to load completely before checking the visibility of the element.
        #     assert MenuButton.is_displayed(), "User is not logged in"
        #     print("User is logged in")
        # except:
        #     print("User is not logged in")
        if self.lp.verify_user_Login_or_registration() == "pass":
            print("User is logged in")
            self.driver.save_screenshot(".\\Screenshots\\test_CredKart_User_Login_002_pass.png")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_CredKart_User_Login_002_fail.png")
            print("User is not logged in")
            assert False


    def test_CredKart_User_Registration_003(self, driver_setup, faker):
        """Test verify_user_login method with valid credentials."""
        self.driver = driver_setup
        self.lp = Login_Page_Class(self.driver)
        self.rp = Registration_Page_Class(self.driver)
        self.driver.get("https://automation.credence.in/register")

        random_name = faker.name()
        random_email = faker.email()
        # Enter the Name
        self.rp.Enter_Name(random_name)
        # Enter the Email
        self.lp.Enter_Email(random_email)
        # Enter the Password
        self.lp.Enter_Password("Credence@123")
        # Enter the Confirm Password
        self.rp.Enter_Confirm_Password("Credence@123")
        # Click the register button
        self.lp.Click_submit_Button()
        if self.lp.verify_user_Login_or_registration() == "pass1":
            print("User is registered")
            self.driver.save_screenshot(".\\Screenshots\\test_CredKart_User_Registration_003_pass.png")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_CredKart_User_Registration_003_fail.png")
            print("User is not registered")
            assert False


"pytest -v -n auto --html=HtmlReports/my_report.html --browser chrome"