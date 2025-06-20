import unittest
from datasets.GPT_4.Few_shot.programs.program_005 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_case_2(self):
        self.assertEqual(square_perimeter(1), 4)

    def test_case_3(self):
        self.assertEqual(square_perimeter(10), 40)

    def test_case_4(self):
        self.assertEqual(square_perimeter(1000000), 4000000)

    def test_case_5(self):
        self.fail("Negative input not supported by implementation; test would hang.") #  self.assertEqual(square_perimeter(-5), -20)

    def test_case_6(self):
        self.assertEqual(square_perimeter(2.5), 10.0)

