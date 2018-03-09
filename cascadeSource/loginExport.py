import time
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# Change sys path
sys.path.insert(0, 'cascadeSource/config/')
from config import username, password


def loginExport():
    # setUp
    chromePath = "cascadeSource/webdriver/chromedriver.exe"
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory": r"D:\Cellese Unleashed Cascade\SalesEnquiries"}
    chromeOptions.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(
        executable_path=chromePath, chrome_options=chromeOptions)

    driver.get("https://ap.unleashedsoftware.com/v2/Enquiry/SalesEnquiry")
    driver.maximize_window()

    # Log In into Unleashed
    UnleashedUsername = username
    UnleashedPassword = password
    emailFieldID = "username"
    passFieldID = "password"
    loginButtonXpath = """//input[@value='Log In']"""

    emailFieldElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_id(emailFieldID))
    passFieldElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_id(passFieldID))
    loginButtonElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(loginButtonXpath))

    emailFieldElement.clear()
    emailFieldElement.send_keys(UnleashedUsername)
    passFieldElement.clear()
    passFieldElement.send_keys(UnleashedPassword)
    loginButtonElement.click()

    # Export CSV file
    exportButtonXpath = """//*[@id="ddbExport"]/dl/dd/ul/li[2]/a"""
    exportDropdownElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_class_name("arrowDown"))
    exportDropdownElement.click()
    exportButtonElement = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(exportButtonXpath))
    exportButtonElement.click()

    # Wait for file to download
    time.sleep(10)

    # tearDown
    driver.quit()


if __name__ == '__main__':
    loginExport()
