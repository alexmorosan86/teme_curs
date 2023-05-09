from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Teme.tema11.pages.base_page import BasePage



class LoginPage(BasePage):
    USER_NAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.XPATH, '//*[@id="login"]/button')
    LOGIN_PAGE_URL = "https://the-internet.herokuapp.com/login"
    SUCCESS_MESSAGE = (By.ID, "flash")
    LOGOUT_BTN = (By.ID, "content")


    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 10)

    def navigate_to_login_page(self):
        self.driver.get(self.LOGIN_PAGE_URL)

    def set_user(self, user_name):
        self.type(LoginPage.USER_NAME, user_name)

    def set_password(self, password):
        self.type(LoginPage.PASSWORD, password)

    def click_login_btn(self):
        self.click(self.LOGIN_BTN)

    def success_message_is_displayed(self):
        return self.is_element_displayed(self.SUCCESS_MESSAGE)

    def click_logout_btn(self):
        self.click(self.LOGOUT_BTN)





