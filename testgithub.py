from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import unittest

class SampleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_git_hub(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://github.com/')
        driver.implicitly_wait(4)
        x=ActionChains(driver)
        click_explore = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/nav/ul/li[4]/details')
        x.move_to_element(click_explore).perform()
        collections = driver.find_element(By.LINK_TEXT,"Collections")
        x.move_to_element(collections).click().perform()
        count_articles = 50
        data = driver.find_elements(By.XPATH,"//*[@id='js-pjax-container']/div[4]/article")
        print(len(data))
        assert count_articles == len(data)

if __name__ == "__main__":
    unittest.main()

