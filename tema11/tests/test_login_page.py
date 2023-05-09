import time
import unittest
from selenium.webdriver.common.by import By
from Teme.tema11.pages import login_page
from Teme.tema11.pages.login_page import LoginPage
from Teme.tema11.pages import base_page
from Teme.tema11.utils.driverfactory import DriverFactory



class TestLoginPage(unittest.TestCase):
    USER_NAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.XPATH, '//*[@id="login"]/button')
    LOGIN_PAGE_URL = "https://the-internet.herokuapp.com/login"
    SUCCESS_MESSAGE = (By.ID, "flash")
    LOGOUT_BTN = (By.ID,  "content")


    def setUp(self):
        self.driver = DriverFactory.get_driver()
        self.login_page = LoginPage(self.driver)
        self.login_page.navigate_to_login_page()

    def tearDown(self):
        self.driver.quit()

    def test_set_user_name(self):
        self.login_page.set_user("tomsmith")
        time.sleep(1)

    def test_set_password(self):
        self.login_page.set_password("SuperSecretPassword!")
        time.sleep(1)

    def test_click_login_btn(self):
        self.login_page.click_login_btn()
        time.sleep(1)

    def test_success_message_is_displayed(self):
        self.login_page.set_user("tomsmith")
        self.login_page.set_password("SuperSecretPassword!")
        self.login_page.click_login_btn()
        self.assertTrue(self.login_page.success_message_is_displayed())
        time.sleep(1)

    def test_click_logout_btn(self):
        self.login_page.set_user("tomsmith")
        self.login_page.set_password("SuperSecretPassword!")
        self.login_page.click_login_btn()
        self.login_page.click_logout_btn()
        time.sleep(1)


































