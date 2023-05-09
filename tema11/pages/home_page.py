from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Teme.tema11.pages.base_page import BasePage



class HomePage(BasePage):

    FORM_AUTHENTICATION = (By.LINK_TEXT, 'Form Authentication')
    INPUTS = (By.LINK_TEXT, 'Inputs')
    CONTEXT_MENU =  (By.LINK_TEXT, 'Context Menu')
    HOME_PAGE_URL = "https://the-internet.herokuapp.com"

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 10)

    def navigate_to_home_page(self):
        self.driver.get(self.HOME_PAGE_URL)

    def click_elements_form(self):
        self.click(self.FORM_AUTHENTICATION)

    def click_elements_inputs(self):
        self.click(self.INPUTS)

    def click_elements_context_menu(self):
        self.click(self.CONTEXT_MENU)






