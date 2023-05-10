import time
import unittest
from selenium.webdriver.common.by import By
from Teme.tema11.pages import home_page
from Teme.tema11.pages.home_page import HomePage
from Teme.tema11.pages import base_page
from Teme.tema11.utils.driverfactory import DriverFactory

class TestHomePage(unittest.TestCase):
    EXPECTED_URL_FORM = "https://the-internet.herokuapp.com/login"
    EXPECTED_URL_INPUTS = "https://the-internet.herokuapp.com/inputs"
    EXPECTED_URL_CONTEXT_MENU = "https://the-internet.herokuapp.com/context_menu"



    def setUp(self):
        self.driver = DriverFactory.get_driver()
        navigate = HomePage(self.driver)
        navigate.navigate_to_home_page()

    def tearDown(self):
        self.driver.quit()


    def test_click_elements_form(self):
        home_page = HomePage(self.driver)
        home_page.click_elements_form()
        current_url = self.driver.current_url
        self.assertEqual(current_url, self.EXPECTED_URL_FORM)


    def test_click_elements_inputs(self):
        home_page = HomePage(self.driver)
        home_page.click_elements_inputs()
        current_url = self.driver.current_url
        self.assertEqual(current_url, self.EXPECTED_URL_INPUTS)

    def test_click_elements_context_menu(self):
        home_page = HomePage(self.driver)
        home_page.click_elements_context_menu()
        current_url = self.driver.current_url
        self.assertEqual(current_url, self.EXPECTED_URL_CONTEXT_MENU)

























