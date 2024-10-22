from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from Library.dictionary import *
from selenium.webdriver.remote.webelement import WebElement

class SeleniumBase():
    
    def Chrome(self, path):
        self.driver = webdriver.Chrome(service=Service(path+'chromedriver.exe'))
        return self.driver

    def find_ID(self, value) -> WebElement:
        #AttributeError: 'NoneType' object has no attribute 'click' add -> -> WebElement and add return
        return self.driver.find_element(By.ID, value=value)
    
    def find_Name(self, value) -> WebElement:
        return self.driver.find_element(By.NAME, value=value)
    
    def find_xpath(self, value) -> WebElement:
        return self.driver.find_element(By.XPATH, value=value)
    
    def find_IDs(self, value) -> WebElement:
        return self.driver.find_elements(By.ID, value=value)
    
    def find_Names(self, value) -> WebElement:
        return self.driver.find_elements(By.NAME, value=value)

    def find_xpaths(self, value) -> WebElement:
        return self.driver.find_elements(By.XPATH, value=value)

    def get_window_handles(self):
        """return list with handles. Cooperate with `switch_window()`"""
        return self.driver.window_handles