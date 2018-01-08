import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class Test(unittest.TestCase):

    def setUp(self):
        chromePath = r"D:\Chrome Downloads\webdrivers\chromedriver.exe"
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory" : r"C:\Users\Justin\Desktop\Cascade CSV Export Files"}
        chromeOptions.add_experimental_option("prefs", prefs)
        
        self.driver = webdriver.Chrome(executable_path=chromePath, chrome_options=chromeOptions)
        self.driver.get("https://ap.unleashedsoftware.com/v2/Enquiry/SalesEnquiry")
                
    def test_unleashed(self):
        driver = self.driver
        
        # Log In into Unleashed
        UnleashedUsername = "connor@cellese.com"
        UnleashedPassword = "3rZup3WiqEi9"
        emailFieldID = "username"
        passFieldID = "password"
        loginButtonXpath = """//input[@value='Log In']"""
        
        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
        passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldID))
        loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))

        emailFieldElement.clear()
        emailFieldElement.send_keys(UnleashedUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(UnleashedPassword)
        loginButtonElement.click()
        
        # Export CSV file
        exportButtonXpath = """//*[@id="ddbExport"]/dl/dd/ul/li[2]/a"""
        
        exportDropdownElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_class_name("arrowDown"))
        exportDropdownElement.click()
                
        exportButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(exportButtonXpath))
        exportButtonElement.click()
       
        # Wait for file to download
        time.sleep(10)

        # Rename CSV file with date and time
        timestr = time.strftime("%Y%m%d-%H%M%S")
        old_file = os.path.join(r"C:\Users\Justin\Desktop\Cascade CSV Export Files", "SalesEnquiryList.csv")
        new_file = os.path.join(r"C:\Users\Justin\Desktop\Cascade CSV Export Files", "SalesEnquiryList " + timestr + ".csv")
        os.rename(old_file, new_file)        
        
        # keep window open for 10 seconds 
        time.sleep(10)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()