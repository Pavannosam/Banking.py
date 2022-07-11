import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class test_flipkart_login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def login(self):
        driver = self.driver
        driver.get('https://www.flipkart.com/')
        driver.find_element(By.CLASS_NAME , "_1_3w1N").click()
        driver.find_element(By.CLASS_NAME ,"_2IX_2- VJZDxU").send_keys('pkrnosam@gmail.com')
        driver.find_element(By.CLASS_NAME , "_2IX_2- _3mctLh VJZDxU").send_keys('Pavan@313')
        driver.find_element(By.CSS_SELECTOR , "button[class='_2KpZ6l _2HKlqd _3AWRsL'] ").click()
        time.sleep(2)
        driver.close()

if __name__ == "__main__" :
    unittest.main()