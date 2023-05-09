
import unittest
import HtmlTestRunner


from Teme.tema11.tests.test_home_page import TestHomePage
from Teme.tema11.tests.test_login_page import TestLoginPage


class TestSuite(unittest.TestCase):

    def test_suite(self):

        teste_de_rulat = unittest.TestSuite()
        # adaugam testele in suita
        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestHomePage),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestLoginPage),
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="Test report",
            report_name="Test Results"
        )

        runner.run(teste_de_rulat)
