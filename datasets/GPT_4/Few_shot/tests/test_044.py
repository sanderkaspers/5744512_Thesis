import unittest
from datasets.GPT_4.Few_shot.programs.program_044 import *

class TestVersion(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(divisor(10), 5) # Largest divisor of 10)

    def test_case_2(self):
        self.assertEqual(divisor(16), 8) # Largest divisor of 16)

    def test_case_3(self):
        self.assertEqual(divisor(13), 1) # Prime number)

    def test_case_4(self):
        self.assertEqual(divisor(1), 1) # Edge case n = 1)

    def test_case_5(self):
        self.assertEqual(divisor(100), 50) # Large number)

    def test_case_6(self):
        self.assertEqual(divisor(25), 5) # Perfect square)

    def test_case_7(self):
        self.assertEqual(divisor(18), 9) # Composite number)

    def test_case_8(self):
        self.assertEqual(divisor(6), 3) # Small composite number)

