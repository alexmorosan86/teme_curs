import time
from lib2to3.pgen2 import driver
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




class Login(TestCase):
    driver = None
    LINK = "https://the-internet.herokuapp.com/"


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.LINK)
        self.driver.find_element(By.LINK_TEXT, "Form Authentication").click()
        self.driver.maximize_window()
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    def wait_for_element_to_be_present(self, element_locator, seconds_to_wait):
        wait = WebDriverWait(self.driver, seconds_to_wait)
        return wait.until(EC.presence_of_element_located(element_locator))

    def test_valid_credentials(self):
        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys("tomsmith")
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys("SuperSecretPassword!")
        self.driver.find_element(By.XPATH, "//*[@class='radius']").click()
        actual_url = self.driver.current_url
        expected_url = 'https://the-internet.herokuapp.com/secure'
        self.assertEqual(actual_url, expected_url, 'Eroare')

    def test_new_url(self):
        expected_url = "https://the-internet.herokuapp.com/login"
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"Invalid URL, expected {expected_url}, but found {actual_url}"

    def test_page_title(self):
        expected_title = "The Internet"
        actual_title = self.driver.title
        assert expected_title == actual_title, f"Invalid title, expected {expected_title}, but found {actual_title}"

    def test_heading_text(self):
        expected_text = self.driver.find_element(By.XPATH, "//h2").text
        actual_text = "Login Page"
        assert expected_text == actual_text, f"Invalid text, expected {expected_text}, but found {actual_text}"

    def test_btn_login_is_displayed(self):
        login_button = self.driver.find_element(By.XPATH, "//*[@class='fa fa-2x fa-sign-in']")
        # self.assertIsNotNone(login_button, "Butonul de login nu este prezent pe pagina.")
        self.assertTrue(login_button.is_displayed(), "Butonul de login nu este afișat pe pagina.")

    def test_href_atrribute_is_correct(self):
        element = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/a")
        element_href = element.get_attribute("href")
        self.assertEqual(element_href, 'http://elementalselenium.com/')

    def test_empty_credentials(self):
        self.driver.find_element(By.XPATH, "//*[@id='username']")
        self.driver.find_element(By.XPATH, "//*[@id='password']")
        self.driver.find_element(By.XPATH, "//*[@class='radius']").click()
        error_message = self.driver.find_element(By.XPATH, "//*[@id='flash']")
        assert error_message.is_displayed()

    def test_invalid_credentials(self):
        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys("sajdjsadja")
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(13123123)
        self.driver.find_element(By.XPATH, "//*[@class='radius']").click()
        error_message = self.driver.find_element(By.XPATH, "//*[@id='flash']").text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in error_message, 'Error message is incorrect')

    def test_login_logout(self):
        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys("tomsmith")
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys("SuperSecretPassword!")
        self.driver.find_element(By.XPATH, "//*[@class='radius']").click()
        self.driver.find_element(By.XPATH, "//*[@class='button secondary radius']").click()
        expected_url = "https://the-internet.herokuapp.com/login"
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"Invalid URL, expected {expected_url}, but found {actual_url}"


    def test_username_and_pass_is_text_expected(self):
        labels = self.driver.find_elements(By.XPATH, "//label[@for]")
        expected_texts = ["Username", "Password"]
        for label in labels:
            text = label.text
            self.assertIn(text, expected_texts, f"Textul de pe {label} este 'Username' si 'Password'.")

# Clasa noua creata cu functii de test


class AddElements(TestCase):
    driver = None
    LINK = "https://the-internet.herokuapp.com/"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.LINK)
        self.driver.find_element(By.LINK_TEXT, "Add/Remove Elements").click()
        self.driver.maximize_window()
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    def test_add_element(self):
        self.driver.find_element(By.XPATH, '//button[@onclick="addElement()"]').click()
        button = self.driver.find_element(By.CLASS_NAME, "added-manually")
        text = button.text
        expected_text = "Delete"
        self.assertTrue(text, expected_text)

#test fdbdfbderf











