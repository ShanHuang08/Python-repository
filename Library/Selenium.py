from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class SeleniumBase():
    
    def Open_Chrome(self, path):
        self.driver = webdriver.Chrome(service=Service('chromedriver.exe'))
        return self.driver

    def find_ID(self, value):
        self.driver.find_element(By.ID, value=value)