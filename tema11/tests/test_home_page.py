
import unittest
from selenium.webdriver.common.by import By
from Teme.tema11.pages import home_page
from Teme.tema11.pages.home_page import HomePage
from Teme.tema11.pages import base_page
from Teme.tema11.utils.driverfactory import DriverFactory

class TestHomePage(unittest.TestCase):
    FORM_AUTHENTICATION = (By.LINK_TEXT, 'Form Authentication')
    INPUTS =  (By.LINK_TEXT, 'Inputs')
    CONTEXT_MENU =  (By.LINK_TEXT, 'Context Menu')
    HOME_PAGE_URL = 'https://the-internet.herokuapp.com'


    def setUp(self):
        self.driver = DriverFactory.get_driver()

        navigate = HomePage(self.driver)
        navigate.navigate_to_home_page()

    def tearDown(self):
        self.driver.quit()


    def test_click_elements_form(self):
        home_page_element = HomePage(self.driver)
        home_page_element.click_elements_form()

    def test_click_elements_inputs(self):
        home_page_element = HomePage(self.driver)
        home_page_element.click_elements_inputs()

    def test_click_elements_context_menu(self):
        home_page_element = HomePage(self.driver)
        home_page_element.click_elements_context_menu()

























