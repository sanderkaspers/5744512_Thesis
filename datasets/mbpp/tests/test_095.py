import unittest
from datasets.mbpp.programs.program_095 import *

class TestVersion(unittest.TestCase):
    def test_perimeter_pentagon_with_5_expect_25(self):
        self.assertEqual(perimeter_pentagon(5), 25)

    def test_perimeter_pentagon_with_10_expect_50(self):
        self.assertEqual(perimeter_pentagon(10), 50)

    def test_perimeter_pentagon_with_15_expect_75(self):
        self.assertEqual(perimeter_pentagon(15), 75)

