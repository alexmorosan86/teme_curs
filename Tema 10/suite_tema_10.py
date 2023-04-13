import unittest
import HtmlTestRunner
from teste import TestNewUrl
from teste import TestEmptyCredentials
from teste import TestPageTitle
from teste import TestHeadingText
from teste import TestButtonLoginDisplayed
from teste import TestHrefCorrect
from teste import TestInvalidCredentials
from teste import LoginLogout
from teste import AddElements
from teste import DisappearingElements
from teste import UserPassIsExpected



class TestSuite(unittest.TestCase):

    def test_suite(self):
        teste_de_rulat = unittest.TestSuite()
        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestNewUrl),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestEmptyCredentials),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestPageTitle),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestHeadingText),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestButtonLoginDisplayed),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestHrefCorrect),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestInvalidCredentials),
            unittest.defaultTestLoader.loadTestsFromTestCase(LoginLogout),
            unittest.defaultTestLoader.loadTestsFromTestCase(UserPassIsExpected),
            unittest.defaultTestLoader.loadTestsFromTestCase(AddElements),
            unittest.defaultTestLoader.loadTestsFromTestCase(DisappearingElements)

        ])

        # vom crea o variabila de tip HTMLTestRunner care ne ajuta in executarea testelor din suita
        # si ne va genera un raport HTML cu rezultatele testelor
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,  # vrem sa ne genereze un singur raport pentru toate clasele
            report_title="My first test report",
            report_name="Test Results"
        )

        runner.run(teste_de_rulat)