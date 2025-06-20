import unittest
from datasets.GPT_4.Few_shot.programs.program_089 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(div_sum(28), 28) # Perfect number)

    def test_case_2(self):
        self.assertEqual(div_sum(6), 6) # Small perfect number)

    def test_case_3(self):
        self.assertEqual(div_sum(12), 16) # Composite number)

    def test_case_4(self):
        self.assertEqual(div_sum(1), 1) # Edge case n = 1)

    def test_case_5(self):
        self.assertEqual(div_sum(25), 6) # Square number (5^2))

    def test_case_6(self):
        self.assertEqual(div_sum(97), 1) # Prime number)

    def test_case_7(self):
        self.assertEqual(div_sum(100), 117) # Larger composite number)

    def test_case_8(self):
        self.assertEqual(div_sum(50), 43) # Composite number with non-trivial divisors)

