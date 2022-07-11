import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class test_flipkart_login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_login(self):
        driver = self.driver
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get('https://www.flipkart.com/')
        driver.find_element(By.CSS_SELECTOR ,"[class='_2MlkI1'] div form input[type='text']").send_keys('pkrnosam@gmail.com')
        driver.find_element(By.CSS_SELECTOR , "[type='password']").send_keys('Pavan@313')
        driver.find_element(By.CSS_SELECTOR , "button[class='_2KpZ6l _2HKlqd _3AWRsL'] ").click()
        time.sleep(2)
        #driver.close()

if __name__ == "__main__" :
    unittest.main()

