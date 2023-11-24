from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from Library.Call_Method import Check_PWD

class Selenium_test:
    def __init__(self) -> None:
        self.driver = webdriver
        # self.server_ip = input('Input server ip: ')
        # self.pwd = Check_PWD(self.server_ip)[1]

    def Open_Chrome(self):
        self.browser = self.driver.Chrome('C:\\Users\\Stephenhuang\\Python\\chromedriver.exe')

    

    
    def find_ID(self, ID:str):
        self.browser.find_element(By.ID, value=ID)

    def find_IDs(self, ID:str):
        self.browser.find_elements(By.ID, value=ID)

    def find_name(self, NAME:str):
        self.browser.find_element(By.NAME, value=NAME)

    def find_names(self, NAME:str):
        self.browser.find_elements(By.NAME, value=NAME)

    def find_xpath(self, xpath:str):
        self.browser.find_element(By.XPATH, value=xpath)

    def find_xpaths(self, xpath:str):
        self.browser.find_elements(By.XPATH, value=xpath)
    
    
    def Open_Firefox(self):
        self.browser = self.driver.Firefox()