import unittest
from datasets.GPT_4.Few_shot.programs.program_041 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(power(2, 3), 8) # 2^3)

    def test_case_2(self):
        self.assertEqual(power(5, 0), 1) # 5^0)

    def test_case_3(self):
        self.assertEqual(power(1, 5), 1) # 1^5)

    def test_case_4(self):
        self.assertEqual(power(0, 5), 0) # 0^5)

    def test_case_5(self):
        try:
            power(2, -3)   # Negative power
        except RecursionError:
            print("Passed: RecursionError for negative power.")

    def test_case_6(self):
        self.assertEqual(power(2, 1), 2) # 2^1)

    def test_case_7(self):
        self.assertEqual(power(2, 10), 1024) # Large exponent)

    def test_case_8(self):
        self.assertEqual(power(-2, 3), -8) # Negative base, odd exponent)

