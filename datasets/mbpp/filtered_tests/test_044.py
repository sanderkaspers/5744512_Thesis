import unittest
from datasets.mbpp.programs.program_044 import *

class TestVersion(unittest.TestCase):
    def test_divisor_with_15_expect_4(self):
        self.assertEqual(divisor(15), 4)

    def test_divisor_with_12_expect_6(self):
        self.assertEqual(divisor(12), 6)

    def test_divisor_with_9_expect_3(self):
        self.assertEqual(divisor(9), 3)

