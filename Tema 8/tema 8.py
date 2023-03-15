# Exerciții obligatorii - grad de dificultate: Usor spre Mediu
# Alege-ți unuul sau mai multe din sugestiile de site-uri de mai jos
# - https://www.phptravels.net/
# - http://automationpractice.com/index.php
# - https://formy-project.herokuapp.com/
# - https://the-internet.herokuapp.com/
# - https://www.techlistic.com/p/selenium-practice-form.html
# - jules.app
import time
from lib2to3.pgen2 import driver

# Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
# ● Id
# ● Link text
# ● Parțial link text
# ● Name
# ● Tag*
# ● Class name*
# ● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)


# observație:
# - Probabil nu vei găsi un singur website care să cuprindă toate variantele
# de mai sus, astfel că îți recomandăm să folosești mai multe site-uri
#

# - Opțional: La tag și class name vei folosi find elementS! - salvează în listă.
# Interactionează cu un element la alegere din listă.
# Pentru xpath identifică elemente după criteriile de mai jos:
# ● 3 după atribut valoare
# ● 3 după textul de pe element
# ● 1 după parțial text
# ● 1 cu SAU, folosind pipe |
# ● 1 cu *
# ● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci
# cu (xpath)[1]
# ● 1 în care să folosești parent::
# ● 1 în care să folosești fratele anterior sau de după (la alegere)
# ● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu
# ce element vreau să interacționez.
# Exerciții extra - Opțional
# https://www.automatetheplanet.com/most-exhaustive-xpath-locators-cheat-sh
#
#
# work site : https://www.techlistic.com/p/selenium-practice-form.html
# work site : https://formy-project.herokuapp.com/buttons


# driver = webdriver.Chrome()
# LINK = "https://www.techlistic.com/p/selenium-practice-form.html"
#
# driver.get(LINK)
# driver.maximize_window()
# time.sleep(2)
# button = driver.find_element(By.XPATH, "//*[@id='ez-accept-all']")
# button.click()
# time.sleep(10)




# 3 elemente dupa id
#
# //*[@id="exp-0"]
# //*[@id="exp-1"]
# //*[@id="exp-2"]

# [id="exp-3"]
# [id="exp-4"]
# [id="exp-5"]



# 3 elemete dupa link-text

# link_text = driver.find_element(By.LINK_TEXT, "Automate Amazon like E-Commerce website with Selenium")
# link_text = driver.find_element(By.LINK_TEXT, "Automate GoDaddy website features with Selenium")
# link_text = driver.find_element(By.LINK_TEXT, "Automate Google search with Selenium")

# 3 elemete dupa partial link-text

# partial_link_text = driver.find_element(By.PARTIAL_LINK_TEXT, "Automate Amazon like")
# partial_link_text = driver.find_element(By.PARTIAL_LINK_TEXT, "Automate GoDaddy website")
# partial_link_text = driver.find_element(By.PARTIAL_LINK_TEXT, "Automate Google search")

# 3 elemente dupa name
# first_name = driver.find.element((By.NAME, 'firstname'))
# last_name = driver.find.element((By.NAME, 'lastname'))
# continents = driver.find.element((By.NAME, 'continents'))

# input[name="firstname"]
# input[name="lastname"]
# input[name="continents"]

# input#sex-0
# input#sex-1
# input#datepicker


# 3 elemente dupa TAG

# dupa_tag_name_1 = driver.find_element(By.TAG_NAME, 'input')
# dupa_tag_name_2 = driver.find_element(By.TAG_NAME, 'select')
# dupa_tag_name_3 = driver.find_element(By.TAG_NAME, 'div')


# 3 elemente dupa class name

# element_1_by_class_name = driver.find.elemeny(By.CLASS_NAME, 'control-group')
# element_2_by_class_name = driver.find.elemeny(By.CLASS_NAME, 'input-file')
# element_3_by_class_name = driver.find.elemeny(By.CLASS_NAME, 'controls')

#Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)

# dupa id
# #postal_code

# dupa clasa
#.input-file

#după atribut=valoare_partiala)
# //input[contains(@id,'date')]
# //input[contains(@id,'street')]
# //input[contains(@id,'administrative')]

# Pentru xpath identifică elemente după criteriile de mai jos:

# 3 elemente dupa atribut-valoare:

# //*[@id="sex-0"]
# //*[@id="datepicker"]
# //*[@id="photo"]

# 3 după textul de pe element

# //button[text()='Right']
# //button[text()='Middle']
# //button[text()='Left']

# 1 după parțial text
#//a[contains(text(), 'Drag')]

# 1 cu *

# //*[@id='street_number']

# ● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci
# cu (xpath)[1]
# //*[@id="continents"]/option[1]

# 1 în care să folosești parent::

# //parent::div[@class='col-sm-8']
# //parent::div[@class='dropdown-menu show']

# 1 în care să folosești fratele anterior sau de după (la alegere)
# //following-sibling::p [2]

# 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu
# ce element vreau să interacționez.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# LINK = "https://formy-project.herokuapp.com/modal"
#
# driver.get(LINK)
# driver.maximize_window()
# time.sleep(2)
# button = driver.find_element(By.XPATH, '//*[@id="modal-button"]')
# button.click()
# time.sleep(2)
# close = driver.find_element(By.XPATH, '//*[@id="close-button"]')
# close.click()
# time.sleep(2)
# driver.quit()

def interact_with_element(link, element_xpath):
    driver = webdriver.Chrome()
    driver.get(link)
    driver.maximize_window()
    time.sleep(2)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, element_xpath)))
    element.click()
    time.sleep(2)
    driver.quit()

LINK = "https://formy-project.herokuapp.com/modal"
ELEMENT_XPATH = '//*[@id="modal-button"]'
interact_with_element(LINK, ELEMENT_XPATH)



