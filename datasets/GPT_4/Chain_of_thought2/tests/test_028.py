import unittest
from datasets.GPT_4.Chain_of_thought2.programs.program_028 import *

class TestVersion(unittest.TestCase):
    def test_zero(self): self.assertEqual(factorial(0), 1)

    def test_one(self): self.assertEqual(factorial(1), 1)

    def test_five(self): self.assertEqual(factorial(5), 120)

    def test_ten(self): self.assertEqual(factorial(10), 3628800)

    def test_boolean_true(self): self.assertEqual(factorial(True), 1)

    def test_large_valid_input(self): self.assertEqual(factorial(15), 1307674368000)

