import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")

@pytest.fixture
def driver_setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print("launching chrome browser")
        driver = webdriver.Chrome()
    elif browser == "firefox":
        print("launching firefox browser")
        driver = webdriver.Firefox()
    elif browser == "edge":
        print("launching edge browser")
        driver = webdriver.Edge()
    elif browser == "headless":
        print("chrome headless browser started")
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no visible browser windows)
        driver = webdriver.Chrome(options=chrome_options)
    else:
        print("Chrome browser started")
        driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver # driver is return to the test cases or method
    driver.quit()
    print("Browser closed")


def pytest_metadata(metadata):
    metadata["Class"] = "Credence_Test#20"
    metadata["Description"] = "Test to verify the Credence homepage and search functionality"
    metadata["Test Type"] = "Functional"
    metadata["Author"] = "Credence : Test Automation Team"
    metadata["URL"] = "https://automation.credence.in/" # to add url key in report
    metadata.pop("Platform", None) # to remove the platform key
    # metadata.pop("Plugins", None)
    # How to edit summary in html report is your task