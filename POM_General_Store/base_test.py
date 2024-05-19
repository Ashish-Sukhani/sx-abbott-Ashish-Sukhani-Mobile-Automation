import unittest
from capabilities import init_driver

class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = init_driver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()