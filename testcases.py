import unittest
from selenium import webdriver
from vourne import login, configurator, technology, consolidate, summary, saved_business
from colorama import init, Fore, Style


class VourneTesting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome_driver_path = "C:\\proj\\chromedriver.exe"
        service = webdriver.chrome.service.Service(executable_path=chrome_driver_path)
        cls.driver = webdriver.Chrome(service=service)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def print_passed(self, message):
        print(f"{Fore.GREEN}{message}{Style.RESET_ALL}")

    def print_failed(self, message):
        print(f"{Fore.RED}{message}{Style.RESET_ALL}")

    def test_login(self):
        print("\nLogin Test Running......")
        result = login(self.driver)
        self.assertTrue(result)
        if result:
            self.print_passed("Login Test Result: PASSED")
        else:
            self.print_failed("Login Test Result: FAILED")
        print("_________________________________________________________________________")

    def test_configurator(self):
        print("\nConfigurator Test Running......")
        result = configurator(self.driver)
        self.assertTrue(result)
        if result:
            self.print_passed("Configurator Test Result: PASSED")
        else:
            self.print_failed("Configurator Test Result: FAILED")
        print("_________________________________________________________________________")

    def test_technology(self):
        print("\nTechnology Test Running......")
        result = technology(self.driver)
        self.assertTrue(result)
        if result:
            self.print_passed("Technology Test Result: PASSED")
        else:
            self.print_failed("Technology Test Result: FAILED")
        print("_________________________________________________________________________")

    def test_consolidate(self):
        print("\nConsolidate Test Running......")
        result = consolidate(self.driver, "consolidated_data.csv")
        self.assertTrue(result)
        if result:
            self.print_passed("Consolidate Test Result: PASSED")
        else:
            self.print_failed("Consolidate Test Result: FAILED")
        print("_________________________________________________________________________")

    def test_summary(self):
        print("\nSummary Test Running......")
        result = summary(self.driver)
        self.assertTrue(result)
        if result:
            self.print_passed("Summary Test Result: PASSED")
        else:
            self.print_failed("Summary Test Result: FAILED")
        print("_________________________________________________________________________")

    def test_saved_business(self):
        print("\nSaved Business Test Running......")
        result = saved_business(self.driver)
        self.assertTrue(result)
        if result:
            self.print_passed("Saved Business Test Result: PASSED")
        else:
            self.print_failed("Saved Business Test Result: FAILED")
        print("_________________________________________________________________________")


if __name__ == '__main__':
    init()  # Initialize colorama
    suite = unittest.TestSuite()
    suite.addTest(VourneTesting('test_login'))
    suite.addTest(VourneTesting('test_configurator'))
    suite.addTest(VourneTesting('test_technology'))
    suite.addTest(VourneTesting('test_consolidate'))
    suite.addTest(VourneTesting('test_summary'))
    suite.addTest(VourneTesting('test_saved_business'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
