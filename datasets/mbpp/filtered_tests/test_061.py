import unittest
from datasets.mbpp.programs.program_061 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(list_to_float([("3", "4")]))

    def test_case_2(self):
        self.assertTrue(list_to_float([("4", "4")]))

    def test_case_3(self):
        self.assertTrue(list_to_float([("6", "78")]))

