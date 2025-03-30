import unittest
from selenium import webdriver
from selenium.webdriver import FirefoxService
from selenium.webdriver.chrome.service import Service



class Config(unittest.TestCase):

    def setUp(self) -> None:
        service = Service(r"C:\Users\jose.velasquez\Desktop\Drivers\chromedriver-win64\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.convertworld.com/es/")
        self.driver.implicitly_wait(10)


    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()





