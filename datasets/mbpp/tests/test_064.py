import unittest
from datasets.mbpp.programs.program_064 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(max_product_tuple([(2, 7)]))

    def test_case_2(self):
        self.assertTrue(max_product_tuple([(10, 20)]))

    def test_case_3(self):
        self.assertTrue(max_product_tuple([(11, 44)]))

