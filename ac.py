import time

from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class test_orange_hrm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login_hrm(self):
        driver = self.driver
        driver.implicitly_wait(3)
        driver.get("https://testautomationpractice.blogspot.com/")
        driver.maximize_window()
        copy = driver.find_element(By.PARTIAL_LINK_TEXT, "Text")

        action = ActionChains(driver)
        action.double_click(copy).perform()
        time.sleep(3)


if __name__ == "__main__" :
    unittest.main()
