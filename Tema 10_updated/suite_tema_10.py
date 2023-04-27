import unittest
import HtmlTestRunner
from teste import Login




class TestSuite(unittest.TestCase):

    def test_suite(self):
        teste_de_rulat = unittest.TestSuite()
        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login)


        ])

        # vom crea o variabila de tip HTMLTestRunner care ne ajuta in executarea testelor din suita
        # si ne va genera un raport HTML cu rezultatele testelor
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,  # vrem sa ne genereze un singur raport pentru toate clasele
            report_title="My first test report",
            report_name="Test Results"
        )

        runner.run(teste_de_rulat)

        #;dsfvsdfv